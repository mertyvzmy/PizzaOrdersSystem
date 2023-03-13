import csv
import datetime as dt


# Üst Sınıf ------------------------------------------
class Pizza:
    def __init__(self, tip, cost, description):
        self._tip = tip
        self._cost = cost
        self._description = description

    def get_tip(self):
        return self._tip

    def get_cost(self):
        return self._cost

    def get_description(self):
        return self._description


# -------------------------------------------------------------------------


# Alt Sınıflar-------------------------------------------------------------
class Klasik(Pizza):
    def __init__(self):
        super().__init__("Klasik", 120, ", Domates, Mantar, Kaşar Peyniri, Sucuk, Salam ve Sosis")

    def get_description(self):
        return f"Seçtiğiniz {self._tip}  pizzanın içeriğinde {self._description} bulunmaktadır."


class Margarita(Pizza):
    def __init__(self):
        super().__init__("Margarita", 110, "Domates, Mozzarella Peyniri, Fesleğen ve Zeytinyağı")

    def get_description(self):
        return f"Seçtiğiniz {self._tip}  pizzanın içeriğinde {self._description} bulunmaktadır."


class Marinara(Pizza):
    def __init__(self):
        super().__init__("Marinara", 110, "Domates, Kekik, Sarımsak, Sızma Zeytinyağı ve Taze Fesleğen")

    def get_description(self):
        return f"Seçtiğiniz {self._tip}  pizzanın içeriğinde {self._description} bulunmaktadır."


class Quattro(Pizza):
    def __init__(self):
        super().__init__("Quattro Stagioni", 170, "İstiridye, Karides, Istakoz Eti, Kalamar ve Midye")

    def get_description(self):
        return f"Seçtiğiniz {self._tip}  pizzanın içeriğinde {self._description} bulunmaktadır."


class Frutti(Pizza):
    def __init__(self):
        super().__init__("Frutti Di Mare", 200, "Domates, Peynir, Hamsi, Mantar, Soğan, Zeytin, Ananas ve Et")

    def get_description(self):
        return f"Seçtiğiniz {self._tip}  pizzanın içeriğinde {self._description} bulunmaktadır."


# -------------------------------------------------------------------


# Decarator Sınıfı(Ek Malzemeler)-----------------------------------
class Decorator(Pizza):
    def __init__(self, ekstra):
        self.ekstra = ekstra

    def get_description(self):
        return self.ekstra.get_description() + ", " + self._description

    def get_cost(self):
        return self.ekstra.get_cost()


class Zeytin(Decorator):
    def __init__(self, ekstra):
        super().__init__(ekstra)
        self._description = " Zeytin"
        self._cost = 8

    def get_description(self):
        return self.ekstra.get_description() + ", " + self._description

    def get_cost(self):
        return self.ekstra.get_cost() + self._cost


class Cheddar(Decorator):
    def __init__(self, ekstra):
        super().__init__(ekstra)
        self._description = " Cheddar"
        self._cost = 10

    def get_description(self):
        return self.ekstra.get_description() + ", " + self._description

    def get_cost(self):
        return self.ekstra.get_cost() + self._cost


class Mantar(Decorator):
    def __init__(self, ekstra):
        super().__init__(ekstra)
        self._description = " Mantar"
        self._cost = 8

    def get_description(self):
        return self.ekstra.get_description() + ", " + self._description

    def get_cost(self):
        return self.ekstra.get_cost() + self._cost


class Sucuk(Decorator):
    def __init__(self, ekstra):
        super().__init__(ekstra)
        self._description = " Sucuk"
        self._cost = 10

    def get_description(self):
        return self.ekstra.get_description() + ", " + self._description

    def get_cost(self):
        return self.ekstra.get_cost() + self._cost


# -------------------------------------------------------------

# -------------------------------------------------------------

# Main Fonksiyonu --------------------------------------------
def main():
    with open("_menu.csv") as menu:
        okuyucu = csv.reader(menu)

        for satir in okuyucu:
            print(satir)


print("Menüyü Görüntülemek İçin M Tuşuna Basınız :")
kullanici_secimi = input()
if kullanici_secimi.lower() == 'm':
    print(main())
else:
    print("Lütfen Belirtilen Tuş ile İşlem Yapınız")
    quit()
#--------------------------------------------------------
#Kullanıcı Bilgileri Alma-------------------------------
def kk_bil():
    ad = ''
    while ad == '':
        ad = input('Adınızı ve Soyadınız Giriniz : ')
        if ad == '':
            print('Lütfen Adınızı Giriniz...!')

    tckn = ''
    while tckn == '':
        tckn = input('TC Kimlik Numaranızı Giriniz : ')
        if len(tckn) != 11:
            print('Lütfen 11 Haneli TC Kimlik Numaranızı Giriniz...!')
            tckn = ''

    kk_numara = ''
    while kk_numara == '':
        kk_numara = input('Kredi Kartı Numaranızı Giriniz : ')
        if len(kk_numara) != 16:
            print('Lütfen 11 Haneli Kredi Kartı Numaranızı Giriniz ...!')
            kk_numara = ''

    kk_sifre = ''
    while kk_sifre == '':
        kk_sifre = input('Kart Şifrenizi Giriniz : ')
        if len(kk_sifre) != 4:
            print('Lütfen 4 Haneli Kredi Kartı Şifrenizi Giriniz...!')

    return ad, tckn, kk_numara, kk_sifre


def kullanici_bil():
    with open('Orders_Database.csv', 'w', newline='') as sip:
        writer = csv.writer(sip)
        writer.writerow(['Ad', 'Tc Kimlik", "Kart Numarası", "KartŞifresi', 'Sipariş Tarihi'])
    sip.close()


def kk_yaz(ad, tc_kimlik, kk_no, kk_sifre):
    with open('Orders_Database.csv', 'a', newline='') as sip:
        writer = csv.writer(sip)
        writer.writerow([ad, tc_kimlik, kk_no, kk_sifre, dt.datetime.now().strftime("%d.%m-%Y %H:%M")])
    sip.close()

def tarih_bil():
    tarih = dt.datetime.now()
    saat = dt.datetime.now()
    tarih_str = tarih.strftime("%d-%m-%Y")
    saat_str = saat.strftime("%H:%M:%S")
    return tarih_str, saat_str

#-----------------------------------------------------------------------------------


sepet = []
fiyat = []
pizza1 = Klasik()
pizza2 = Margarita()
pizza3 = Marinara()
pizza4 = Quattro()
pizza5 = Frutti()

ek1 = Zeytin(Decorator)
ek2 = Cheddar(Decorator)
ek3 = Mantar(Decorator)
ek4 = Sucuk(Decorator)

# Pizza Seçimi Yapılır ------------------------------------------------
while True:
    pizza_sec = input(
        "\n Lütfen Menüde Listelenen Sıra Numarasına Göre Pizza Seçimi Yapınız(Çıkmak İçin 'q', Onaylamak İçin 'o' Basınız) : ")
    if pizza_sec == 'o' or pizza_sec == 'O':
        break
    if pizza_sec == 'q' or pizza_sec == 'Q':
        quit()
    if pizza_sec == '1':
        print(f"\n{pizza1.get_tip()} Pizza Seçtiniz...")
        print(f"Seçilen Pizzanın içindekiler : {pizza1.get_description()}")
        sepet.append(pizza1.get_tip())
        fiyat.append(pizza1.get_cost())

    if pizza_sec == '2':
        print(f"\n{pizza2.get_tip()} Pizza Seçtiniz...")
        print(f"Seçilen Pizzanın içindekiler : {pizza2.get_description()}")
        sepet.append(pizza2.get_tip())
        fiyat.append(pizza2.get_cost())

    if pizza_sec == '3':
        print(f"\n{pizza3.get_tip()} Pizza Seçtiniz...")
        print(f"Seçilen Pizzanın içindekiler : {pizza3.get_description()}")
        sepet.append(pizza3.get_tip())
        fiyat.append(pizza3.get_cost())
    if pizza_sec == '4':
        print(f"\n{pizza4.get_tip()} Pizza Seçtiniz...")
        print(f"Seçilen Pizzanın içindekiler : {pizza4.get_description()}")
        sepet.append(pizza4.get_tip())
        fiyat.append(pizza4.get_cost())
    if pizza_sec == '5':
        print(f"\n{pizza5.get_tip()} Pizza Seçtiniz...")
        print(f"Seçilen Pizzanın içindekiler : {pizza5.get_description()}")
        sepet.append(pizza5.get_tip())
        fiyat.append(pizza5.get_cost())

# -----------------------------------------------------------------------

# Ek Malzeme Seçimi -----------------------------------------------------
while True:
    ek_sec = input(
        "\n Sepetinizde Bulunan Pizzalara Ek Malzeme Eklemek İçin Menüde Listenen Numarasına Göre Seçim Yapınız (Onaylamak İçin 'o' Basınız) : ")
    if ek_sec == 'o':
        break
    if ek_sec == '1':
        print(f"\n{ek1._description} Seçildi...")
        sepet.append(ek1._description)
        fiyat.append(ek1._cost)
    if ek_sec == '2':
        print(f"\n{ek2._description} Seçildi...")
        sepet.append(ek2._description)
        fiyat.append(ek2._cost)
    if ek_sec == '3':
        print(f"\n{ek3._description} Seçildi...")
        sepet.append(ek3._description)
        fiyat.append(ek3._cost)
    if ek_sec == '4':
        print(f"\n{ek2._description} Seçildi...")
        sepet.append(ek4._description)
        fiyat.append(ek4._cost)
# -------------------------------------------------------------------------

print("\nSepetiniz : ", sepet)
print("Toplam ", sum(fiyat), "TL")

# Sepetten Ürün Çıkarma----------------------------------------------------
while True:
    kont = input("Sepetinizden Ürün Çıkarmak İstiyormusunuz ? (e/h) ")
    if kont == 'e':
        sil = int(input("Kaldırmak İstediğiniz Ürünün Sepetteki Sıra Numarasını Tuşlayın : "))
        if sil > 0 and sil <= len(sepet and fiyat):
            sil_sepet = sepet.pop(sil - 1)
            sil_fiyat = fiyat.pop(sil - 1)
            print("\nSeçili Ürün Çıkartıldı")
            print(sepet)
            print("Toplam ", sum(fiyat), "TL")
    if kont == 'h':
        print("\nÖdeme Bilgileri İçin Yönlendiriliyorsunuz...")
        break
# -------------------------------------------------------------------------

print("Sepet İçeriği : ", sepet)
print("Ödenecek Tutar :  ", sum(fiyat), "TL")

# Ödeme Yöntemi--------------------------------------------------
ad, tckn, kk_numara, kk_sifre =kk_bil()
kk_yaz(ad, tckn, kk_numara, kk_sifre)
print("Ödeme İşleminiz Tamamlandı... Afiyet Olsun.")
# ---------------------------------------------------------------
print(tarih_bil())