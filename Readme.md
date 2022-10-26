# QR greeter
## Nasıl kurulur
1. Bu deb dosyasını indirip yükleyelim. https://github.com/qr-greeter/qr-greeter/releases/download/current/etap-greeter_0.1.0_all.deb
2. Kurulum esnasında sizden gdm ve lightm arasından seçim yapmanızı soracaktır. lightdm seçip devam edin.
3. İşlem bittikten sonra tahtayı yeniden başlatın.

## Varsayılan qr kullanıcı parolası ayarlama
1. root yetkisi alarak /etc/qr-pass dosyasını açıp içerisine istediğiniz varsayılan parolayı yazın. (`sudo nano /etc/qr-pass`)
2. Dosya aitliğini roota verin. (`chown root /etc/qr-pass` ve `chmod 700 /etc/qr-pass`)
3. Sistemi yeniden başlatın. Bu işlem mevcut qr kullanıcılarını etkilemeyecektir. 
