# adventurous_girl
# Adventurous Girl - 2D Koşu ve Animasyon Oyunu

Bu proje, Python ve Pygame kullanılarak geliştirilmiş basit bir 2D koşu oyunudur. Karakter animasyonları, hareketli arka plan, rastgele engeller ve skor sistemi içerir. Skor arttıkça ev ekranı değişir, oyun sırasında duraklatma ve menü özellikleri mevcuttur.

---

## Özellikler

- Animasyonlu karakter hareketleri (koşma, zıplama, saldırı)
- Sonsuz kayan arka plan
- Rastgele çıkan engeller
- Çift zıplama mekaniği
- Skor ve yüksek skor takibi
- Oyun sırasında duraklatma (pause) özelliği
- Skor arttıkça değişen ev ekranı (oda durumu)
- Menü, oyun sonu ve duraklatma ekranları

---

## Kurulum ve Çalıştırma

1. Python 3.x yüklü olmalıdır.
2. Gerekli kütüphaneleri yükleyin:

    ```bash
    pip install pygame
    ```

3. Projeyi klonlayın veya indirin.
4. Terminalden proje klasörüne gidin.
5. Oyunu çalıştırmak için:

    ```bash
    python main.py
    ```

---

## Dosya Yapısı

- `main.py`: Oyun döngüsü ve ana yönetim.
- `character_animation.py`: Karakter animasyonlarının yüklenmesi ve yönetimi.
- `player.py`: Karakter hareketi ve durum yönetimi.
- `menu.py`: Menü ve oyun durumları (oyun başlatma, duraklatma, oyun sonu).
- `house.py`: Ev ekranı yönetimi ve oda durumlarının gösterimi.
- `images/`: Oyun içi görseller (arka plan, karakter sprite'ları, engeller, ev odası resimleri).

---

## Özelleştirme

- Karakter animasyonlarını `images/character-animations` klasörüne yeni PNG dosyaları ekleyerek değiştirebilirsiniz.
- Engelleri `images/obstacles` klasörüne yeni görseller ekleyerek çeşitlendirebilirsiniz.
- Ev odası görsellerini `images/oda_esya/` klasöründe değiştirip artırabilirsiniz.
- Menüdeki metinleri `menu.py` dosyasında düzenleyebilirsiniz.

---

## Gelecek Planları

- Yeni engel türleri ve düşmanlar eklemek.
- Ses efektleri ve müzik desteği.
- Daha zengin ev dekorasyon ve kişiselleştirme sistemi.
- Çoklu dil desteği.

---

> **Not:** Bu proje öğrenme ve eğlenme amacıyla hazırlanmıştır.

