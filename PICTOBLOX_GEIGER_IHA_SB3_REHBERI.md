# `geiger iha.sb3` – PictoBlox Proje Rehberi (Blok Açıklamaları)

Bu doküman, **`geiger iha.sb3`** PictoBlox dosyasının içinde bulunan blokların ne yaptığını açıklar ve RadMap projesindeki hedef akışa nasıl genişletilebileceğini özetler.

## 1) Bu `.sb3` dosyası şu an ne yapıyor?

Bu dosya, **Arduino Nano** üzerinde **D2 dijital girişini okuyup** (buton/sinyal), giriş durumuna göre **D13 dahili LED’i** yakıp söndürür.

> Not: Bu dosya, RadMap’in “CPM/µSv/h hesaplama + OLED + kayıt + 3B işleme” akışının tamamını içermez; daha çok **pin okuma ve kontrol testi** gibi çalışır.

## 1.1) Bu dosyada neler var / neler yok?

**Var:**
- Arduino başlatma + sürekli döngü
- D2 pin okuma (`digitalRead`)
- D13 LED kontrolü (`digitalWrite`)

**Yok:**
- Geiger darbelerini sayma (pulse counting)
- CPM / µSv/h hesaplama
- OLED ekran gösterimi
- GPS + SD kart kayıt
- Google Earth KML üretimi (bu kısım bilgisayarda Python ile yapılır)

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
  - GPS + yükseklik ile 3B görselleştirme (Google Earth KML)

Bu genişletilmiş akışın algoritma tarafı için repoda şu dosyalara bakabilirsiniz:

- `Codeavour_Adaptation/PictoBlox_Final_Code.py` (Arduino Nano + OLED + Tobi akışı örnek)
- `Codeavour_Adaptation/PictoBlox_Geiger_Logic.py` (sliding window + CPM/µSv/h mantığı)

## 6) Sık hata / kontrol listesi

- **Arduino bağlantısı**: Doğru COM port / doğru kart seçimi (Arduino Nano)
- **Pin numarası**: Geiger TTL çıkışı gerçekten D2’ye mi bağlı?
- **Ters okuma**: Pull‑up/pull‑down nedeniyle 1/0 ters olabilir (gerekirse koşulu tersleyin)

## Ek: PictoBlox Python kodu örneği (fonksiyonlar ne yapıyor?)

RadMap’in gerçek ölçüm algoritmasını “kod olarak” görmek isterseniz, proje klasörünüzdeki şu dosya iyi bir referanstır:

- `Codeavour_Adaptation/PictoBlox_Final_Code.py`

Aşağıda bu dosyadaki fonksiyonların özeti ve temel kod parçaları var.

### `read_geiger_pin()` – Geiger girişini okur

```python
def read_geiger_pin():
    if SIMULATION_MODE:
        import random
        return random.random() > 0.85
    if nano:
        raw = nano.readDigital(GEIGER_PIN) if hasattr(nano, 'readDigital') else nano.digitalRead(GEIGER_PIN)
        return raw in (True, 1) or str(raw).lower() == 'true'
    return False
```

- **Ne yapıyor?** Geiger TTL çıkışını dijital pin üzerinden okur.
- **SIMULATION_MODE** açıksa donanım olmadan test için rastgele değer üretir.

### `oled_yaz()` ve `oled_temizle()` – OLED’e yazdırır

```python
def oled_yaz(metin, x=0, y=0):
    if not oled_ok or nano is None:
        return
    nano.writeDisplay(str(metin), x, y)

def oled_temizle():
    if not oled_ok or nano is None:
        return
    nano.clearDisplay()
```

- **Ne yapıyor?** Ölçüm değerlerini OLED ekrana basar (başlatma başarılıysa).

### Ana döngü – 1 saniyede darbe sayar, CPM ve µSv/h hesaplar

```python
while True:
    start_sec = time.time()
    pulse_in_sec = 0

    while time.time() - start_sec < 1.0:
        val = read_geiger_pin()
        if val and not prev_state:
            pulse_in_sec += 1
            prev_state = True
        elif not val:
            prev_state = False

    total_counts -= counts[buffer_index]
    counts[buffer_index] = pulse_in_sec
    total_counts += pulse_in_sec
    buffer_index = (buffer_index + 1) % WINDOW_SIZE

    cpm = (total_counts / WINDOW_SIZE) * 60
    uSv = cpm * CONVERSION_FACTOR
```

- **Ne yapıyor?**
  - 1 saniye içinde gelen darbeleri sayar (`pulse_in_sec`)
  - Son \(N\) saniyeyi (WINDOW_SIZE) kullanarak kaydırmalı pencere ile daha stabil CPM üretir
  - CPM’yi dönüşüm katsayısı ile µSv/h’a çevirir

> Bu Python dosyası `.sb3`’nin kendisi değil; PictoBlox’un Python modunda aynı mantığı çalıştırmak için hazırlanmış bir örnektir.

