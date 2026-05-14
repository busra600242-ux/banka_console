hesaplar ={
    "kullanıcıadı " : "busra",
    "bakiye":50000
}

while True:
    print("hangi işlemi yapmak istersiniz:")
    print("1-para yatır")
    print("2-para çek")
    print("3-hesabı görüntüle")
    print("4-çıkış")

    islem = input("hangi işlemi yapmak istersiniz? işlem numarasını giriniz.:  ")
    if islem == "1":
        para_yatırma = int(input("yatırma miktarını giriniz:"))
        hesaplar["bakiye"] = para_yatırma
        print("bakiyenideki yeni miktar:", hesaplar["bakiye"])
        print("güncel profiliniz:", hesaplar)
        break

    elif islem == "2":
     while True:
        para_cekme = int(input("çekmek istedğiniz miktarı giriniz:"))
        if para_cekme > hesaplar["bakiye"]:
            print("yetersiz bakiye")
            continue
        else:
            hesaplar["bakiye"] -= para_cekme
            print("güncel bakiyeniz:", hesaplar["bakiye"])
            print("güncel profiliniz:", hesaplar)
            print("İYİ GÜNLER DİLERİZ", hesaplar["kullanıcıadı"])
            print("İYİ GÜNLER DİLERİZ", hesaplar["kullanıcıadı"])
            break

    elif islem == "3":
        print("hesabınzın güncel profil:", hesaplar)
        print("İYİ GÜNLER DİLERİZ", hesaplar["kullanıcıadı"])
        break

    elif islem == "4":
        print("çıkış yapıılıyor....")
        print("İYİ GÜNLER DİLERİZ", hesaplar["kullanıcıadı"])
        break

       
