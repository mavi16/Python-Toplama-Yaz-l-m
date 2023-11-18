# UTF-8
# Developer Mavi16
# "Collection Software"

import time
import random
from random import randint
import calendar
import itertools

# Kullanıcı Paneli
kullanici = "Admin"
sifre = "16Mavi2023"
kod = "12896"
ozel_sifre = ":<v/;*/23gıAX7{(94FG=d?*1"
dogrulamakod = "901625"

komutlar = {

    "komutlar": ["...", "...."],
    "merhaba": ["Merhaba!", "Selam!", "Nasılsın?", "Hey, Selam! Hoş geldin!", "Selamm!"],
    "selam": ["Selam!", "Hey, selam!", "Selam", "Hoş geldin!"],
    "günaydın": ["Sanada günaydın, günün güzel geçsin!", "Hey, günaydın!"],
    "iyi geceler": ["Sanada iyi geceler!", "İyi geceler, tatlı uykular!"],
    "iyi öğlenler": ["İyi öğlenler!", "Sanada iyi öğlenler!"],
    "güncelleme": ["Yeni güncellemelerden haberdar olmak için Forum wepsitemizden Mavilands.Net Kategorisini takip ediniz", "Yeni güncellemeler aktif! Forumu takip edin, güncelleme notlarını forumda paylaşıyoruz."],
    "nasılsın?": ["İyiyim, teşekkür ederim!", "Harika!", "Her zamanki gibi, Mükemmel!"],
    "ismin ne?": ["Adım yok, Ben bir sohbet botuyum.", "Gelişim aşamasında olan bir yapay zekayım."],
    "naber?": ["iyiyim, ya sen?", "tabiki de!", "İyiyim, teşekkür ederim."],
    "haberler": ["Anlık. sondakika ve dğer alanlarda bilgi&haber almak için Forum wepsitemize gel! (https://mavioyun16.wixsite.com/mavi)", "Forum wepsitemizde mevcut! (https://mavioyun16.wixsite.com/mavi)"],
    "neler yapabilirsin?": ["Ben basit bir yapay zekayım, daha doğrusu sohbet botu! Sadece sistemime kayıtlı sorulara cevap verebilirim.", "Henüz gelişim aşamasındayım, sadece belirli komutlara cevap verebilirim."],
    "görevin nedir?": ["Görevim sizi eğlendirebilmek ve sorularınıza cevap verebilmek!", "Basit bir yapay zeka olduğum için çok fazla bir şey yapamıyorum."],
    "geliştiricin kim?": ["Geliştiricim kendi bilgilerini paylaşılmasını istemiyor, ama takma adı MaviOyun16.", "Takma adı MaviOyun16"],
    "geliştiricinin websitesi var mı?": ["Evet, var. İşte linki: https://mavioyun16.wixsite.com/mavi", "Linki: https://mavioyun16.wixsite.com/mavi"],
    "geliştiricinin Discord sunucusu var mı?": ["Evet, var. İşte linki: https://discord.gg/5Xj7xrG577", "Linki: https://discord.gg/5Xj7xrG577"],
    "hesap makinesi": ["Hesap makinesi özelliği aktif.", "Hesap makinesi çalışıyor."],
    "not defteri": ["Not defteri özelliği aktif.", "Not defteri çalışıyor."],
    "sosyal medya": ["Sosyal medya özelliği aktif.", "Sosyal medya çalışıyor."],
    "takvim": ["Takvim özelliği aktif.", "Takvim çalışıyor."],
    "kronometre": ["Kronometre özelliği aktif.", "Kronometre çalışıyor."],
    "liste oluşturucu": ["Liste OLuşturucu aktif.", "Liste oluşturucu çalışıyor."],
    "asal sayı kontrol": ["Asal Sayı Kontrol aktif.", "Asal Sayı Kontrol çalışıyor."],
    "hızlı yazma test": ["Hızlı Yazma Test aktif.", "Hızlı Yazma Test çalışıyor."],
    "şifre kırıcı": ["Şifre Kırıcı aktif.", "Şifre Kırıcı çalışıyor"],
    "zar oyunu": ["Zar Oyunu aktif.", "Zar oyunu çalışıyor."],
    "amiral battı oyunu": ["Amiral Battı Oyunu aktif.", "Amiral Battı Oyunu çalışıyor."],
    "sayı tahmin oyunu": ["Sayı Tahmin Oyunu aktif.", "Sayı Tahmin Oyunu çalışıyor."],
    "taş kağıt makas oyunu": ["Taş kağıt makas oyunu aktif.", "Taş kağıt makas oyunu çalışıyor."],
    "çarpım tablosu": ["Çarpım Tablosu aktif.", "Çarpım Tablosu çalışıyor."],
    "saat": ["Zamanlayıcı aktif.", "Zamanlayıcı çalışıyor."],
    "alarm": ["Alarm aktif.", "Alarm çalışıyor."],
    "vücut kitle endeksi": ["vücut kitle endeksi aktif.", "vücut kitle endeksi çalışıyor."],
    "destek talebi": ["Destek talebini discord sunucumuzdan veya wepsitemizden oluşturabilirsiniz.", "Destek talebi oluşturmak wepitemizi veya discord sunucumuzu ziyaret etmelisiniz."],
    "iletişim": ["İletişim özelliği aktif.", "İletişim özelliği çalışıyor"],
    "internet hız testi": ["Aktif.", "çalışıyor."],
    "yılan oyunu": ["Yılan oyunu aktif.", "Yılan oyunu çalışıyor."],
    "şifre oluşturucu": ["Aktif.", "Çalışıyor."],
    "metin şifreleme": ["Aktif", "Çalışıyor."],
    "ses kayıt": ["Aktif.", "çalışıyor."],
    "url video indirme": ["Aktif.", "Çalışıyor."],
    "dosya oluşturma": ["Aktif.", "çalışıyor."],
    "kurallar ve politikalar": ["Aktif.", "Çalışıyor."],
    "sürüm": ["Aktif.", "çalışıyor."],
    "internet bağlantı kontrol": ["Aktif.", "Çalışıyor."],
    "ip doğrulama": ["Aktif.", "Çalışıyor."],
    "e-posta doğrulama": ["Aktif.", "Çalışıyor."],
    "z16 antivirüs": ["Aktif.", "çalışıyor."],
    "arama": ["aktif", "çalışıyor."],
    "mayın tarlası oyunu": ["Aktif.", "çalışıyor."],
    "xox oyunu": ["Aktif.", "çalışıyor."],
    "kopyalama": ["Aktif", "çalışıyor"],
    "mavi x16": ["Hey Buradayım!", "Evet?"],
    "gps harita": ["Aktif.", "çalışıyor."],
    "afk": ["Aktif.", "çalışıyor."],
    "mavi id": ["AKTİF.", "ÇALIŞIYOR."],
    "server": ["aktif.", "çalışıyor."],
    "bilgisayar yönetimi": ["aktif.", "çalışıyor."],

}


def yanit_ver(girdi):
    girdi = girdi.lower()
    yanit = "Mavi-X16: Üzgünüm, sistemime kayıtlı böyle bir komut yok!"

    if girdi in komutlar:
        if girdi == "hesap makinesi":
            yanit = hesap_makinesi()
        elif girdi == "bilgisayar yönetimi":
            yanit = bilgisayar_yonetimi()
        elif girdi == "not defteri":
            yanit = not_defteri()
        elif girdi == "takvim":
            yanit = turkce_takvim()
        elif girdi == "kronometre":
            yanit = kronometre()
        elif girdi == "zar oyunu":
            yanit = zar_oyunu()
        elif girdi == "amiral battı oyunu":
            yanit = amiral_battı_oyunu()
        elif girdi == "liste oluşturucu":
            yanit = liste_olusturucu()
        elif girdi == "şifre kırıcı":
            yanit = sifre_kırıcı()
        elif girdi == "sayı tahmin oyunu":
            yanit = sayı_tahmin_oyunu()
        elif girdi == "asal sayı kontrol":
            yanit = asal_sayı_kontrol()
        elif girdi == "hızlı yazma test":
            yanit = hızlı_yazma_test()
        elif girdi == "çarpım tablosu":
            yanit = carpimtablosu()
        elif girdi == "taş kağıt makas oyunu":
            yanit = tas_kagit_makas()
        elif girdi == "vücut kitle endeksi":
            yanit = kitle()
        elif girdi == "destek talebi":
            yanit = destek_talebi()
        elif girdi == "sosyal medya":
            yanit = linkler()
        elif girdi == "iletişim":
            yanit = iletişim()
        elif girdi == "internet hız testi":
            yanit = test_internet_speed()
        elif girdi == "yılan oyunu":
            yanit = yilan_oyunu()
        elif girdi == "şifre oluşturucu":
            yanit = sifre_olusturucu()
        elif girdi == "metin şifreleme":
            yanit = metin_sifreleme()
        elif girdi == "ses kayıt":
            yanit = ses_kayıt()
        elif girdi == "url video indirme":
            yanit = url_video_indirme()
        elif girdi == "dosya oluşturma":
            yanit = dosya_olusturma()
        elif girdi == "kurallar ve politikalar":
            yanit = kurallar_uyarı()
        elif girdi == "sürüm":
            yanit = version()
        elif girdi == "internet bağlantı kontrol":
            yanit = internet_kontrol()
        elif girdi == "ip doğrulama":
            yanit = ip_dogrulama()
        elif girdi == "e-posta doğrulama":
            yanit = eposta_dogrulama()
        elif girdi == "z16 antivirüs":
            yanit = antivirüs()
        elif girdi == "arama":
            yanit = arama()
        elif girdi == "mayın tarlası oyunu":
            yanit = mayın_tarlası_oyunu()
        elif girdi == "xox oyunu":
            yanit = xox_oyunu()
        elif girdi == "kopyalama":
            yanit = copy_program()
        elif girdi == "saat":
            yanit = zamanlayıcı()
        elif girdi == "gps harita":
            yanit = gps_harita()
        elif girdi == "afk":
            yanit = afk()
        elif girdi == "mavi id":
            yanit = id_mavi()
        elif girdi == "server":
            yanit = server()

        else:
            yanit = random.choice(komutlar[girdi])

    return yanit


def bilgisayar_yonetimi():
    import time
    import os
    import subprocess

    def bilgisayari_kapat():
        print("Bilgisayar Kapatılıyor...")
        time.sleep(5)
        os.system("shutdown /s /t 0")

    def bilgisayari_uykuya_al():
        print("Bilgisayar uykuya alınıyor...")
        time.sleep(5)
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

    def bilgisayari_yeniden_baslat():
        print("Bilgisayar yeniden başlatılıyor...")
        time.sleep(5)
        os.system("shutdown /r /t 0")

    while True:
        komut = input(
            "Bilgisayarı kapatmak için 'kapat', uyku moduna almak için 'uyku', yeniden başlatmak için 'yeniden' yazın (Çıkış için 'q'): ").lower()

        if komut == "kapat":
            bilgisayari_kapat()
        elif komut == "uyku":
            bilgisayari_uykuya_al()
        elif komut == "yeniden":
            bilgisayari_yeniden_baslat()
        elif komut == "q":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz komut. Tekrar deneyin.")


def hesap_makinesi():
    import math
    import operator

    def toplama(a, b):
        return a + b

    def cikarma(a, b):
        return a - b

    def carpma(a, b):
        return a * b

    def bolme(a, b):
        if b != 0:
            return a / b
        else:
            return "Bölme işlemi için geçerli bir bölen giriniz!"

    def karekok(a):
        return math.sqrt(a)

    def faktoriyel(a):
        return math.factorial(a)

    def us_alma(a, b):
        return math.pow(a, b)

    def hata_mesaji():
        return "Geçersiz bir işlem veya sayı girdiniz!"

    def yapay_zeka_hesap_makinesi(islem, sayilar):
        try:
            operatorler = {
                "+": operator.add,
                "-": operator.sub,
                "*": operator.mul,
                "/": operator.truediv
            }

            if islem in operatorler:
                return operatorler[islem](*sayilar)
            elif islem == "sqrt":
                return karekok(*sayilar)
            elif islem == "fact":
                return faktoriyel(*sayilar)
            elif islem == "^":
                return us_alma(*sayilar)
            else:
                return hata_mesaji()
        except:
            return hata_mesaji()

    print("İşlemler:")
    print("+ : Toplama")
    print("- : Çıkarma")
    print("* : Çarpma")
    print("/ : Bölme")
    print("sqrt : Karekök")
    print("fact : Faktoriyel")
    print("^ : Üs Alma")

    while True:
        islem = input("Bir işlem seçin (Çıkış için 'q' girin): ")

        if islem == "q":
            time.sleep(2)
            print("- Çıkış yapılıyor...")
            time.sleep(1)
            break

        sayilar = [float(sayi) for sayi in input("Sayıları girin (virgülle ayırarak): ").split(",")]

        sonuc = yapay_zeka_hesap_makinesi(islem, sayilar)
        print("Sonuç:", sonuc)


def not_defteri():
    notlar = []  # Kayıtlı notları listeler

    while True:
        print("1 - Yeni not ekle")
        print("2 - Notları listele")
        print("3 - Not sil")
        print("4 - Tüm notları sil")
        print("5 - Not defterinden çık")

        secim = input("Seçiminizi yapın: ")

        if secim == "1":
            yeni_not = input("Yeni notu girin: ")
            notlar.append(yeni_not)
            print("Not eklendi!")
        elif secim == "2":
            if len(notlar) == 0:
                print("Not defteri boş.")
            else:
                print("Notlar:")
                for i, notum in enumerate(notlar, start=1):
                    print(f"{i}. {notum}")
        elif secim == "3":
            if len(notlar) == 0:
                print("Not defteri boş.")
            else:
                not_sil = int(input("Silmek istediğiniz notun numarasını girin: "))
                if not_sil >= 1 and not_sil <= len(notlar):
                    silinecek_not = notlar[not_sil - 1]
                    notlar.remove(silinecek_not)
                    print(f"{silinecek_not} notu silindi.")
                else:
                    print("Geçersiz not numarası!")
        elif secim == "4":
            if len(notlar) == 0:
                print("Not defteri zaten boş.")
            else:
                notlar.clear()
                print("Tüm notlar silindi!")
        elif secim == "5":
            break
        else:
            print("Geçersiz seçim!")


import calendar  # Gereken tek kütüphaneyi çağırıyoruz


def turkce_takvim():
    yil = int(input("Takvim yılını giriniz: "))
    cal = calendar.LocaleTextCalendar(0, "TURKISH")  # "TURKISH" yazarak Türkçe diline ayarlıyoruz
    cal.pryear(yil)


def kronometre():
    print("Kronometre çalışıyor...")
    input("Başlamak için ENTER tuşuna basın...")

    baslangic = time.time()

    while True:
        try:
            secim = input("Durdurmak için 'd', devam etmek için 'e' tuşuna basın: ")
            if secim == "d":
                bitis = time.time()
                sure = bitis - baslangic
                print(f"Geçen süre: {sure:.2f} saniye")
                break
            elif secim == "e":
                continue
            else:
                print("Geçersiz seçim!")
        except KeyboardInterrupt:
            bitis = time.time()
            sure = bitis - baslangic
            print(f"Geçen süre: {sure:.2f} saniye")
            break

    return ""


def zar_oyunu():
    i = 1
    while True:
        zar_1 = random.randint(1, 6)
        zar_2 = random.randint(1, 6)

        if zar_1 == 6 and zar_2 == 6:
            print("""Deneme {}:\t({},{}) *** """.format(i, zar_1, zar_2))
            time.sleep(2)
            break

        print("""Deneme {}:\t({},{}) """.format(i, zar_1, zar_2))
        i += 1
        time.sleep(0.5)

    print("""\n*** {}. denemede (6,6) geldi ***""".format(i))


# Amiral Battı Oyunu
def amiral_battı_oyunu():
    board = []
    sayac = 0
    puan = 250
    for i in range(5):
        board.append(["0"] * 5)

    def print_board(board):
        for satir in board:
            print(" ".join(satir))

    def rand(board):
        return randint(1, len(board) - 1)

    print("-" * 55)
    print("Amiral battı oyununa hoş geldiniz")
    print("-" * 55)
    print("Puanınız:", puan)
    print("-" * 55)
    print_board(board)
    gemi_satir = rand(board)
    gemi_sutun = rand(board)
    gemi1_satir = rand(board)
    gemi1_sutun = rand(board)
    gemi2_satir = rand(board)
    gemi2_sutun = rand(board)
    while True:
        if (gemi_satir == gemi1_satir and gemi_sutun == gemi1_sutun):
            gemi1_satir = rand(board)
            gemi1_sutun = rand(board)
            continue
        elif (gemi_satir == gemi2_satir and gemi_sutun == gemi2_sutun):
            gemi2_satir = rand(board)
            gemi2_sutun = rand(board)
            continue
        elif (gemi1_satir == gemi2_satir and gemi1_sutun == gemi2_sutun):
            gemi2_satir = rand(board)
            gemi2_sutun = rand(board)
            continue
        else:
            print("-" * 55)
            tahmin_satir = int(input("Satır giriniz: "))
            tahmin_sutun = int(input("Sütun giriniz: "))
            if (tahmin_satir == gemi_satir and tahmin_sutun == gemi_sutun) \
                    or (tahmin_satir == gemi1_satir and tahmin_sutun == gemi1_sutun) \
                    or (tahmin_satir == gemi2_satir and tahmin_sutun == gemi2_sutun):
                if board[tahmin_satir - 1][tahmin_sutun - 1] == "/":
                    print("-" * 55)
                    print("Zaten tahmin ettiniz")
                    print_board(board)
                    print(puan)
                else:
                    print("-" * 55)
                    print("Tebrikler gemiyi batırdınız!")
                    board[tahmin_satir - 1][tahmin_sutun - 1] = "/"
                    print("Puanınız:", puan)
                    print("-" * 55)
                    print_board(board)
                    sayac += 1
            else:
                if (tahmin_satir < 0 or tahmin_sutun < 0) or (tahmin_satir > 5 or tahmin_sutun > 5):
                    print("-" * 55)
                    print("Alan sınırları dışında değer girdiniz")
                elif board[tahmin_satir - 1][tahmin_sutun - 1] == "X":
                    print("-" * 55)
                    print("Zaten tahmin ettiniz")
                    print("-" * 55)
                    print_board(board)
                else:
                    print("-" * 55)
                    print("Vuramadınız")
                    board[tahmin_satir - 1][tahmin_sutun - 1] = "X"
                    puan -= 10
                    print("Puanınız:", puan)
                    print("-" * 55)
                    print_board(board)
                if sayac == 3:
                    print("-" * 55)
                    print("Tebrikler bütün gemileri batırdınız ve oyunu kazandınız")
                    print("-" * 55)
                    break


def liste_olusturucu():
    # boş bir To-Do listesi oluşturma
    to_do_list = []

    def add_task(to_do_list):
        task = input("Yapılacak görevi girin: ")
        to_do_list.append(task)
        print("Görev başarıyla eklendi!")

    # Listede bulunan görevleri gösteren fonksiyon
    def show_tasks(to_do_list):
        print("Yapılacak görevler: ")
        for task in to_do_list:
            print("- " + task)

    # Listeden görev silen fonksiyon
    def delete_task(to_do_list):
        task = input("Silmek istediğiniz görevi girin: ")
        if task in to_do_list:
            to_do_list.remove(task)
            print("Görev başarılıyla silindi.")
        else:
            print("Görev bulunamadı.")

    # Ana döngü
    while True:
        print("\nTo-Do List Uygulaması")
        print("1. Görev ekle")
        print("2. Görevleri Göster")
        print("3. Görev sil")
        print("4. Çıkış")
        choice = input("Seçiminiz (1/2/3/4): ")

        if choice == "1":
            add_task(to_do_list)
        elif choice == "2":
            show_tasks(to_do_list)
        elif choice == "3":
            delete_task(to_do_list)
        elif choice == "4":
            print("Uygulamadan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, Lütfen tekrar deneyin..")


# Basit Şifre Kırıcı
def sifre_kırıcı():
    print("- Unutmayın ki bu program basit bir şifre kırıcıdır ve bu tarz gelişmiş programlar yasal değildir.")
    print("- Ayrıca gelişmiş bir şifre kırıcı olmadığı gibi sorumluluk kabul edilmemektedir.")
    ozel_giris = input("Özel şifreyi giriniz: ")
    if ozel_giris == ozel_sifre:
        print("Şifre doğru!")

    else:
        print("Şifre yanlış!")
        exit()

    giris_ozel = input("Özel kodu giriniz: ")
    if kod == giris_ozel:
        print("Kod doğru, giriş yapabilirsiniz.")

    else:
        print("Kod yanlış!")
        exit()

    def crack_password(password, max_length):
        chars = """ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.:/*-_,;`\?=}])([{&%!½+$^#£é"' """
        attempts = 0

        for length in range(1, max_length + 1):
            for guess in itertools.product(chars,
                                           repeat=length):  # Tüm kombinasyonları denemek için itertools kullanılıyor
                attempts += 1
                guess = ''.join(guess)  # Şifre denemesini birleştir

                if guess == password:
                    return guess, attempts

        return None, attempts

    hedef_sifre = input(">> Kırılacak şifreyi girin: ")
    maksimum_uzunluk = int(input(">> Maksimum şifre uzunluğunu belirleyin: "))

    sonuc, deneme_sayisi = crack_password(hedef_sifre, maksimum_uzunluk)

    if sonuc:
        print(">> Şifre kırıldı!")
        print("Kırılan şifre:", sonuc)
        print("Deneme sayısı:", deneme_sayisi)
    else:
        print(">> Şifre kırılamadı.")


def sayı_tahmin_oyunu():
    rand = randint(1, 100)
    sayac = 0

    while True:
        sayac += 1
        sayi = int(input("1 ile 100 arasında değer girin (0 çıkış):"))
        if (sayi == 0):
            print("Oyunu iptal Ettiniz")
            break
        elif sayi < rand:
            print("Daha yüksek bir değer girin.")
            continue
        elif sayi > rand:
            print("Daha düşük bir sayı girin.")
            continue
        else:
            print("Rastgele seçilen sayı {0}!".format(rand))
            print("Tahmin sayınız {0}".format(sayac))


def asal_sayı_kontrol():
    sayı_bir = int(input("Bir sayı giriniz: "))
    asal = True

    if sayı_bir < 2:
        asal = False
    else:
        for i in range(2, int(sayı_bir ** 0.5) + 1):
            if sayı_bir % i == 0:
                asal = False
                break

    if asal:
        print(sayı_bir, "bir asal sayıdır.")
    else:
        print(sayı_bir, "bir asal sayı değildir.")


import datetime


def hızlı_yazma_test():
    print("- Lütfen 3 saniye sonra yazmaya başla!")

    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("Başla!")
    time.sleep(0.2)
    before = datetime.datetime.now()

    text = input("Bir şeyler yazın:")
    after = datetime.datetime.now()
    speed = after - before
    seconds = round(speed.total_seconds(), 2)
    letter_per_second = round(len(text) / seconds, 1)
    print("Yazdın: {} saniyede!".format(seconds))
    print("Bu kadar harf yazdın: {} .".format(letter_per_second))


def carpimtablosu():
    def carpim(i, j, r):
        if r != "E":
            result = str(i * j)
            if result == r:
                print("\t\t***** Doğru *****")
            else:
                print("\t!!! Yanlış cevap %s olacaktı" % result)
        else:

            secim()

    def basla(rng_1, rng_2):
        if rng_1 > 10:
            x = 10
        else:
            x = 5
        for i in range(0, x):
            for j in range(0, x):
                sayi_1 = randint(rng_1, rng_2)
                sayi_2 = randint(rng_1, rng_2)
                print("_" * 50, "\n")
                print("\t%d x %d kaça eşittir? (çıkış = E)" % (sayi_1, sayi_2))
                sonuc = input("sonuc >> ")
                carpim(sayi_1, sayi_2, sonuc)

                if i == 4 and j == 4:
                    print("\n *-- Bu bölüm bitti bir üst bölüme geçebilsiniz --*\n")
                    secim()

    def secim():
        print(" Hangi seviyeden başlamak istiyorsunuz (çıkış = E) ?\n")
        print("  1 - Kolay ")
        print("  2 - Orta Düzey")
        print("  3 - Zor")
        print("  4 - İleri Düzey\n")

        svy = input(" >> ")

        if svy == "1":
            basla(1, 6)

        elif svy == "2":
            basla(6, 12)

        elif svy == "3":
            basla(12, 25)

        elif svy == "4":
            basla(25, 100)

        else:
            print("- Çıkış yapılıyor..")

    if __name__ == '__main__':
        secim()


def tas_kagit_makas():
    secenekler = ["taş", "kağıt", "makas"]

    while True:
        # Kullanıcıdan seçim alınır
        kullanici_secimi = input("Taş, kağıt veya makas? (Çıkmak için 'q' tuşuna basın): ").lower()
        if kullanici_secimi == "q":
            break

        if kullanici_secimi not in secenekler:
            print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")
            continue

        # Bilgisayar rastgele seçim yapar
        bilgisayar_secimi = random.choice(secenekler)

        print("Bilgisayarın seçimi:", bilgisayar_secimi)

        # Kazanan belirlenir
        if kullanici_secimi == bilgisayar_secimi:
            print("Berabere!")
        elif (kullanici_secimi == "taş" and bilgisayar_secimi == "makas") or \
                (kullanici_secimi == "kağıt" and bilgisayar_secimi == "taş") or \
                (kullanici_secimi == "makas" and bilgisayar_secimi == "kağıt"):
            print("Tebrikler, kazandınız!")
        else:
            print("Maalesef, kaybettiniz!")


import time
import os
import platform


def zamanlayıcı():
    def temizle():
        if platform.system() == 'Linux' or platform.system() == 'Darwin':
            os.system('clear')
        else:
            os.system('cls')

    while True:
        zaman = time.localtime()
        yil = zaman[0]
        ay = zaman[1]
        gun = zaman[2]
        saat = zaman[3]
        dakika = zaman[4]
        saniye = zaman[5]

        time.sleep(1)
        temizle()

        print("""
            tarih: {}/{}/{}
            saat : {}:{}:{}
            """.format(gun, ay, yil, saat, dakika, saniye))
        sorum = input("Çıkış için 'Q' basınız. | Devam etmek için 'E' basınız. ")
        if sorum == "Q":
            print("Çıkış yapıldı.")
            break
        elif sorum == "E":
            continue
        else:
            print("Lütfen geçerli tuşa basın.")
            break


def kitle():
    boy = float(input("Boy (m):"))
    kilo = int(input("Kilo (kg):"))

    endeks = kilo / (boy * boy)

    if endeks <= 18:
        print("\n zayıf VKİ:{}".format(endeks))
    elif endeks > 18 and endeks <= 25:
        print("\n kilolu VKİ:{}".format(endeks))
    elif endeks > 25 and endeks <= 30:
        print("\n obez VKİ:{}".format(endeks))
    elif endeks > 30:
        print("\n ciddi obez VKİ:{}".format(endeks))


def destek_talebi():
    talep = input("Destek talebi oluşturmak istediğinizden emin misiniz? (Onayla/İptal): ")
    while True:
        if talep == "İptal":
            print("- Çıkış yapılıyor..")
            time.sleep(1)
            break

        elif talep == "Onayla":
            time.sleep(1)
            konu_gir = input("Talebinizin konusu nedir? ")
            içerik_gir = input("Talebinizi yazınız: ")
            print("- Kaydediliyor..")
            time.sleep(2)
            sayi_yaz = random.randint(10000, 1000000)
            print("Talep ID: ", sayi_yaz)
            print(
                "Yukarıdaki kod talep numaranızdır, e-posta yoluyla iletişime geçerseniz konuyu ve talebinizi yazınız ardından talep numaranızı yazınız.")
            time.sleep(10)
            print("- İşlem sonlandırıldı ve kaydedildi!")
            break

        else:
            print("Geçersiz karakter!")
            break


def linkler():
    print("SOSYAL MEDYA LİNKLERİMİZ:")
    print("İnstagram: https://www.instagram.com/mavioyun16")
    print("İnstagram Ekip: https://www.instagram.com/mavistudio16")
    print("Youtube: https://www.youtube.com/@mavioyun16")
    print("Youtube Ekip: https://www.youtube.com/@mavistudio16")
    print("Wepsite: https://mavioyun16.wixsite.com/mavi")
    print("Discord Sunucu: https://discord.gg/5Xj7xrG577")
    print("Steam Hesabı: https://steamcommunity.com/profiles/76561199231216216/")


def iletişim():
    while True:
        print("İLETİŞİM SEÇENEKLERİ:")
        print("1. E-Posta")
        print("2. Destek Talebi")
        print("3. Wepsite İletişim")
        print("4. Discord İletişim")
        print("5. Çıkış")

        soru_iletişim = input("Seçiminizi yapın: ")

        if soru_iletişim == "5":
            print("- Çıkış yapılıyor..")
            break

        elif soru_iletişim == "1":
            print("E-POSTA İLETİŞİM:")
            print("Ekip İletişim 7/24: mavistudio16@gmail.com")
            print("Kurucu/Geliştirici İletişim 7/24: mavigelistirici16.iletisim@gmail.com")
            print("- Mesajınızda konuyu ve talebi ayrıntılı bir şekilde yazınız.")
            time.sleep(6)
            break

        elif soru_iletişim == "2":
            print("Destek talebi komutu(destek talebi) bulunmaktadır, programa yönlendiriliyorsunuz..")
            time.sleep(8)
            destek_talebi()

        elif soru_iletişim == "3":
            print("Link: www.mavioyun16.wixsite.com/mavi")
            time.sleep(10)
            break

        elif soru_iletişim == "4":
            print("Linki: https://discord.gg/5Xj7xrG577")
            time.sleep(10)
            break
        else:
            print("Geçersiz karakter!")
            break


import speedtest


def test_internet_speed():
    while True:
        speed_soru = input("Testi başlatmak için 'E' çıkış için 'F' basınız.")
        if speed_soru == "F":
            print("- Çıkış yapılıyor..")
            time.sleep(2)
            break

        elif speed_soru == "E":
            print(
                "- Test yapılırken arkaplanda veya aktif kullandığınız pencereler (programlar) testin verimiliğini, doğruluğunu düşürebilir.")
            time.sleep(10)
            print(">> Test başlatılıyor..")
            time.sleep(3)
            try:
                st = speedtest.Speedtest()
                print(">>> İnternet hız testi yapılıyor...")
                download_speed = st.download() / 10 ** 6
                upload_speed = st.upload() / 10 ** 6
                print("İndirme hızı: {:.2f} Mbps".format(download_speed))
                print("Yükleme hızı: {:.2f} Mbps".format(upload_speed))
            except speedtest.SpeedtestException:
                print("Hız testi yapılırken bir hata oluştu.")

        else:
            print("Geçersiz karakter!")
            break


def yilan_oyunu():
    import pygame
    import random

    while True:
        soru_yilan = input("Oyuna başlamak için 'E' yazınız. (çıkış = Q): ")
        if soru_yilan == "Q":
            print("- Çıkış yapılıyor..")
            time.sleep(2)
            break
        elif soru_yilan == "E":
            time.sleep(1)

            # Pencere boyutları
            WIDTH = 800
            HEIGHT = 600

            # Renkler
            BLACK = (0, 0, 0)
            WHITE = (255, 255, 255)
            GREEN = (0, 255, 0)
            RED = (255, 0, 0)

            # Yılan boyutları
            BLOCK_SIZE = 20
            SNAKE_SPEED = 10

            # Oyun ekranını başlatma
            pygame.init()
            screen = pygame.display.set_mode((WIDTH, HEIGHT))
            clock = pygame.time.Clock()
            font = pygame.font.Font(None, 36)

            # Yılan oluşturma
            snake = [(WIDTH / 2, HEIGHT / 2)]
            snake_direction = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])

            # Yem oluşturma
            food = (random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE,
                    random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE)

            # Skor
            score = 0

            # Oyun döngüsü
            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP] and snake_direction != 'DOWN':
                    snake_direction = 'UP'
                elif keys[pygame.K_DOWN] and snake_direction != 'UP':
                    snake_direction = 'DOWN'
                elif keys[pygame.K_LEFT] and snake_direction != 'RIGHT':
                    snake_direction = 'LEFT'
                elif keys[pygame.K_RIGHT] and snake_direction != 'LEFT':
                    snake_direction = 'RIGHT'

                # Yılanın hareketi
                x, y = snake[0]
                if snake_direction == 'UP':
                    y -= BLOCK_SIZE
                elif snake_direction == 'DOWN':
                    y += BLOCK_SIZE
                elif snake_direction == 'LEFT':
                    x -= BLOCK_SIZE
                elif snake_direction == 'RIGHT':
                    x += BLOCK_SIZE
                snake.insert(0, (x, y))

                # Yılanın kendine çarpmasını kontrol etme
                if len(snake) > 1 and (x, y) in snake[1:]:
                    running = False

                # Yılanın ekranın dışına çıkmasını kontrol etme
                if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
                    running = False

                # Yılanın yemi yemesini kontrol etme
                if (x, y) == food:
                    food = (random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE,
                            random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE)
                    score += 1
                else:
                    snake.pop()

                # Ekranı temizleme
                screen.fill(BLACK)

                # Yılanı çizme
                for block in snake:
                    pygame.draw.rect(screen, GREEN, (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

                # Yemi çizme
                pygame.draw.rect(screen, RED, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))

                # Skoru gösterme
                score_text = font.render(f"SKOR: {score}", True, WHITE)
                screen.blit(score_text, (10, 10))

                # Ekranı güncelleme
                pygame.display.flip()
                clock.tick(SNAKE_SPEED)

            # Oyun döngüsünden çıktıktan sonra Pygame'i kapatma
            pygame.quit()

            print(f">> Oyun bitti! Skorun: {score}")


        else:
            print("Geçersiz karakter!")
            time.sleep(1)
            break


def sifre_olusturucu():
    while True:
        olusturma_soru = input("Şifre oluşturmak için 'E' basınız. (çıkış = Q): ")
        if olusturma_soru == "Q":
            print("- Çıkış yapılıyor..")
            time.sleep(2)
            break
        elif olusturma_soru == "E":
            print("Rastgele bir şifre oluşturuluyor..")
            time.sleep(4)
            import random
            import string

            uzunluk = int(input("Şifre uzunluğunu girin: "))
            karakterler = string.ascii_letters + string.digits + string.punctuation
            sifre = ''.join(random.choice(karakterler) for _ in range(uzunluk))
            print("Oluşturulan şifre:", sifre)
        else:
            print("Geçersiz karakter!")
            time.sleep(2)
            break


import hashlib


def metin_sifreleme():
    while True:

        text1 = input("Şifrelenecek metni yazınız. (çıkış = Q): ")
        if text1 == "Q":
            print("- Çıkış yapılıyor..")
            time.sleep(2)
            break
        else:
            hashed_text = hashlib.sha256(text1.encode()).hexdigest(),
            print("Şifrelenmiş Metin:", hashed_text)


import pyaudio
import wave
import threading


def ses_kayıt():
    def record_audio(duration, output_file):
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100

        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        print("Ses kaydı başladı...")

        frames = []
        stop_recording = threading.Event()

        def stop():
            input("Kaydı durdurmak için Enter tuşuna basın...")
            stop_recording.set()

        stop_thread = threading.Thread(target=stop)
        stop_thread.start()

        while not stop_recording.is_set():
            data = stream.read(CHUNK)
            frames.append(data)

        print("Ses kaydı tamamlandı.")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(output_file, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

    # Ses kaydını başlat
    duration = int(input("Kayıt süresini saniye cinsinden girin: "))
    output_file = input("Kaydedilecek dosya adını girin (örn. kayit.wav): ")

    record_audio(duration, output_file)


def url_video_indirme():
    while True:
        import requests

        def video_indir(url, hedef_dosya):
            response = requests.get(url, stream=True)
            with open(hedef_dosya, 'wb') as dosya:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        dosya.write(chunk)
            print("Video indirme tamamlandı.")

        # Video indirme örneği
        print("- Çıkış için 'Q' basınız.")
        video_url = input("Video URL'sini yazınız: ")
        if video_url == "Q":
            print("- Çıkış yapılıyor..")
            time.sleep(3)
            break
        hedef_dosya = input("Hedef dosyanın adını yazınız: ")
        if hedef_dosya == "Q":
            print("- Çıkış yapılıyor..")
            time.sleep(3)
            break

        video_indir(video_url, hedef_dosya)


def dosya_olusturma():
    import os

    def dosya_olustur(dosya_adi):
        try:
            with open(dosya_adi, 'w') as dosya:
                print("Dosya oluşturuldu:", dosya_adi)
        except Exception as e:
            print("Dosya oluşturma hatası:", str(e))

    def dosya_sil(dosya_adi):
        try:
            os.remove(dosya_adi)
            print("Dosya silindi:", dosya_adi)
        except Exception as e:
            print("Dosya silme hatası:", str(e))

    def metin_belgesi_olustur(dosya_adi, icerik):
        try:
            with open(dosya_adi, 'w') as dosya:
                dosya.write(icerik)
            print("Metin belgesi oluşturuldu:", dosya_adi)
        except Exception as e:
            print("Metin belgesi oluşturma hatası:", str(e))

    def metin_belgesi_sil(dosya_adi):
        try:
            os.remove(dosya_adi)
            print("Metin belgesi silindi:", dosya_adi)
        except Exception as e:
            print("Metin belgesi silme hatası:", str(e))

    while True:
        print("1. Dosya Oluştur")
        print("2. Dosya Sil")
        print("3. Metin Belgesi Oluştur")
        print("4. Metin Belgesi Sil")
        print("5. Çıkış")
        secim = input("İşlem seçin (1-5): ")

        if secim == '1':
            dosya_adi = input("Oluşturmak istediğiniz dosyanın adını girin: ")
            dosya_olustur(dosya_adi)
        elif secim == '2':
            dosya_adi = input("Silmek istediğiniz dosyanın adını girin: ")
            dosya_sil(dosya_adi)
        elif secim == '3':
            dosya_adi = input("Oluşturmak istediğiniz metin belgesinin adını girin: ")
            icerik = input("Metin belgesinin içeriğini girin: ")
            metin_belgesi_olustur(dosya_adi, icerik)
        elif secim == '4':
            dosya_adi = input("Silmek istediğiniz metin belgesinin adını girin: ")
            metin_belgesi_sil(dosya_adi)
        elif secim == '5':
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim!")


def kurallar_uyarı():
    while True:
        print("1. Kullanım Kuralları")
        print("2. Yasal Uyarı")
        print("3. Telif ve Gizlilik Politakası")
        print("4. Çıkış")
        soru2 = input("Seçiminizi yapınız(1-4): ")

        if soru2 == "4":
            print("- Çıkış yapılıyor..")
            time.sleep(2)
            break
        elif soru2 == "1":
            print("- Yapay zeka sohbeti ve sesli asistan kayıt altındadır.")
            print("- Küfür, argo, 'Maviland' veya ekibimize en ufak bir zararda perma ban alırsınız. (kalıcı ban)")
            print("- Yapay zekaya ters ve kasten verilen cevap (hatalar) ban sebebidir.")
            time.sleep(15)
            break
        elif soru2 == "3":
            print("- Yapay Zeka 'Mavi- X16' ile ilgili tüm haklar 'Maviland'a aittir.")
            print(
                "- Arka plan işlemleri ve kodları (yazılımı) Şirketimize aittir, Sızdırılma gibi bir durumda hukuki işlemler başlatılacaktır.")
            time.sleep(12)
            break
        elif soru2 == "2":
            print("- Yazılım şirketimize aittir, telif hakkı ve diğer haklar korunmaktadır.")
            time.sleep(10)
            break

        else:
            print("Geçersiz karakter, program kapatılıyor..")
            time.sleep(4)
            break


def version():
    while True:
        print(">> Sürüm kontrol ediliyor..")
        time.sleep(4)
        print("Sürüm: V1.0 DEMO ")
        break


def internet_kontrol():
    import socket
    try:
        socket.create_connection(("https://mavioyun16.wixsite.com/mavi", 80))
        return True
    except OSError:
        pass
    return False

    if internet_kontrol():
        print("İnternet bağlantısı var.")
    else:
        print("İnternet bağlantısı yok.")


def ip_dogrulama():
    import ipaddress
    ip_address = input("İP giriniz: ")

    try:
        ip = ipaddress.IPv4Address(ip_address)
        print("Geçerli bir IP adresi.")
    except ipaddress.AddressValueError:
        print("Geçerli bir IP adresi değil.")


import re


def eposta_dogrulama():
    def is_valid_email(email):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        match = re.match(pattern, email)
        return bool(match)

    eposta_dogrula = input("E-Posta giriniz: ")
    if is_valid_email(eposta_dogrula):
        print("Geçerli bir e-posta adresi.")
    else:
        print("Geçerli bir e-posta adresi değil.")


def arama():
    import webbrowser

    def search_google(query):
        search_url = f"https://www.google.com/search?q={query}"
        webbrowser.open(search_url)

    # Kullanıcıdan arama terimini alın
    search_term = input("Google'da aramak için yazın: ")

    # Google'da arama yap
    search_google(search_term)


def mayın_tarlası_oyunu():
    import random

    def create_board(size, num_mines):
        # Boş bir oyun tahtası oluştur
        board = [[' ' for _ in range(size)] for _ in range(size)]

        # Mayınları yerleştir
        mines = random.sample(range(size * size), num_mines)
        for mine in mines:
            row = mine // size
            col = mine % size
            board[row][col] = '*'

        return board

    def print_board(board):
        size = len(board)
        print('    ' + '   '.join(str(i) for i in range(size)))
        print('  ' + '+---' * size + '+')

        for i in range(size):
            print(i, end=' | ')
            print(' | '.join(board[i]), end=' |\n')
            print('  ' + '+---' * size + '+')

    def play_game():
        size = int(input("Oyun tahtasının boyutunu girin: "))
        num_mines = int(input("Mayın sayısını girin: "))

        board = create_board(size, num_mines)
        uncovered = [[' ' for _ in range(size)] for _ in range(size)]

        game_over = False

        while not game_over:
            print_board(uncovered)

            row = int(input("Satır seçin: "))
            col = int(input("Sütun seçin: "))

            if board[row][col] == '*':
                print("Mayına bastınız! Oyun bitti.")
                game_over = True
            else:
                count = 0
                for i in range(row - 1, row + 2):
                    for j in range(col - 1, col + 2):
                        if 0 <= i < size and 0 <= j < size and board[i][j] == '*':
                            count += 1
                uncovered[row][col] = str(count)

                if count == 0:
                    for i in range(row - 1, row + 2):
                        for j in range(col - 1, col + 2):
                            if 0 <= i < size and 0 <= j < size and uncovered[i][j] == ' ':
                                uncovered[i][j] = str(count)
                                # Recursive uncovering of adjacent cells
                                if i != row or j != col:
                                    play_game_recursive(board, uncovered, size, i, j)

                if all(' ' not in row for row in uncovered):
                    print("Tebrikler! Tüm alanları keşfettiniz.")
                    game_over = True

    def play_game_recursive(board, uncovered, size, row, col):
        count = 0
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if 0 <= i < size and 0 <= j < size and board[i][j] == '*':
                    count += 1
        uncovered[row][col] = str(count)

        if count == 0:
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    if 0 <= i < size and 0 <= j < size and uncovered[i][j] == ' ':
                        uncovered[i][j] = str(count)
                        if i != row or j != col:
                            play_game_recursive(board, uncovered, size, i, j)

    play_game()


def xox_oyunu():
    import random

    # Oyun tahtası
    board = [' ' for _ in range(9)]

    # Kazanma kombinasyonları
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Yatay kombinasyonlar
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Dikey kombinasyonlar
        [0, 4, 8], [2, 4, 6]  # Çapraz kombinasyonlar
    ]

    # Oyun tahtasını çizme
    def draw_board():
        print('-----------')
        for i in range(3):
            row = '| '.join(board[i * 3:(i * 3) + 3])
            print(f'| {row} |')
            print('-----------')

    # Oyuncunun hamlesini almak
    def get_player_move():
        while True:
            move = input('Sıra sende (1-9): ')
            try:
                move = int(move) - 1
                if move in range(9) and board[move] == ' ':
                    return move
                else:
                    print('Geçersiz hamle. Lütfen tekrar dene.')
            except ValueError:
                print('Geçersiz hamle. Lütfen tekrar dene.')

    # Bilgisayarın hamlesini yapmak
    def get_computer_move():
        available_moves = [i for i, spot in enumerate(board) if spot == ' ']
        for move in available_moves:
            board_copy = board[:]
            board_copy[move] = 'O'
            if is_winner(board_copy):
                return move

        for move in available_moves:
            board_copy = board[:]
            board_copy[move] = 'X'
            if is_winner(board_copy):
                return move

        corners = [0, 2, 6, 8]
        available_corners = [corner for corner in corners if corner in available_moves]
        if len(available_corners) > 0:
            return random.choice(available_corners)

        if 4 in available_moves:
            return 4

        edges = [1, 3, 5, 7]
        available_edges = [edge for edge in edges if edge in available_moves]
        if len(available_edges) > 0:
            return random.choice(available_edges)

    # Kazananı kontrol etme
    def is_winner(board):
        for combo in winning_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
                return True
        return False

    # Oyun döngüsü
    def play_game():
        draw_board()
        while True:
            if ' ' not in board:
                print('Oyun berabere bitti.')
                break

            player_move = get_player_move()
            board[player_move] = 'X'
            draw_board()

            if is_winner(board):
                print('Tebrikler! Kazandın.')
                break

            computer_move = get_computer_move()
            board[computer_move] = 'O'
            draw_board()

            if is_winner(board):
                print('Üzgünüm, kaybettin!')
                break

    # Oyunu başlatma
    play_game()


def copy_program():
    def yaziyi_kopyala(yazi, uzunluk):
        try:
            kopya = yazi * uzunluk
            return kopya

        except TypeError:
            print("Hata: 'yazi' bir dize (string) olmalıdır.")
            return None

    while True:
        yazi = input("Kopyalamak istediğiniz metni yazınız (çıkmak için 'Q' giriniz): ")
        if yazi == 'Q':
            print("- Çıkış yapılıyor..")
            time.sleep(2)
            break

        uzunluk = int(input("Kopya uzunluğunu yazınız: "))

        kopya_yazi = yaziyi_kopyala(yazi, uzunluk)
        if kopya_yazi:
            print(f"Kopya: {kopya_yazi}")


import folium
from geopy.geocoders import Nominatim


def gps_harita():
    while True:
        gps_soru = input("Devam etmek için 'ENTER' basınız | Çıkış için 'Q'")
        if gps_soru == "Q":
            print("- Çıkış yapılıyor..")
            time.sleep(3)
            break
        elif gps_soru == "":
            time.sleep(2)

            def get_coordinates(location):
                geolocator = Nominatim(user_agent="gps_map_app")
                location = geolocator.geocode(location)
                return (location.latitude, location.longitude)

            def main():
                location_name = input("Lütfen konum adını girin: ")
                coordinates = get_coordinates(location_name)
                map_osm = folium.Map(location=coordinates, zoom_start=15)
                folium.Marker(location=coordinates, popup=location_name).add_to(map_osm)

                map_osm.save("gps_map.html")
                print("Harita oluşturuldu ve 'gps_map.html' adında kaydedildi.")

            if __name__ == "__main__":
                main()

        else:
            print("Geçersiz karakter!")


def afk():
    while True:
        print("AFK PROGRAMI")
        print("0. 5dk")
        print("1. 15dk")
        print("2. 30dk")
        print("3. 60dk")
        print("4. 120dk")
        print("5. 300dk")
        print("6. Çıkış")

        print(
            "NOT: AFK başlatıldıktan sonra programdan çıkış yapamazsınız, AFK süreniz bitince '6' yazarak programı kapatabilirsiniz.")
        print("DİPNOT: Süre boyunca programdan çıkılamaz fakat kapatılabilir.")

        afk_soru = input("Seçiminizi yapın: ")
        if afk_soru == "6":
            print("- Çıkış yapılıyor..")
            time.sleep(3)
            break
        elif afk_soru == "0":
            print("5 Dakikalık AFK başlatıldı!")
            time.sleep(300)
        elif afk_soru == "1":
            print("15 Dakikalık AFK başlatıldı!")
            time.sleep(900)
        elif afk_soru == "2":
            print("30 Dakikalık AFK başaltıldı!")
            time.sleep(1800)
        elif afk_soru == "3":
            print("1 Saatlik AFK başlatıldı!")
            time.sleep(3600)
        elif afk_soru == "4":
            print("2 Saatlik AFK başlatıldı!")
            time.sleep(7200)
        elif afk_soru == "5":
            print("5 Saatlik AFK başlatıldı!")
            time.sleep(18000)
        else:
            print("Geçersiz karakter!")


def id_mavi():
    while True:
        print("SEÇENEKLER:")
        print("0. ID Sorgula")
        print("1. ID Oluştur")
        print("2. ID Hakkında")
        print("3. Çıkış")

        secim0 = int(input("Seçiminizi yapın. (0-3): "))
        if secim0 == 3:
            print("- Çıkış yapılıyor...")
            time.sleep(2)
            break
        elif secim0 == 1:
            id_oluştur = random.randint(100000, 10000000)
            print("Yeni 'Mavi ID'niz: ", id_oluştur)
            time.sleep(4)
        elif secim0 == 0:
            print("ID'niz: ", id_oluştur)
            break
        elif secim0 == 2:
            print("- 'Mavi ID' sisteme girerken güvenlik ve kayıt için oluşturulan numaradır.")
            break
        else:
            print("Geçersiz karakter'")


def server():
    server_pasword = "MAVİ.16_dv!:Dc'#681<"
    while True:
        server_login = input("Server Login: ")
        if server_login == server_pasword:
            print(">>> Server Onayı Bekleniyor...")
            time.sleep(5)
            print(">>> Server Giriş Yapılıyor...")
            time.sleep(2)
            print("MAVİ-X16 SERVER'A HOŞ GELDİNİZ!")
            time.sleep(1)
            print("!!! : server info gelişim aşamasındadır.")

        elif server_login == "exit":
            break

        else:
            print(">>> Server Reddedildi!")
            break


import os
import hashlib


def antivirüs():
    while True:
        atvr = input("Programa başlamak için 'E' basınız. (Çıkış = Q): ")
        if atvr == "Q":
            print("- Çıkış yapılıyor..")
            time.sleep(3)
            break
        elif atvr == "E":
            print("Z-16 ANTİVİRÜS BAŞLATILIYOR..")
            time.sleep(4)

            def calculate_md5(file_path):
                with open(file_path, 'rb') as file:
                    content = file.read()
                    md5_hash = hashlib.md5(content).hexdigest()
                    return md5_hash

            def scan_file(file_path):
                md5_hash = calculate_md5(file_path)

                # Zararlı imzaları kontrol etmek için bir veritabanı kullanılır
                if md5_hash in malicious_signatures:
                    print(f"Potansiyel zararlı dosya bulundu: {file_path}")
                    # Burada dosya silme, karantinaya alma veya temizleme gibi işlemler gerçekleştirilebilir
                else:
                    print(f"Güvenli dosya: {file_path}")

            def scan_directory(directory_path):
                for root, dirs, files in os.walk(directory_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        scan_file(file_path)

            def login():
                password1 = "69._4aQ/x=?."  # Örnek şifre

                while True:
                    user_password = input("Programı başlatmak için Antivirüs Şifresini giriniz: ")

                    if user_password == password1:
                        print("Giriş başarılı!")
                        break
                    else:
                        print("Hatalı şifre. Tekrar deneyin.")

            # Zararlı imzaların bir listesi
            malicious_signatures = [
                "e8dc4081b13434b45189a720b77b6818",  # Örnek zararlı imza 1
                "4b9f741b1c22c86038a61de3d32c5c21"  # Örnek zararlı imza 2
            ]

            # Giriş yap
            login()

            # Taranacak klasörü belirtin
            directory_path = input("Taramak istediğiniz klasör yolunu girin: ")

            # Klasörü tara
            scan_directory(directory_path)

            # Çıkış yap
            input("Çıkış yapmak için Enter tuşuna basın...")


while True:

    kullanici_girdisi = input("Mavi-X16: Size nasıl yardımcı olabilirim? ")
    if kullanici_girdisi.lower() == 'x':
        print("- Çıkış yapılıyor...")
        time.sleep(2)
        exit()
