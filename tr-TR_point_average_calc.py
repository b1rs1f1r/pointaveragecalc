sayılar=0
notlar=[]

ders_sayısı=int(input("Kaç dersiniz var?: "))

for x in range(ders_sayısı):
	veri=int(input("{}. not: ".format(x+1)))
	sayılar+=veri
	notlar+=[veri]

print("Girdiğiniz notlar: ", *notlar)
print("Not ortalamanız: ", sayılar/ders_sayısı)