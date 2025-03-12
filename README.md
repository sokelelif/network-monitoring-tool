# network-monitoring-tool

Bu proje ile Python kullanarak temel bir ağ izleme aracı geliştirmeyi amaçladım. Araç, ağdaki TCP ve UDP paketlerini yakalayıp analiz ederek kullanıcının ağ trafiğini izlemesine yardımcı olur.

## Özellikler
- Ağ trafiğini gerçek zamanlı olarak izlemeyi sağlar.
- TCP ve UDP paketlerini filtreleyerek gösterir.
- Yakalanan paketlerin özet bilgilerini ekrana yazdırır.

## Kullanım

Projeyi çalıştırmadan önce aşağıdaki kütüphanelerin yüklü olması gerekir:
- scapy
- keyboard
  
Kütüphaneleri yüklemek için şu komutu kullanabilirsiniz:

```
pip install scapy keyboard
```
Aşağıdaki komutu çalıştırarak aracı başlatabilirsiniz:

```
python network-monitor.py
```
Programı durdurmak için Enter tuşuna basın. Bu paket yakalamayı durduracak ve programı sonlandıracaktır.
