#1.Soru
#ge=Gelirler
#gi=Giderler
#tc=Toplam Ciro
#tcs=Toplam Çalışan Sıyısı
def isletmeKari (ge,gi):
    ge=int(ge)
    gi=int(gi)
    isletmeKari=ge-gi
    print(isletmeKari)
def adambasiCiro (tc,tcs):
    tc=int(tc)
    tcs=int(tcs)
    adambasiCiro=tc/tcs
    print(adambasiCiro)



#2.soru:
class aktif():
    def hesapla(kasa,alınan,bankalar,alıcak,ticari,binalar,tasitlar,demirB):
        aktif=(kasa+alınan+bankalar+alıcak+ticari+binalar+tasitlar+demirB)
        return aktif
class pasif():
    def hesapla(banka,satıcılar,bankaK,borc,özS):
        pasif=(banka+satıcılar+bankaK+borc+özS)
        return pasif


#3.soru:
class etkilesim_orani():
    def __init__(self,begeni,yorum,paylasim,icerik,takip):
        etkilesim=(((begeni+yorum+paylasim)/icerik)/takip)*100
        print(float(etkilesim))
        if etkilesim>=0.20:
           print("Başarılı")
        else:
            print("Başarısız")
