#!/usr/bin/env python3
"""
HashBox - Hash / Encoding / Cipher Encode-Decode & Wordlist Cracker Tool

Original: 2022, Furkan (@Kerxunos)
Refactored: 2026 - kod duzenlendi, salt kullanimi guvenlik acisindan
duzeltildi, desteklenen hash/encoding/sifre turleri genisletildi.
"""

from __future__ import annotations

import base64
import codecs
import hashlib
import os
import secrets
import sys
import zlib
from pathlib import Path
from time import sleep
from typing import Callable

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    COLOR_ENABLED = True
except ImportError:
    COLOR_ENABLED = False

    class _NoColor:
        def __getattr__(self, name):
            return ""

    Fore = Style = _NoColor()

APP_NAME = "HashBox"
APP_VERSION = "3.0"
APP_AUTHOR = "Furkan (@Kerxunos)"

BANNER = r"""
    __  __           __    ____
   / / / /___ ______/ /_  / __ )____  _  __ (R)
  / /_/ / __ `/ ___/ __ \/ __  / __ \| |/_/
 / __  / /_/ (__  ) / / / /_/ / /_/ />  <
/_/ /_/\____/____/_/ /_/_____/\____/_/|_|
"""

DEFAULT_SALT_BYTES = 16  # 128 bit - guvenli, yaygin kabul goren varsayilan uzunluk


# --------------------------------------------------------------------------- #
# HASH ALGORITMALARI (tek yonlu - geri donusumsuz)
#
# Her deger, bytes alip hex digest dondruren bir fonksiyon. Yeni bir
# algoritma eklemek icin tek yapman gereken bu sozluge bir satir eklemek.
# --------------------------------------------------------------------------- #

def _std_hash(ctor: Callable) -> Callable[[bytes], str]:
    return lambda data: ctor(data).hexdigest()


HASH_ALGORITHMS: dict[str, Callable[[bytes], str]] = {
    "md5": _std_hash(hashlib.md5),
    "sha1": _std_hash(hashlib.sha1),
    "sha224": _std_hash(hashlib.sha224),
    "sha256": _std_hash(hashlib.sha256),
    "sha384": _std_hash(hashlib.sha384),
    "sha512": _std_hash(hashlib.sha512),
    "sha3_224": _std_hash(hashlib.sha3_224),
    "sha3_256": _std_hash(hashlib.sha3_256),
    "sha3_384": _std_hash(hashlib.sha3_384),
    "sha3_512": _std_hash(hashlib.sha3_512),
    "blake2b": _std_hash(hashlib.blake2b),
    "blake2s": _std_hash(hashlib.blake2s),
    "shake128": lambda data: hashlib.shake_128(data).hexdigest(32),
    "shake256": lambda data: hashlib.shake_256(data).hexdigest(32),
    "crc32": lambda data: format(zlib.crc32(data) & 0xFFFFFFFF, "08x"),
    "adler32": lambda data: format(zlib.adler32(data) & 0xFFFFFFFF, "08x"),
}


def _register_optional_hash_extras() -> None:
    """Platforma / OpenSSL surumune gore bulunmayabilecek algoritmalari,
    varsa ekler; yoksa sessizce atlar (programi crashlatmaz)."""
    for name in ("ripemd160", "whirlpool", "sha512_224", "sha512_256", "md4"):
        try:
            hashlib.new(name, b"test")
        except Exception:
            continue
        HASH_ALGORITHMS[name] = (lambda n: (lambda data: hashlib.new(n, data).hexdigest()))(name)


_register_optional_hash_extras()


# --------------------------------------------------------------------------- #
# BASE ENCODING TURLERI (geri donusumlu, anahtar gerektirmez)
# --------------------------------------------------------------------------- #

BASE_ENCODINGS: dict[str, tuple[Callable[[bytes], bytes], Callable[[bytes], bytes]]] = {
    "base16": (base64.b16encode, base64.b16decode),
    "base32": (base64.b32encode, base64.b32decode),
    "base64": (base64.b64encode, base64.b64decode),
    "base64url": (base64.urlsafe_b64encode, base64.urlsafe_b64decode),
    "base85": (base64.b85encode, base64.b85decode),
    "ascii85": (base64.a85encode, base64.a85decode),
    "hex": (lambda b: b.hex().encode("ascii"), lambda b: bytes.fromhex(b.decode("ascii"))),
}


# --------------------------------------------------------------------------- #
# BASIT SIFRELER (geri donusumlu, anahtar GEREKTIRMEZ, kendi kendinin tersi)
# --------------------------------------------------------------------------- #

def rot47(text: str) -> str:
    result = []
    for ch in text:
        code = ord(ch)
        if 33 <= code <= 126:
            result.append(chr(33 + ((code + 14) % 94)))
        else:
            result.append(ch)
    return "".join(result)


SIMPLE_CIPHERS: dict[str, tuple[Callable[[str], str], Callable[[str], str]]] = {
    "rot13": (lambda t: codecs.encode(t, "rot_13"), lambda t: codecs.decode(t, "rot_13")),
    "rot47": (rot47, rot47),
}


# --------------------------------------------------------------------------- #
# ANAHTARLI SIFRELER
#
# ONEMLI FARK: Buradaki "anahtar" (key), hash'lerdeki "salt" ile KARISTIRILMAMALI.
#   - Salt: rastgele uretilir, GIZLI DEGILDIR, hash ile birlikte acikca saklanir,
#     amaci ayni metnin farkli hash'ler uretmesini saglamaktir (bkz. yukarisi).
#   - Anahtar (key): sifreleyen kisi tarafindan secilir/hatirlanir, cozmek
#     icin ZORUNLUDUR ve GIZLI TUTULMALIDIR - hash salt'inin aksine paylasilmaz.
# --------------------------------------------------------------------------- #

def caesar_encode(text: str, shift: int) -> str:
    shift %= 26
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return "".join(result)


def caesar_decode(text: str, shift: int) -> str:
    return caesar_encode(text, -shift)


def _validate_alpha_key(key: str, cipher_name: str) -> str:
    if not key or not key.isalpha():
        raise ValueError(f"{cipher_name} anahtari sadece harflerden olusmalidir.")
    return key.lower()


def vigenere_encode(text: str, key: str) -> str:
    key = _validate_alpha_key(key, "Vigenere")
    result, ki = [], 0
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            shift = ord(key[ki % len(key)]) - ord("a")
            result.append(chr((ord(ch) - base + shift) % 26 + base))
            ki += 1
        else:
            result.append(ch)
    return "".join(result)


def vigenere_decode(text: str, key: str) -> str:
    key = _validate_alpha_key(key, "Vigenere")
    result, ki = [], 0
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            shift = ord(key[ki % len(key)]) - ord("a")
            result.append(chr((ord(ch) - base - shift) % 26 + base))
            ki += 1
        else:
            result.append(ch)
    return "".join(result)


def xor_encode(text: str, key: str) -> str:
    if not key:
        raise ValueError("XOR anahtari bos olamaz.")
    data = text.encode("utf-8")
    key_bytes = key.encode("utf-8")
    out = bytes(b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(data))
    return out.hex()


def xor_decode(hex_text: str, key: str) -> str:
    if not key:
        raise ValueError("XOR anahtari bos olamaz.")
    data = bytes.fromhex(hex_text)
    key_bytes = key.encode("utf-8")
    out = bytes(b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(data))
    return out.decode("utf-8", errors="replace")


KEYED_CIPHERS = {
    "caesar": {
        "encode": lambda text, key: caesar_encode(text, int(key)),
        "decode": lambda text, key: caesar_decode(text, int(key)),
        "key_prompt": "Kaydirma miktari (ornegin: 3)",
    },
    "vigenere": {
        "encode": vigenere_encode,
        "decode": vigenere_decode,
        "key_prompt": "Anahtar kelime (sadece harf)",
    },
    "xor": {
        "encode": xor_encode,
        "decode": xor_decode,
        "key_prompt": "Anahtar metin",
    },
}

SUPPORTED_TYPES = list(HASH_ALGORITHMS) + list(BASE_ENCODINGS) + list(SIMPLE_CIPHERS) + list(KEYED_CIPHERS)


# --------------------------------------------------------------------------- #
# Yardimci fonksiyonlar
# --------------------------------------------------------------------------- #

def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def colorize(text: str, fore: str = "", style: str = "") -> str:
    if not COLOR_ENABLED:
        return text
    return f"{fore}{style}{text}{Style.RESET_ALL}"


def print_banner() -> None:
    print(colorize(BANNER, Fore.CYAN))
    print(colorize(f"  {APP_NAME}  -  by {APP_AUTHOR}          v{APP_VERSION}", Fore.CYAN))
    print()


def print_supported_types() -> None:
    print(colorize("Hash turleri:", Fore.CYAN), ", ".join(HASH_ALGORITHMS))
    print(colorize("Encoding turleri:", Fore.CYAN), ", ".join(BASE_ENCODINGS))
    print(colorize("Basit sifreler (anahtarsiz):", Fore.CYAN), ", ".join(SIMPLE_CIPHERS))
    print(colorize("Anahtarli sifreler:", Fore.CYAN), ", ".join(KEYED_CIPHERS))


def ask_yes_no(prompt: str, default: bool = True) -> bool:
    suffix = "(Y/n)" if default else "(y/N)"
    answer = input(f"{prompt} {suffix}: ").strip().lower()
    if not answer:
        return default
    return answer in ("y", "yes", "e", "evet")


# --------------------------------------------------------------------------- #
# SALT (sadece hash'ler ve encoding'ler icin - opsiyonel)
# --------------------------------------------------------------------------- #

def generate_salt(num_bytes: int = DEFAULT_SALT_BYTES) -> str:
    return secrets.token_hex(num_bytes)


def get_salt_for_encoding() -> str | None:
    if not ask_yes_no("Salt kullanilsin mi?", default=True):
        return None

    if ask_yes_no("Otomatik, guvenli, rastgele salt uretilsin mi?", default=True):
        salt = generate_salt()
        print(colorize(f"[i] Uretilen salt: {salt}", Fore.YELLOW))
        print(colorize(
            "[i] Bu degeri hash ile BIRLIKTE saklamalisin; dogrulama/kirma "
            "islemleri icin gereklidir. Salt gizli tutulmak zorunda degildir.",
            Fore.YELLOW,
        ))
        return salt

    salt = input("Salt degerini gir: ").strip()
    print(colorize(
        "[!] Uyari: Elle secilen / tahmin edilebilir saltlar rastgele "
        "uretilen saltlara gore daha zayif koruma saglar.",
        Fore.RED,
    ))
    return salt


def apply_salt(text: str, salt: str | None) -> str:
    return text if salt is None else text + salt


# --------------------------------------------------------------------------- #
# Encode / Decode / Crack
# --------------------------------------------------------------------------- #

def encode_text(algorithm: str, text: str, salt: str | None) -> str:
    salted_text = apply_salt(text, salt)

    if algorithm in HASH_ALGORITHMS:
        return HASH_ALGORITHMS[algorithm](salted_text.encode("utf-8"))

    if algorithm in BASE_ENCODINGS:
        encode_fn, _ = BASE_ENCODINGS[algorithm]
        return encode_fn(salted_text.encode("utf-8")).decode("ascii")

    if algorithm in SIMPLE_CIPHERS:
        encode_fn, _ = SIMPLE_CIPHERS[algorithm]
        return encode_fn(salted_text)

    raise ValueError(f"Desteklenmeyen tur: {algorithm}")


def decode_text(algorithm: str, text: str) -> str:
    """Sadece anahtarsiz, geri donusumlu turler icin (encodings + basit
    sifreler). Hash'ler tek yonludur (bkz. crack_with_wordlist), anahtarli
    sifreler ise ayri bir akista (anahtar sorularak) cozulur."""
    if algorithm in BASE_ENCODINGS:
        _, decode_fn = BASE_ENCODINGS[algorithm]
        return decode_fn(text.encode("ascii")).decode("utf-8")

    if algorithm in SIMPLE_CIPHERS:
        _, decode_fn = SIMPLE_CIPHERS[algorithm]
        return decode_fn(text)

    raise ValueError(f"'{algorithm}' bu fonksiyonla cozulemez.")


def crack_with_wordlist(
    algorithm: str,
    target_hash: str,
    wordlist_path: str,
    salt: str | None,
) -> str | None:
    hasher = HASH_ALGORITHMS[algorithm]
    path = Path(wordlist_path)
    if not path.is_file():
        raise FileNotFoundError(f"Wordlist bulunamadi: {wordlist_path}")

    with path.open("r", encoding="utf-8", errors="ignore") as handle:
        words = handle.readlines()
    total = len(words)

    for index, raw_word in enumerate(words, start=1):
        word = raw_word.strip()
        if not word:
            continue

        candidate = apply_salt(word, salt)
        candidate_hash = hasher(candidate.encode("utf-8"))

        if index % 200 == 0 or index == total:
            print(f"\r[-] Deneniyor: {index}/{total}", end="", flush=True)

        if candidate_hash == target_hash:
            print()
            return word

    print()
    return None


def print_result(title: str, rows: dict) -> None:
    print(colorize(f"---------- {title} ----------", Fore.CYAN))
    for label, value in rows.items():
        print(f"[-] {label}: {value}")


# --------------------------------------------------------------------------- #
# Menuler
# --------------------------------------------------------------------------- #

def run_encode_menu() -> None:
    print_supported_types()
    algorithm = input("Kodlama/Hash/Sifre turu: ").strip().lower()
    if algorithm not in SUPPORTED_TYPES:
        print(colorize(f"[!] Gecersiz tur: {algorithm}", Fore.RED))
        return

    if algorithm in KEYED_CIPHERS:
        key = input(f"{KEYED_CIPHERS[algorithm]['key_prompt']}: ").strip()
        text = input("Metin: ")
        try:
            result = KEYED_CIPHERS[algorithm]["encode"](text, key)
        except Exception as exc:
            print(colorize(f"[!] Hata: {exc}", Fore.RED))
            return
        print_result("Sifreleme Sonucu", {
            "Metin": text,
            "Tur": algorithm,
            "Anahtar": key,
            "Sonuc": result,
        })
        print(colorize(
            "[i] Bu anahtari GIZLI TUT ve hatirla - salt'in aksine otomatik "
            "uretilip yaninda saklanmaz; cozmek icin sadece bu anahtar yeterlidir.",
            Fore.YELLOW,
        ))
        sleep(1)
        return

    salt = None
    if algorithm in SIMPLE_CIPHERS:
        print(colorize(f"[i] Not: {algorithm} bir sifreleme degil, basit bir karakter kaydirmadir; salt kriptografik bir fayda saglamaz.", Fore.YELLOW))
        if ask_yes_no("Yine de salt eklensin mi?", default=False):
            salt = get_salt_for_encoding()
    else:
        salt = get_salt_for_encoding()

    text = input("Metin: ")
    result = encode_text(algorithm, text, salt)

    print_result("Kodlama Sonucu", {
        "Metin": text,
        "Tur": algorithm,
        "Salt": salt if salt else "Kullanilmadi",
        "Sonuc": result,
    })
    sleep(1)


def run_decode_menu() -> None:
    print_supported_types()
    algorithm = input("Kodlama/Hash/Sifre turu: ").strip().lower()
    if algorithm not in SUPPORTED_TYPES:
        print(colorize(f"[!] Gecersiz tur: {algorithm}", Fore.RED))
        return

    if algorithm in KEYED_CIPHERS:
        if algorithm == "caesar" and ask_yes_no("Anahtari (kaydirma miktarini) bilmiyorsan tum ihtimalleri dene?", default=False):
            text = input("Kodlanmis metin: ")
            print_result("Olasi Tum Kaydirmalar (0-25)", {str(s): caesar_decode(text, s) for s in range(26)})
            return

        key = input(f"{KEYED_CIPHERS[algorithm]['key_prompt']}: ").strip()
        text = input("Kodlanmis metin: ")
        try:
            result = KEYED_CIPHERS[algorithm]["decode"](text, key)
        except Exception as exc:
            print(colorize(f"[!] Hata: {exc}", Fore.RED))
            return
        print_result("Cozme Sonucu", {"Girdi": text, "Tur": algorithm, "Anahtar": key, "Sonuc": result})
        return

    if algorithm in BASE_ENCODINGS or algorithm in SIMPLE_CIPHERS:
        text = input("Kodlanmis metin: ")
        try:
            result = decode_text(algorithm, text)
        except Exception as exc:
            print(colorize(f"[!] Cozme hatasi: {exc}", Fore.RED))
            return
        print_result("Cozme Sonucu", {"Girdi": text, "Tur": algorithm, "Sonuc": result})
        return

    # Hash turleri tek yonludur; sadece wordlist ile eslesme denenebilir.
    print(colorize("[i] Hash algoritmalari tek yonludur, dogrudan 'cozulemezler'.", Fore.YELLOW))
    print(colorize("[i] Bunun yerine bir wordlist kullanilarak eslesme aranacak.", Fore.YELLOW))

    target_hash = input("Hedef hash: ").strip()
    wordlist_path = input("Wordlist dosya yolu: ").strip()

    salt = None
    if ask_yes_no("Bu hash bir salt ile mi olusturulmustu?", default=False):
        salt = input("Salt degerini gir (hash olusturulurken kullanilan, saklanmis deger): ").strip()

    try:
        found = crack_with_wordlist(algorithm, target_hash, wordlist_path, salt)
    except FileNotFoundError as exc:
        print(colorize(f"[!] {exc}", Fore.RED))
        return

    if found is not None:
        print_result("Hash Kirildi!", {
            "Hash Turu": algorithm,
            "Sifre": found,
            "Salt": salt or "Kullanilmadi",
        })
    else:
        print(colorize("[!] Wordlist icinde eslesme bulunamadi.", Fore.RED))
    sleep(1)


def main() -> None:
    clear_screen()
    print_banner()
    mode = input("Encoding mi Decoding mi? (E/D): ").strip().lower()

    if mode == "e":
        run_encode_menu()
    elif mode == "d":
        run_decode_menu()
    else:
        print(colorize("[!] Gecersiz secim.", Fore.RED))
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Islem iptal edildi.")
        sys.exit(0)
