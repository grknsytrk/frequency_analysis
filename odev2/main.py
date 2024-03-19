import frequency_analysis

text = "Türkiye, bazı tarihi nedenlerle uygulayık yaşamına geç girmiş, büyük kültürel kopukluklar yaşamış bir ülke. Bu geçmişten sanıcalarla da çok uzun sürmüştür. Türk şair ve yazarları, bu büyük kopukluğun derin acılarını, yüzlerini yaşayor hâlâ. Bugün Türk edebiyatında haddinden fazla bireycilik ve son derece köksüz bir lirizm görülcek bir olgudur. Şiirde yaşadığı soyarif ve yazarlarımız. Halbuki bireycilik de topluluculuk gibi kültürel kökler oluştan temellere dayanır."
text = frequency_analysis.lower(text)

for i in [100, 1000, 10000]:
    print(f"\\nİlk {i} karakter için frekans analizi:")
    sozluk = frequency_analysis.frequency(text[:i])
    for harf, (sayac, oran) in sorted(sozluk.items()):
        print(f"{harf}: kullanım sayısı: {sayac}, kullanım oranı: {oran}%")
        
frequency_analysis.yazdir()