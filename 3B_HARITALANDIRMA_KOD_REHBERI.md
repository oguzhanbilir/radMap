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

## 3) Ölçüm → 3B haritalandırma akışı (özet)

1. **Arduino Nano + Geiger + GPS** ile ölçüm al
2. Veriyi **SD karta CSV** olarak kaydet
3. Veriyi bilgisayara alıp **temizle/dönüştür**
4. **Google Earth** üzerinde KML ile **3B görselleştir**

## 4) Sık sorunlar

- **Noktalar yanlış yerde**: X=Longitude, Y=Latitude olduğuna emin olun.
- **Her şey aynı renkte**: VMIN/VMAX aralığı verinize uymuyordur; aralığı ayarlayın.
- **Hiç görünmüyor**: Zoom/tilt yapın, grid boyutunu büyütün.

