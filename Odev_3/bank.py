# Kullanıcıdan analiz edilecek metni veya paragrafı input fonksiyonu ile alıyoruz.
metin = input("Lütfen bir cümle giriniz: ")

# Boşluklar dahil toplam karakter sayısını len fonksiyonu ile hesaplıyoruz.
toplam_karakter = len(metin)

#harf ayrımını ortadan kaldırmak için tüm metni küçük harfe çeviriyoruz.
kucuk_metin = metin.lower()

# Küçük harfe çevrilen metni boşluk karakterlerinden bölerek kelimelerden oluşan bir liste elde ediyoruz.
kelimeler = kucuk_metin.split()

# Liste içindeki eleman sayısını alarak toplam kelime sayısını buluyoruz.
toplam_kelime = len(kelimeler)

# Max() fonksiyonu ve key=len parametresi ile en uzun kelimeyi bulup uzunluğunu alıyoruz.
if kelimeler:
    # Listede karakter uzunluğu en büyük olan kelimeyi seçip len() ile karakter sayısını hesaplıyoruz.
    en_uzun_kelime_uzunlugu = len(max(kelimeler, key=len))
else:
    # Kullanıcı hiç kelime girmediyse hata almamak için uzunluğu 0 olarak belirliyoruz.
    en_uzun_kelime_uzunlugu = 0

# Her bir kelimenin kaç kez geçtiğini anahtar-değer (kelime: adet) olarak tutacak boş bir sözlük oluşturuyoruz.
tekrarlarr = {}

# Kelimeler listesindeki her bir kelimeyi tek tek dolaşmak için for döngüsü başlatıyoruz.
for kelime in kelimeler:
    # Kelime daha önce sözlüğe eklenmiş mi diye kontrol ediyoruz.
    if kelime in tekrarlarr:
        # Kelime sözlükte zaten varsa mevcut sayacını 1 artırıyoruz.
        tekrarlarr[kelime] += 1
    else:
        # Kelime sözlükte yoksa ilk kez karşılaşıyoruz demektir, değerini 1 olarak ekliyoruz.
        tekrarlarr[kelime] = 1

# Sonuçları ekranda düzenli göstermek için bir ayraç çizgisi yazdırıyoruz.
print("\n--- METİN İSTATİSTİKLERİ ---")

# Hesaplanan toplam kelime sayısını ekrana yazdırıyoruz.
print(f"Toplam Kelime Sayısı: {toplam_kelime}")

# Boşluklar dahil toplam karakter sayısını ekrana yazdırıyoruz.
print(f"Toplam Karakter Sayısı (Boşluklar Dahil): {toplam_karakter}")

# Bulunan en uzun kelimenin kaç karakter olduğunu ekrana yazdırıyoruz.
print(f"En Uzun Kelimenin Uzunluğu: {en_uzun_kelime_uzunlugu}")

# Kelime tekrarları listesi için alt başlık yazdırıyoruz.
print("\nKelime Tekrar Sayıları:")

# Eğer kullanıcı hiç kelime girmediyse uyarı veriyoruz.
if not tekrarlarr:
    # Metinde analiz edilecek geçerli bir kelime olmadığını belirtiyoruz.
    print("Metinde sayılacak kelime bulunamadı.")
else:
    # Sözlükteki her bir kelime ve tekrar sayısını sırayla almak için döngü kuruyoruz.
    for kelime, adet in tekrarlarr.items():
        # Kelimeyi ve kaç kez tekrar ettiğini formatlı şekilde ekrana yazdırıyoruz.
        print(f"- '{kelime}': {adet} kez")







        