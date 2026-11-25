# 1. Hesap Sınıfını Oluşturuyoruz
class Hesap:
    # Hesap açılırken sahip, numara ve bakiye bilgilerini kaydediyoruz.
    def __init__(self, sahip, hesap_no, bakiye):
        self.sahip = sahip
        self.hesap_no = hesap_no
        self.bakiye = bakiye

    # Para yatırma fonksiyonu
    def para_yatir(self, miktar):
        self.bakiye += miktar
        print(f"{miktar} TL yatirildi. Yeni bakiye: {self.bakiye} TL")

    # Para çekme fonksiyonu
    def para_cek(self, miktar):
        if miktar <= self.bakiye:
            self.bakiye -= miktar
            print(f"{miktar} TL çekildi. Kalan bakiye: {self.bakiye} TL")
        else:
            print("Yetersiz bakiye işlemi gerçekleştirilemiyor.")

    # Bakiye görüntüleme fonksiyonu
    def bakiye_goster(self):
        print(f"Hesap Sahibi: {self.sahip} | Hesap No: {self.hesap_no} | Bakiye: {self.bakiye} TL")


# 2. Kullanıcıdan Bilgileri Alıyoruz
ad = input("Adınız Soyadınız: ")
no = input("Hesap Numaranız: ")
ilk_para = float(input("Başlangıç Bakiyeniz: "))

# Aldığımız bilgilerle hesabı oluşturuyoruz
benim_hesabim = Hesap(ad, no, ilk_para)

# 3. Hesap İşlemlerini Yapıyoruz
benim_hesabim.bakiye_goster()

yatirilacak = float(input("\nYatırmak istediğiniz tutar: "))
benim_hesabim.para_yatir(yatirilacak)

cekilecek = float(input("\nÇekmek istediğiniz tutar: "))
benim_hesabim.para_cek(cekilecek)

benim_hesabim.bakiye_goster()
