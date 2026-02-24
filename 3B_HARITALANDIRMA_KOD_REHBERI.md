# RadMap – 3B Haritalandırma Kod Rehberi

Bu doküman, RadMap projesinde **ölçüm sonrası** elde edilen verilerin **3B haritalandırmaya** dönüştürülmesi için kullanılan dosyaların mantığını ve kullanım adımlarını özetler.

> Bu repo bir “web sitesi repo”su olduğu için 3B haritalandırma kodları proje klasörünüzde ayrıca bulunur. Dokümandaki dosya yollarını kendi bilgisayarınızdaki proje klasör yapısına göre kullanın.

## 1) Gerekli veri alanları (minimum)

3B haritalandırma için her ölçüm noktası şu bilgileri içermelidir:

- **Enlem / Boylam**: `Latitude`, `Longitude`
- **Yükseklik**: `Altitude` (metre)
- **Radyasyon değeri**: `Radiation_Value` (µSv/h)
- (Opsiyonel) **Zaman**: `Time` (`YYYY-MM-DDTHH:MM:SS`)
- (Opsiyonel) **Hız**: `Speed` (m/s)

Bu formatın örneği proje klasörünüzdeki `qgis_data.csv` dosyasında bulunur.

## 2) Google Earth ile 3B görselleştirme (KML)

Bu projede 3B haritalandırmayı **Google Earth üzerinde KML** ile yaptık. Bu yüzden aşağıdaki akış Google Earth odaklıdır.

Google Earth için veriyi KML formatına dönüştüren bir script kullanılır.

### Bu rehberde referans alınan ana dosyalar

- **Girdi veri**: `drone_data_paper.json`
- **KML üretici script**: `generate_kml.py`
- **Çıktı**: `drone_radiation_visualization.kml` (Google Earth’te açılır)

### KML üretimi genel mantık
- Her ölçüm noktası için küçük bir **poligon/katman** üretilir.
- Radyasyon değerine göre **renk** (mavi→yeşil→sarı→kırmızı) atanır.
- Yükseklik (Z) ile birlikte katmanlar “3B” görünür.

### Ayarlanabilir parametreler
KML üretim scriptlerinde genelde şu ayarlar vardır:

- **VMIN / VMAX**: Renk ölçeğinin alt/üst sınırı  
  (Küçük farkları görmek için dar aralık seçilebilir.)
- **Grid boyutu**: Noktaların çizimde kapladığı alan  
  (Büyürse daha “dolgun”, küçülürse daha “noktasal” görünür.)
- **Altitude mode**: `relativeToGround` gibi ayarlar

### Google Earth’te açma
- Google Earth Pro → **File → Open** → üretilen `.kml`
- 3B etki için kamerayı **tilt** yapın ve yakınlaştırın.

## 3) `generate_kml.py` kod rehberi (parça parça)

Aşağıdaki parçalar `KAYNAK KODLAR/drone_3b_haritalama/generate_kml.py` dosyasından alınmıştır ve script’in mantığını açıklar.

### 3.1) Veriyi yükleme (JSON → DataFrame)

Script, `drone_data_paper.json` içindeki listeyi okur ve `pandas` ile tabloya çevirir:

```python
with open('drone_data_paper.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
```

- **Ne işe yarıyor?** JSON’daki her ölçüm noktası bir satır olacak şekilde işlenir.
- **Bu dosyada neler olmalı?** En az şu alanlar: `Enlem (Lat)`, `Boylam (Lon)`, `Yükseklik (m)`, `Doz Hızı (μSv/h)`

### 3.2) Kamera merkezini hesaplama (LookAt)

Google Earth açıldığında sahnenin ortasına yakın bakması için enlem-boylam ortalaması alınır:

```python
center_lat = df['Enlem (Lat)'].mean()
center_lon = df['Boylam (Lon)'].mean()
```

- **Ne işe yarıyor?** KML içindeki `<LookAt>` bölümüne yazılıp başlangıç görünümünü iyileştirir.

### 3.3) Görselleştirme ölçeği (VMIN/VMAX) ve grid boyutu (hw)

Bu kısım, renklerin hangi aralıkta dağıtılacağını ve her noktanın sahnede ne kadar alan kaplayacağını belirler:

```python
VMIN = 0.090
VMAX = 0.130

hw = 0.000013
```

- **VMIN/VMAX**: Renk skalasının alt/üst sınırı. Aralık dar olursa küçük değişimler daha görünür olur.
- **hw**: Bir noktanın etrafında çizilecek poligonun “yarı genişliği”. Çok küçükse görünmeyebilir, çok büyükse üst üste binebilir.

### 3.4) Satır satır KML üretme (asıl döngü)

Her ölçüm noktası için enlem, boylam, doz ve yükseklik alınır:

```python
for _, row in df.iterrows():
    lat = row['Enlem (Lat)']
    lon = row['Boylam (Lon)']
    rad = row['Doz Hızı (μSv/h)']
    real_altitude = row['Yükseklik (m)']
```

- **Ne işe yarıyor?** KML’de her satır için bir `<Placemark>` oluşturulacak.

### 3.5) Radyasyonu “sıkıştırma” (clamp) ve normalize etme

Renk basamaklarını düzgün dağıtmak için değer önce aralığa sıkıştırılır, sonra 0–1 aralığına normalize edilir:

```python
chart_val = max(VMIN, min(VMAX, rad))
norm = (chart_val - VMIN) / (VMAX - VMIN)
```

- **Ne işe yarıyor?** Çok düşük/yüksek uç değerler grafiği “boğmasın” diye.

### 3.6) Renk haritası (basamaklı)

`norm` değerine göre 5 basamaklı renk seçimi yapılır:

```python
if norm < 0.2:
    red, green, blue = 0, 0, 255
elif norm < 0.4:
    red, green, blue = 0, 255, 255
elif norm < 0.6:
    red, green, blue = 0, 255, 0
elif norm < 0.8:
    red, green, blue = 255, 255, 0
else:
    red, green, blue = 255, 0, 0
```

- **Ne işe yarıyor?** Mavi (düşük) → Kırmızı (yüksek) görsel ayrım.

### 3.7) Poligon koordinatları (küçük bir kare yüzey)

Her nokta için küçük bir kare poligon çizilir (yükseklik = `real_altitude`):

```python
c1 = f"{lon+hw},{lat+hw},{real_altitude}"
c2 = f"{lon-hw},{lat+hw},{real_altitude}"
c3 = f"{lon-hw},{lat-hw},{real_altitude}"
c4 = f"{lon+hw},{lat-hw},{real_altitude}"
coords_str = f"{c1} {c2} {c3} {c4} {c1}"
```

- **Ne işe yarıyor?** Noktayı “3B katman” gibi göstermek için alan (surface) oluşturur.

### 3.8) Placemark yazma (KML çıktısı)

Bu bölüm, `<Placemark>` içini dosyaya yazar:

```python
f.write(f"""
  <Placemark>
    <description><![CDATA[
      <b>Radiation Layer</b><br>
      Alt: {real_altitude} m<br>
      Doz: {rad:.4f} uSv/h<br>
    ]]></description>
    <Style><PolyStyle><color>{color_hex}</color><outline>0</outline></PolyStyle></Style>
    <Polygon>
      <altitudeMode>relativeToGround</altitudeMode>
      <outerBoundaryIs><LinearRing><coordinates>{coords_str}</coordinates></LinearRing></outerBoundaryIs>
    </Polygon>
  </Placemark>
""")
```

- **Ne işe yarıyor?** Her noktanın 3B katmanı + açıklaması oluşturulur.

## 4) Bu kodda neler var / neler yok?

**Var:**
- JSON veriyi okuma
- Renk ölçekleme (clamp + normalize)
- Basamaklı renk haritası
- Google Earth için KML üretimi (katman/poligon)

**Yok (bilerek eklenmedi):**
- Otomatik “ısı haritası” interpolasyonu (grid doldurma)
- Gerçek zamanlı (uçuş sırasında) canlı haritalama
- Rota optimizasyonu / otonom uçuş planlama

## 3) Ölçüm → 3B haritalandırma akışı (özet)

1. **Arduino Nano + Geiger + GPS** ile ölçüm al
2. Veriyi **SD karta CSV** olarak kaydet
3. Veriyi bilgisayara alıp **temizle/dönüştür**
4. **Google Earth** üzerinde KML ile **3B görselleştir**

## 4) Sık sorunlar

- **Noktalar yanlış yerde**: X=Longitude, Y=Latitude olduğuna emin olun.
- **Her şey aynı renkte**: VMIN/VMAX aralığı verinize uymuyordur; aralığı ayarlayın.
- **Hiç görünmüyor**: Zoom/tilt yapın, grid boyutunu büyütün.

