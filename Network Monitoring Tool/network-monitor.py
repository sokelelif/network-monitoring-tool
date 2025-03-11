import keyboard
from scapy.all import sniff
import threading

def paket_yakalama(paket):
    paket_info = (paket.summary()) 
    print(paket_info)
    with open ("paketler.txt", "a") as file:
        file.write(paket_info + "\n")

stop_event = threading.Event()  # Durdurma için Event oluşturma

def durdurma_kontrol(paket):
    return stop_event.is_set()  # stop_event set edildiyse paket yakalamayı durdur

def kullanici_giris():
    while True:
        if keyboard.is_pressed('enter'):  # 'Enter' tuşuna basıldığını kontrol et
            stop_event.set()  # Giriş alındığında program duracak
            break

# Paket yakalamayı ayrı bir thread'de başlatıyoruz
def paket_yakalama_baslat():
    sniff(prn=paket_yakalama, filter="tcp or udp", stop_filter=durdurma_kontrol)

# Kullanıcı girişini ayrı bir thread'de başlatıyoruz
giris_thread = threading.Thread(target=kullanici_giris, daemon=True)
giris_thread.start()

# Paket yakalamayı ayrı bir thread'de başlatıyoruz
paket_thread = threading.Thread(target=paket_yakalama_baslat)
paket_thread.start()

# Thread'lerin bitmesini bekliyoruz
paket_thread.join()