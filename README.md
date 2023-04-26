# HashBox

![License: GPL v3](https://img.shields.io/github/license/Kerxunos/HashBox)
![Coding](https://img.shields.io/github/languages/top/Kerxunos/HashBox)
![Size](https://img.shields.io/github/languages/code-size/Kerxunos/HashBox)
![Codecs](https://img.shields.io/pypi/v/codecs)
![Hashlib](https://img.shields.io/pypi/v/hashlib)
![Colorama](https://img.shields.io/pypi/v/colorama)
![Observatory_Grade](https://img.shields.io/mozilla-observatory/grade/github.com?publish)
![commit_acitivity](https://img.shields.io/github/commit-activity/w/Kerxunos/HashBox)
![pyapi_format](https://img.shields.io/pypi/format/colorama)
![pyapi_format](https://img.shields.io/pypi/format/hashlib)
![pyapi_format](https://img.shields.io/pypi/format/codecs)
HashBox
HashBox, Python dilinde yazılmış bir hash ve rot şifrelemesi encode/decode aracıdır. Bu araç, hashlib ve codecs gibi Python kütüphaneleri kullanarak hash ve rot şifrelemelerini encode etmenize veya brute force ile decode etmenize olanak tanır. Ayrıca, renkli bir çıktı sağlamak için colorama kütüphanesi de kullanılır.

Kullanım
HashBox'u kullanmak için öncelikle programı klonlayın:

bash
Copy code
git clone https://github.com/kullanıcıadı/HashBox.git
Gerekli kütüphaneleri yüklemek için aşağıdaki komutu çalıştırın:

bash
Copy code
pip install -r requirements.txt
HashBox'u kullanmak için, aşağıdaki komutları kullanabilirsiniz:

bash
Copy code
python hashbox.py -h    # Yardım mesajını görüntüleme
python hashbox.py encode <string> <algorithm>    # Hash veya rot encode
python hashbox.py decode <hash/rot> <algorithm>  # Hash veya rot brute force ile decode
algorithm parametresi olarak md5, sha1, sha256, sha512 gibi desteklenen algoritmaları kullanabilirsiniz.

Örnek kullanımlar:

bash
Copy code
python hashbox.py encode "hello world" md5
python hashbox.py decode 5eb63bbbe01eeed093cb22bb8f5acdc3 md5
Ekran Görüntüleri
HashBox Ekran Görüntüsü 1

HashBox Ekran Görüntüsü 2

Lisans
Bu proje GPL-3.0 lisansı altında dağıtılmaktadır. Daha fazla bilgi için LICENSE dosyasını inceleyin.

Katkıda Bulunma
Bu projeye katkıda bulunmak isterseniz, lütfen bir issue açarak veya pull request göndererek bize ulaşın. Kabul edilebilir davranış kuralları ve katkıda bulunma rehberi için CONTRIBUTING.md dosyasına bakın.
