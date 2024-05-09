class Bolum:
    def __init__(self,bolum_adi,hocalar:list,dersler:list) :
        self.bolum_adi=bolum_adi
        self.hocalar=hocalar
        self.dersler=dersler
    def bilgigetir(self):
        return f"bölüm class'ı oluşturuldu"   
    



class Ogrenci(Bolum):
    def __init__(self, ad,soyad,numara,bolum_adi, hocalar: list, dersler: list):
        super().__init__(bolum_adi, hocalar, dersler) 

        self.ad=ad
        self.soyad=soyad
        self.numara=numara

    def bilgigetir(self):
        return f"Ögrencinin adı:{self.ad} soyadı:{self.soyad}"
    
ogr_1=Ogrenci("sıla","tezcan",2212503005,"YBS",["Ömer Faruk OKTAR","FURKAN HOCA"],["VYST","NESNEL TASARIM"])
print(ogr_1.bilgigetir())

class Sirket:
    def __init__(self,sirket_adi,sirket_calisanlari:list,ürünler:list) :
        self.sirket_adi=sirket_adi
        self.sirket_calisanlari=sirket_calisanlari
        self.ürünler=ürünler
    def bilgiGetir(self):
        return f"sirketin class kısmı oluştu." 
class Sehirler(Sirket):
    def __init__(self, sehir_adi,sehir_kodu, sirket_adi, sirket_calisanlari: list, ürünler: list):
        super().__init__(sirket_adi, sirket_calisanlari, ürünler)
        self.sehir_adi=sehir_adi
        self.sehir_kodu=sehir_kodu
    def bilgiGetir(self):
        return f"sirketin adı={self.sirket_adi} ve ürünleri:{self.ürünler} bu ürünlerin gideceği sehirler={self.sehir_adi}"

sirket=Sehirler("ISPARTA","32000","SNT",["ASLI GÜLER","SULTAN AKBAŞ","MURAT KURUM"],["TV","PHONE","LAPTOP"])   
print(sirket.bilgiGetir())

#Departman adında class oluşturun.
# bu class'ın özellikleri (attributes): (Aşağıda)
# departman_ad, departman_yonetici, eleman_sayisi, eleman_maas
# maasHesapla isminde instance seviyesinde bir fonksiyon yazın
# bu fonksiyon dışarıdan değer almayacak ve çalışanın maaşına yüzde 60 zam yapmak
# üzere tasarlanmış olacak.
class Departman:
    zam=0.60
    def __init__(self,departman_adi,departman_yönetici,eleman_sayisi,eleman_maas):
        self.departman_adi=departman_adi
        self.departman_yönetici=departman_yönetici
        self.eleman_sayisi=eleman_sayisi
        self.eleman_maas=eleman_maas
    def bilgiGetir(self):
        return (self.eleman_maas*0.60)+self.eleman_maas
dep1=Departman("İK","SILA NUR TEZCAN",32,20000)
print(dep1.bilgiGetir())

# Muhasebe adında bir class tanımlayın
# bu class, Departman class'ını miras alacak.
# Ek olarak, Muhasebe class'ının evrak_giderleri adında bir özelliği (atttribute) olacak
# Bunun yanında, Muhasebe class'ının maasHesapla() fonksiyonunda maaş zaman oranı
# yüzde 60 yerine yüzde 55 olarak hesaplanacak

class Muhasebe(Departman):
    def __init__(self, evrak_giderleri,departman_adi, departman_yönetici, eleman_sayisi, eleman_maas):
        super().__init__(departman_adi, departman_yönetici, eleman_sayisi, eleman_maas)
        self.evrak_giderleri=evrak_giderleri
    def maashesaplama(self):
        return (self.eleman_maas*0.55)+self.eleman_maas
muh1=Muhasebe("ik","SILA NUR TEZCAN",32,20000,1500)

    
print("eski zamlı maas: ",dep1.bilgiGetir())
print("yeni zamlı maas: ",muh1.maashesaplama())
    


# Departman adında bir class tanımlayın
# bu class'ın maas_orani(0.5) isminde bir class seviyesinde özniteliği olacak
# bu classın: departman_ad, eleman_sayisi, isminde özniteliği olacak (instance)

class Departman:
    maas_orani=0.5
    def __init__(self,departman_adi,eleman_sayisi):
        self.departman_adi=departman_adi
        self.eleman_sayisi=eleman_sayisi
    
 # IT isminde bir class oluşturun.
# bu class Departman class'ını miras alacak.
# maas_orani özniteliğini yüzde 65 olarak değiştirin
# IT class'ının contructor (yapıcı metod) metodunda departman_ad özelliği
# varsayılan olarak "IT" yazılacak

class IT(Departman):
    maas_orani=0.65   
    def __init__(self,  eleman_sayisi,departman_adi="IT"):
        super().__init__(departman_adi, eleman_sayisi)

# Personel isminde bir class yazın
# IT class'ını miras alacak
# maas_orani %62 olacak
# eleman_maas isminde bir öznitelik olacak (instance seviyesinde)
# Personel class'ına özel zamHesapla isminde bir fonksiyon yazın
# maas_orani özniteliği ile mevcut maaşı zamlı olarak hesaplayacak
# personelden bir adet instance üretin ve değeleri gösterin

class Personel(IT):
    maas_orani=0.62
    def __init__(self,eleman_maas, eleman_sayisi, departman_adi="IT"):
        super().__init__(eleman_sayisi, departman_adi)
        self.eleman_maas=eleman_maas
    def zamHesapla(self):
        return (self.eleman_maas*Personel.maas_orani)+self.eleman_maas
p2=Personel(20000,30)
print(p2.departman_adi)
print("*"*50)
print(p2.zamHesapla())

#ürün adında bir class aç
#ürün_adi,ürün_sayisi,üretildigi_yer adında özellikleri olsun

class Ürün:
    def __init__(self,ürün_adi,ürün_sayisi):
        self.ürün_adi=ürün_adi
        self.ürün_sayisi=ürün_sayisi
        

#kullanılıan ürün adında bir class aç
#ürün classını miras alsın, satılan_ürün(1500) adında class seviyesinde yaz
#satılan_ürünadi adında yeni bir özellik eklensin 
#ürün1 adında çzelliklerin bilgilerini gir
#elimizdeki ilk üründen satılan ürünü çıkarıp şuanki ürün sayısını bize versin

class Kullanilan_ürün(Ürün):
    satilan_ürün=1500
    def __init__(self,satilanürün_adi, ürün_adi, ürün_sayisi):
        super().__init__(ürün_adi, ürün_sayisi)
        self.satilanürün_adi=satilanürün_adi
    def hesap(self):
        return (self.ürün_sayisi-self.satilan_ürün)

ürün1=Kullanilan_ürün("telefon","telefon",2500)
print("*"*50)
print("elimizdeki mevcut ürün sayısı:",ürün1.hesap())
print("*"*50)

class Bolum:
    def __init__(self,bolum_ad,bolum_yönetici,eleman_maas) :
        self.bolum_ad=bolum_ad
        self.bolum_yönetici=bolum_yönetici
        self.eleman_maas=eleman_maas
    def bilgiGetir(self):
        return f"yöneticinin adı={self.bolum_yönetici} ve eleman maası={self.eleman_maas}"
class Maas(Bolum):
    zam_orani=0.45
    def __init__(self, çalisan_sayisi,bolum_ad, bolum_yönetici, eleman_maas):
        super().__init__(bolum_ad, bolum_yönetici, eleman_maas)
        self.çalisan_sayisi=çalisan_sayisi
    def zamHesapla(self):
        return (self.eleman_maas*self.zam_orani)+self.eleman_maas
b1=Maas("10","IT","NİLGÜN",25000)
print( "eski maas=",b1.eleman_maas)
print("zamli maas",b1.zamHesapla())

class Dersler:
    def __init__(self,ingilizce,türkçe) :
        self.ingilizce=ingilizce
        self.türkçe=türkçe
    def bilgiGetir(self):
        return f"dersin class kısmı oluştu."
class İşlemler(Dersler):
    matematik_saati=3
    def __init__(self,matematik, ingilizce, türkçe):
        super().__init__(ingilizce, türkçe)
        self.matematik=matematik
    def matematiksaati_hesapla(self):
        return self.matematik_saati*4
ders1=İşlemler(3,2,4)
print("haftalık türkçe ders saati:",ders1.türkçe)
print("haftalık matematik ders saati: ",ders1.matematik)
print("aylık matematik ders saati:",ders1.matematiksaati_hesapla())

#Departman adında class oluşturun.
# bu class'ın özellikleri (attributes): (Aşağıda)
# departman_ad, departman_yonetici, eleman_sayisi, eleman_maas
# maasHesapla isminde instance seviyesinde bir fonksiyon yazın
# bu fonksiyon dışarıdan değer almayacak ve çalışanın maaşına yüzde 60 zam yapmak
# üzere tasarlanmış olacak.
class Departman:
    def __init__(self,departman_ad,dep_yonetici,eleman_sayisi,eleman_maas) :
        self.departman_ad=departman_ad
        self.dep_yonetici=dep_yonetici
        self.eleman_sayisi=eleman_sayisi
        self.eleman_maas=eleman_maas
    def maasHesapla(self):
        return (self.eleman_maas*0.60)+self.eleman_maas

# Muhasebe adında bir class tanımlayın
# bu class, Departman class'ını miras alacak.
# Ek olarak, Muhasebe class'ının evrak_giderleri adında bir özelliği (atttribute) olacak
# Bunun yanında, Muhasebe class'ının maasHesapla() fonksiyonunda maaş zaman oranı
# yüzde 60 yerine yüzde 55 olarak hesaplanacak

class Muhasebe(Departman):
    def __init__(self, departman_ad, dep_yonetici, eleman_sayisi, eleman_maas,evrak_giderleri):
        super().__init__(departman_ad, dep_yonetici, eleman_sayisi, eleman_maas)
        self.evrak_giderleri=evrak_giderleri
    def maasHesapla(self):
        return (self.eleman_maas*0.55)+self.eleman_maas
d1=Muhasebe("IK","SILA",32,20000,1500)
print("eski maas:",d1.eleman_maas)
print("yeni zamlı maas:",d1.maasHesapla())




 
