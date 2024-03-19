def frequency(text):
    sozluk = {}
    for char in text:
        if char.isalpha():
            if char in sozluk:
                sozluk[char] += 1
            else:
                sozluk[char] = 1

    toplam_harf_sayisi = sum(sozluk.values())
    sozluk = oran(sozluk, toplam_harf_sayisi)
    return sozluk

def oran(sozluk, toplam_harf_sayisi):
    for harf, sayac in sozluk.items():
        sozluk[harf] = (sayac, (sayac / toplam_harf_sayisi) * 100)
    return sozluk

def lower(text):
    ceviri_tablo = str.maketrans("çğıöüâşÇĞIÖÜÂŞ", "cgiouasCGİOUAS")
    text.translate(ceviri_tablo).lower()
    return text
    
def yazdir():
    print("Gürkan Soytürk\n211220039\nHello World!")
