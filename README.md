# RadMap – Drone Tabanlı 3B Radyasyon Haritalama Sistemi

Codeavour 7.0 Track 1 – Proje web sitesi. Rapor verilerine dayalı kapsamlı sunum.

## Sayfalar

| Sayfa | İçerik |
|-------|--------|
| **Ana Sayfa** | Proje özeti, drone tamamlanmış hali, ölçüm özeti, 3B haritalandırma galerisi |
| **Malzemeler** | Arduino Nano, PCE-RAM10 Geiger-Müller, OLED, GPS, SD kart, muhafaza kutusu, DJI Avata 2 |
| **Proje Süreci** | 7 aşamalı gelişim süreci, proje görüntüleri |
| **Ölçüm Sonuçları** | Arka plan, açık alan, kapalı alan tabloları, mesafe grafikleri, Nükleer Tıp doğrulaması |
| **Takım** | Neda, Günseli, Ekin, danışman Oğuzhan Bilir |
| **Proje Çıktıları** | Teknik çıktılar, hedeflenen katılımlar, SDG |

## Görsel Klasör Yapısı

```
images/
├── components/     # nano.jpeg, geiger.jpg, oled.jpg, gps.jpg, sd-kart.jpg, muhafaza-kutusu.jpg
├── drone/          # drone-tamamlanmis.jpg, drone-ust-gorunum.jpg, drone-yan-gorunum.jpg, drone-acik-alan.jpg, dji-avata-2.jpg
├── 3b-harita/      # google-earth-olcum-noktalari.jpg, drone-rota-gorunum.jpg, kapali-alan-grafik.jpg, mesafe-cpm-grafik.jpg, mesafe-usvh-grafik.jpg, arka-plan-dagilim.jpg
└── proje/          # devre-kurulum.jpg, devre-semasi.jpg, drone-montaj.jpg, saha-olcum.jpg, bodrum-olcum.jpg, nukleer-tip.jpg, pictoblox.jpg
```

Her klasörde README.txt ile dosya adları listelenmiştir. Görselleri hazırladıkça ilgili klasöre ekleyin.

## Yayınlama

- **Yerel:** `index.html` dosyasına çift tıklayın
- **GitHub Pages:** Repo → Settings → Pages → main branch
- **Google Sites:** İçeriği kopyalayıp yapıştırın

## Özelleştirme

- **Renkler:** `style.css` → `:root` değişkenleri
- **İçerik:** HTML dosyalarındaki metinler
