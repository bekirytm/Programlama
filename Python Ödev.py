
fg=int(input("Finansman gelirleri:"))
pg=int(input("Pazar gelirleri:"))
kg=int(input("Kira gelirleri:"))
uc=int(input("Ücret:"))
fgi=int(input("Finansman Giderleri:"))
pgi=int(input("Pazar Giderleri:"))
kgi=int(input("Kira Giderleri:"))
mgi=int(input("Muhasebe Giderleri:"))
tgelir=fg+pg+kg
tgider=uc+fgi+pgi+kgi+mgi
if (tgelir-tgider)>1000:
    print("işletme kardadır.")
else:
    print("işletme karda değildir.")



def kullan():
    pus=int(input("Planlanmış Üretim Süresi:"))
    pd=int(input("Plansız Duruş:"))
    kull=(pus-pd)/pus
    print("Kullanılabilirlik oranınız:",kull)

def performans():
    pus=int(input("Planlanmış Üretim Süresi:"))
    pd=int(input("Plansız Duruş:"))
    scz=int(input("Standart Çevrim Zamanı:"))
    um=int(input("Üretim Miktarı:"))
    perf=(scz*um)/(pus-pd)
    print("performansınız:",perf)

def kalite():
    sumi=int(input("Sağlam Ürün Miktarı:"))
    tum=int(input("Toplam Üretim Miktarı:"))
    klt=sumi/tum
    print("kaliteniz:",klt)

def oee():
    kull=int(input("Kullanılabilirlik Oranınızı Giriniz:"))
    perf=int(input("Performansınızı Giriniz:"))
    klt=int(input("Kalitenizi Giriniz:"))
    orn=100/100
    oeee=kull*perf*klt*orn
    print("İşletmenin Ekipman Etkinlik Oranı:",oeee)



def ciro():
    sm=int(input("Satış Miktarını Giriniz:"))
    bsf=int(input("Birim Satış Fiyatını Giriniz:"))
    cro=sm*bsf
    print("Cironuz:",cro)

def adambciro():
    tc=int(input("Toplam Cironuzu Giriniz:"))
    tcs=25
    abc=tc/tcs
    print("Adambaşı Cironuz:",abc)









