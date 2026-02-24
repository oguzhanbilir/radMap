# `geiger iha.sb3` – PictoBlox Proje Rehberi (Blok Açıklamaları)

Bu doküman, **`geiger iha.sb3`** PictoBlox dosyasının içinde bulunan blokların ne yaptığını açıklar ve RadMap projesindeki hedef akışa nasıl genişletilebileceğini özetler.

## 1) Bu `.sb3` dosyası şu an ne yapıyor?

Bu dosya, **Arduino Nano** üzerinde **D2 dijital girişini okuyup** (buton/sinyal), giriş durumuna göre **D13 dahili LED’i** yakıp söndürür.

> Not: Bu dosya, RadMap’in “CPM/µSv/h hesaplama + OLED + kayıt + 3B işleme” akışının tamamını içermez; daha çok **pin okuma ve kontrol testi** gibi çalışır.

## 2) Proje yapısı (içerik özeti)

Dosyanın `project.json` içeriğine göre:

- **Target sayısı**: 2
  - **Stage (Sahne)**: Blok yok (boş). 1 adet varsayılan değişken var.
  - **Sprite**: `Tobi`
- **Extensions (Eklentiler)**: `arduinoUno` (Arduino blokları)
- **Board seçimi (metadata)**: `Arduino Nano` (PictoBlox ayarlarında seçili)
- **Proje modu**: `UPLOAD` (kartı programlama/bağlantı modu)

## 3) Blok akışı (blok-blok)

`Tobi` sprite’ında tek bir akış (script) var:

### A) Arduino başlatma
- **Blok**: `arduinoUnoStartUp`
- **Amaç**: Arduino ile bağlantıyı/başlatmayı gerçekleştirir (PictoBlox tarafında Arduino eklentisini “ready” hale getirir).

### B) Sürekli kontrol döngüsü
- **Blok**: `forever`
- **Amaç**: Aşağıdaki kontrolün sürekli çalışmasını sağlar.

### C) Koşul: D2 pinini oku
- **Blok**: `if else`
  - **Koşul bloğu**: `digitalRead PIN 2`
- **Amaç**: D2 pinindeki dijital değeri (0/1) kontrol eder.

### D) Çıkış: D13 LED’i kontrol et
- **Eğer D2 = TRUE**:
  - **Blok**: `digitalWrite PIN 13 → true`
  - **Sonuç**: LED yanar.

- **Değilse (D2 = FALSE)**:
  - **Blok**: `digitalWrite PIN 13 → false`
  - **Sonuç**: LED söner.

## 4) Donanım bağlantısı (bu dosyaya göre)

Bu proje “buton testi” mantığında olduğu için tipik bağlantı:

- **Giriş**: D2
- **Çıkış**: D13 (Arduino’nun dahili LED’i)

Buton kullanıyorsanız:
- Butonun bir ucu **D2**, diğer ucu **GND** (veya 5V) olacak şekilde bağlanır.
- (Gerekirse) pull‑up/pull‑down ihtiyacına göre direnç ya da Arduino’nun dahili pull‑up ayarları kullanılır.

## 5) RadMap için bu `.sb3` dosyası nasıl geliştirilir?

RadMap hedefi için bu dosyaya şu katmanlar eklenebilir:

- **Sayım (pulse counting)**:
  - Geiger TTL çıkışından gelen darbeler için **pulse sayacı** değişkeni
- **CPM hesaplama**:
  - 1 saniyelik sayımları toplayıp \( \text{CPM} = \text{pulse\_per\_sec} \times 60 \) veya sliding window
- **µSv/h dönüşümü**:
  - Örn. `uSv/h = CPM × 0.00812`
- **OLED gösterim**:
  - CPM ve µSv/h değerlerini OLED’e yazdırma
- **Tobi geri bildirimi**:
  - Tobi’nin “say” bloğu ile sesli/görsel uyarı
- **Kayıt / GPS / 3B**:
  - Veriyi SD’ye yazma (veya PC’ye aktarım)
  - GPS + yükseklik ile 3B görselleştirme (QGIS/KML)

Bu genişletilmiş akışın algoritma tarafı için repoda şu dosyalara bakabilirsiniz:

- `Codeavour_Adaptation/PictoBlox_Final_Code.py` (Arduino Nano + OLED + Tobi akışı örnek)
- `Codeavour_Adaptation/PictoBlox_Geiger_Logic.py` (sliding window + CPM/µSv/h mantığı)

## 6) Sık hata / kontrol listesi

- **Arduino bağlantısı**: Doğru COM port / doğru kart seçimi (Arduino Nano)
- **Pin numarası**: Geiger TTL çıkışı gerçekten D2’ye mi bağlı?
- **Ters okuma**: Pull‑up/pull‑down nedeniyle 1/0 ters olabilir (gerekirse koşulu tersleyin)

