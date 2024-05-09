#ZTYO isminde bir class oluşurun
#öznitelikler => bolum_ad

#YBS ve BST isminde 2 class oluşturun
# bunların da hocalar,dersler,ogrenci_sayisi isminde
#öznitelikleri oalcak

#mezun sayısı isimli bir öznitelik de her iki class'da olacak
#ama bunu kapsülleyin
#sadece get metodu yazın
# set edilmeyecek, başlangıçta hangi değer verildiyse
# öyle devam edecek


from typing import Any


class ZTYO:
    def __init__(self,bolum_ad) :
        self.bolum_ad=bolum_ad
class YBS(ZTYO):
    def __init__(self,hocalar,dersler,ogrenci_sayisi,mezun_sayisi,bolum_ad="ybs"):
        super().__init__(bolum_ad)
        self.hocalar=hocalar
        self.dersler=dersler
        self.ogrenci_sayisi=ogrenci_sayisi
        self._mezun_sayisi=mezun_sayisi
    def get_mezun_sayisi(self):
        return self._mezun_sayisi

class BST(ZTYO):
    def __init__(self,hocalar,dersler,ogrenci_sayisi,mezun_sayisi,bolum_ad="ybs"):
        super().__init__(bolum_ad)
        self.hocalar=hocalar
        self.dersler=dersler
        self.ogrenci_sayisi=ogrenci_sayisi
        self._mezun_sayisi=mezun_sayisi
    def get_mezun_sayisi(self):
        return self._mezun_sayisi
ybs_1=YBS("furkan altan","vyys",32,25)
print(ybs_1._mezun_sayisi)
print(ybs_1.get_mezun_sayisi())

class Personel:
    def __init__(self,ad,soyad) :
        self.ad=ad
        self.soyad=soyad
    @property
    def ad_soyad(self):
        return f"{self.ad},{self.soyad}"
    @property
    def mail(self):
        return f"{self.ad}.{self.soyad}@gmail.com"
    @ad_soyad.setter
    def ad_soyad(self,isim):
        ad,soyad=isim.split(" ")
        self.ad=ad
        self.soyad=soyad

    
p1=Personel("sıla","tezcan")
p1.ad="nur"
print(p1.ad)

p1.ad_soyad="çisem çetin"
print(p1.ad_soyad)

p1.mail="sılan@gmail.com"

print(p1.mail)


class ZTYO:
    def __init__(self,bolum_ad):
        self.bolum_ad=bolum_ad
class YBS(ZTYO):
    def __init__(self,hocalar,dersler,ogr_sayisi,mezun_sayisi, bolum_ad="ybs"):
        super().__init__(bolum_ad)
        self.hocalar=hocalar
        self.dersler=dersler
        self.ogr_sayisi=ogr_sayisi
        self._mezun_sayisi=mezun_sayisi
    def get_mezun_sayisi(self):
        return self._mezun_sayisi

class BST(ZTYO):
    def __init__(self,hocalar,dersler,ogr_sayisi,mezun_sayisi, bolum_ad="ybs"):
        super().__init__(bolum_ad)
        self.hocalar=hocalar
        self.dersler=dersler
        self.ogr_sayisi=ogr_sayisi
        self._mezun_sayisi=mezun_sayisi
    def get_mezun_sayisi(self):
        return self._mezun_sayisi
p1=YBS("FURKAN ALTAN","VYSS",30,32)


print(p1._mezun_sayisi)
print(p1.get_mezun_sayisi)