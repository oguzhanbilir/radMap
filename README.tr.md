Türkçe | [English](README.md)

[![Site check](https://github.com/oguzhanbilir/radMap/actions/workflows/check.yml/badge.svg)](https://github.com/oguzhanbilir/radMap/actions/workflows/check.yml)

# RadMap: drone ile 3B radyasyon haritalama

Drone'a takılan bir Geiger-Müller sayacı, radyasyon ölçümlerini GPS koordinatlarıyla birlikte kaydeder. Ölçümler daha sonra bölgenin 3B haritasına dönüştürülür. Bu depo, proje raporundan hazırlanan proje web sitesidir.

**Codeavour 7.0** · Türkiye 3.lüğü, SANKODE Intelligence takımı (Şubat 2026) · **Samsung Solve for Tomorrow 2026** · Türkiye finalisti, GeigerTim takımı (final 30 Kasım 2026) · **TÜBİTAK 2204-A** · Adana bölge sergisine davet

Site: https://oguzhanbilir.github.io/radMap/

<p align="center">
  <img src="images/drone/dji%20mavic%203%20pro%20ile%20bitmi%C5%9F%20devrenin%20u%C3%A7u%C5%9F%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%201.JPG" width="420" alt="Ölçüm devresi takılı drone uçuşta" />
  <img src="images/drone/dji%20mavic%203%20pro%20modeli%20ile%20devre%20haz%C4%B1r%20hali.JPG" width="420" alt="Drone'a takılmış ölçüm devresi" />
</p>

## Nasıl çalışır

- Arduino Nano, Geiger-Müller tüpünü okur (referans cihaz olarak PCE-RAM10); OLED ekran, GPS modülü ve microSD kayıt içerir
- Devre bir DJI drone'a takılır ve ölçüm noktalarından oluşan bir ızgara üzerinde uçurulur
- Kaydedilen CPM ve µSv/h değerleri Python ile işlenir ve 3B harita olarak görselleştirilir
- Ölçümler iç mekânda, açık alanda ve bir nükleer tıp referans ölçümüyle karşılaştırılarak doğrulandı

## Site sayfaları

| Sayfa | İçerik |
|-------|--------|
| `index.html` | Genel bakış, tamamlanmış drone, ölçüm özeti, 3B harita galerisi |
| `malzemeler.html` | Donanım listesi |
| `proje.html` | 7 aşamada geliştirme süreci |
| `olcum-sonuclari.html` | Arka plan, açık alan ve iç mekân ölçüm tabloları, mesafe grafikleri |
| `rehberler.html` | Adım adım rehberler: Arduino devresi, PictoBlox, Python ile haritalama, 3B haritalama |
| `takim.html` | Ekip |

## Yerelde çalıştırma

`index.html` dosyasını tarayıcıda açın; derleme adımı yok. Renkler `style.css` içindeki `:root` değişkenlerindedir.

## Emeği geçenler

Öğrenci araştırma projesi. Danışman ve web sitesi geliştiricisi: Oğuzhan Bilir.
