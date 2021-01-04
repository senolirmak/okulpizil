# Okul Zil ve Duyuru Sistemi
### 497_29 Raspberry and Python Grubu

Django Dökümanlardan:

**Tablo görünümü için**

https://django-tables2.readthedocs.io/en/latest/pages/tutorial.html

**Form için**

https://docs.djangoproject.com/en/3.1/ref/forms/

_**Tasarım Raporu:**_ https://drive.google.com/file/d/1FRqlEk3-mLSEJ3Kkisuwhbx-87Ohe_d3/view?usp=sharing

_**Analiz Raporu:**_ https://drive.google.com/file/d/1w2tdzo9oIIw--5JP8avNRhyNFnhRfch-/view?usp=sharing

_**Gerçekleştirme Raporu :**_ https://drive.google.com/file/d/14kLWsumYjdwR_FmPwQ6c7T7m0rWlA3lG/view?usp=sharing

_**Test Raporu :**_ https://drive.google.com/file/d/1nQSvRb8lQ3OneQpTp5TbLt2jlGOewmQr/view?usp=sharing

_**Sunum :**_ https://drive.google.com/file/d/16wG7iUtaM9_rnpXoyUMUTieuZvPQaFwj/view?usp=sharing



###### Okul Zil ve Duyuru Sistemi Raporu

**Kısa Özet**

Bilindiği üzere okulların alt yapısında zil sistemi bulunmaktadır. Raspberry Pi’yi web sunucusu olarak kullanarak okul yerel alan ağından; zil ve duyuru otomasyonu gerçekleştirmeyi planladık.

Problem Tanımı Okul yerel alan ağında, herhangi bir cihaz üzerinden web arayüzüne giriş yapılarak sesli duyuru yapılabilir mi? Nöbetçi öğrenciye ihtiyaç duymadan herhangi bir kişinin (sadece sistem üzerinden duyuru metni girilerek konuşmaya dönüştürülmesiyle) idareye çağırılabilmesi, Zil saatlerinin sistem üzerinden ayarlanıp çalınabilmesi, Törenlerdeki İstiklal Marşı’nın okul bahçesinde mobil cihazdan da başlatılabilmesi, Belirli gün ve haftalarda müzik yayını yapılabilmesidir.

Analiz Süreci Problemin çözümü için proje ekibimizle yaptığımız uzaktan toplantılarda problemin detaylı analizi gerçekleştirldi. Bu toplantılarda her sınıfa etkileşimli tahta bulunması, bu tahtaların genelde öğretmenler odalarında da bulunması, projenin kullanılabilir olduğu görüşünü destekledi. Bu analizler sonucunda, programlama dili olarak Python kullanılmasına, programın görsel tasarımında Python kurulumu ile birlikte geldiği için Tkinter modülünün kulllanılmasına, ses bildirimleri için pygame modülünün kullanılmasına ve günlük ders programının tutulması içinse JSON modülünün kullanılmasına kararına varıldı.

İhtiyaç Analizi Okullarda; zil ve duyuru sisteminin belirli kişilere yetki verildiği takdirde herhangi bir cihazdan ya da santral odasından bağımsız ve okul yerel ağından (örneğin okul bahçesinden) kontrol edilmesini sağlamaktır.

İçerik Analizi Projemizde; Raspberry Pi’yi web sunucusu, Django’yu da web programlamada kullanmayı hedefledik. Ders giriş çıkış saatleri, veritabanında tutulacaktır. Tek tuşla zil pasif hale getirilip, ders saatlerinden bağımsız olarak istendiğinde de çalınabilecektir. MP3 dosyaları zil melodisi olarak ayarlanabilecektir. Ayrıca İstiklal Marşı ya da günün anlam ve önemine uygun ses dosyaları sisteme yüklenip çalınabilecektir. Girilen duyuru metinlerinin Google API’yle sese dönüştürülmesi sağlanacaktır.

Durum Ortam Analizi Donanım: Raspberry Pi Web programlama: Django Veritabanı: SQLite3 Arayüz Tasarımı: HTML, CSS, JavaScript Python modülleri: gTTS, playsound, os, system

Kullanıcı Analizi Projemiz github’a yükleneceği için her zaman açık kaynak bir özelliğe sahip olacaktır. Hedef kitlemiz Milli Eğitim Bakanlığı’na bağlı resmi ve özel okullardır. Gerekli kurulumlar yapıldığı takdirde kolaylıkla tüm okullar yazılımdan faydalanabilecektir.

Okul Zil ve Duyuru Sistemi Raporu Kısa Özet Projenin Tasarım sürecinde uygulanan süreç adımlarının ifade edildiği bölümdür.

Veri Tasarımı Projede veritabanı kullanıldığı durumda veritabanı diyagramı bu bölüm içerisinde yer almaktadır.

Ara yüz Tasarımı Kullanıcı ara yüzüne ait tasarımların (Mock Up) yer aldığı bölümdür.

Kod Tasarımı Yazılım geliştirme süreci sırasında Nesne Yönelimli Programlama dikkate alınarak (Class Diagram) tasarımlar bu alanda yer almaktadır.

Zaman Çizelgesi Projenin rapor yazım süreçleri de dahil edilerek gerektiğinde iç içe geçmiş süreçlerinde ifade edilebileceği bölümdür. (Gannt Chart)  

Okul Zil ve Duyuru Sistemi Gerçekleştirme Raporu Karşılaşılan Sorunlar ve Uygulanan Çözümler Projenin gerçekleştirme sürecine karşılaşılan sorunlar ve gidermek için uygulanan çözümlerin ifade edildiği bölümler.

Proje Bileşenleri ve Görevleri Programa ait dökümantasyonun taslak halininde ortaya çıktığı bölümdür.

Github Yükleme Süreci Yazılım kaynak kodunun github profilinde paylaşılması farklı bir kullanıcı tarafından başka bir platforma yüklenmesi sürecinde yapılması gerekenlerin yer aldığı bölümdür.

Okul Zil ve Duyuru Sistemi Test Raporu Karşılaşılan Sorunlar ve Uygulanan Çözümler Yazılım projesinin çalıştırılması ve test edilmesi süresince karşılaşılan sorunlar ve uygulanan çözümler yer almaktadır.

Test Sürecinde Kullanılan Modüller (Varsa) Proje test sürecinde gerektiğinde farklı modüller kullanılarak test çalışması gerçekleştirilmektedir. Proje sürecinde eğer bu modüllerden herhangi birini kullandıysanız. Modülü kullanırken yaptığınız kodlama bu bölümde yer almaktadır.  

Görev dağılımı

Analiz Raporunun Tamamlanması Sadık BARAK, Şenol IRMAK, Barboros KIZILKOCA, Murat SAPMAZ, Nuri TIRAŞ, Ersin TORUNOĞLU, Özcan TOY, Ömer YAVUZ, İbrahim Talha YILMAZ, Leyla YILMAZ

Tasarım Raporunun Tamamlanması Sadık BARAK, Şenol IRMAK, Barboros KIZILKOCA, Murat SAPMAZ, Nuri TIRAŞ, Ersin TORUNOĞLU, Özcan TOY, Ömer YAVUZ, İbrahim Talha YILMAZ, Leyla YILMAZ

Gerçekleştirim Raporunun Tamamlanması Sadık BARAK, Şenol IRMAK, Barboros KIZILKOCA, Murat SAPMAZ, Nuri TIRAŞ, Ersin TORUNOĞLU, Özcan TOY, Ömer YAVUZ, İbrahim Talha YILMAZ, Leyla YILMAZ

Gantt Diagramı Sadık BARAK, Şenol IRMAK, Barboros KIZILKOCA, Murat SAPMAZ, Nuri TIRAŞ, Ersin TORUNOĞLU, Özcan TOY, Ömer YAVUZ, İbrahim Talha YILMAZ, Leyla YILMAZ

Arayüz tasarımı Sadık BARAK, Şenol IRMAK, Barboros KIZILKOCA, Murat SAPMAZ, Nuri TIRAŞ, Ersin TORUNOĞLU, Özcan TOY, Ömer YAVUZ, İbrahim Talha YILMAZ, Leyla YILMAZ

Veri Tasarımı-Sınıf Tasarımı Sadık BARAK, Şenol IRMAK, Barboros KIZILKOCA, Murat SAPMAZ, Nuri TIRAŞ, Ersin TORUNOĞLU, Özcan TOY, Ömer YAVUZ, İbrahim Talha YILMAZ, Leyla YILMAZ Gökhan Dağlı

Programın Çalıştırılması Sadık BARAK, Şenol IRMAK, Barboros KIZILKOCA, Murat SAPMAZ, Nuri TIRAŞ, Ersin TORUNOĞLU, Özcan TOY, Ömer YAVUZ, İbrahim Talha YILMAZ, Leyla YILMAZ

Yazılım Test Çalışması Sadık BARAK, Şenol IRMAK, Barboros KIZILKOCA, Murat SAPMAZ, Nuri TIRAŞ, Ersin TORUNOĞLU, Özcan TOY, Ömer YAVUZ, İbrahim Talha YILMAZ, Leyla YILMAZ