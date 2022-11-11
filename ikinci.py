#control flow
#akışı kontrol et

#a=3 
#b=5 

# # a,b=3,5

# #code block
# #
# if a>b:
#     print("a b'den büyük")
# # else:  #diğer ihtimal
# #     print("a b'den büyük değil....")

# elif a<b:
#     print("a b'den küçük")
# elif a==b:            #2 eşit lazım
#     print("a b'ye eşit")



# #blok nesnesi başladı ise kesinlikle altında girintli bekler 

# # if 4<1:
# #     print("Bu doğru bir durum!")

# degisken_adi=5 
# #int - integer -tam sayı tipli bir değişken
# print(type(degisken_adi))

# kesir=3/7
# #float - kesir tipli bir değişken
# print(type(kesir))

# metin = "metin tipinde"
# #str - string metin tipli bir değişken
# print(type(metin))

# x="5" #str
# y=5 #int
# z=5.0 #float

# # x==y eşit değil
# # y==z eşit

# t=False
# #bool - boolean - Doğru yalnış tipli bir değişken
# print(type(t))
# #Doğru yalnış tipi değeri ilk harfı büyük yazılır


# a=100
# b=" bir daha yaramazlık yapmayacağım \n"
# print(a*b)



# a= 5
# b= " dünya"
# c= str(a) +b
# print(c)


# z="55.2"
# x="34"
# print(float(z)+int(x))



# t="True"
# print(bool(t))


# t=0
# print(t==False)
# p=12
# print(p==True)

# import random
# rasgele = random.randrange(1,10)


# # kul_veri = input("1 ve 10 arası rasgele sayı giriniz: ")
# # if kul_veri == str(rasgele):
# #     print("Tebrikler sayıyı buldunuz!!!")
# # else:
# #     print("Bilgisayarın tuttuğu sayı", rasgele)
# #     print("Sizin gönderiniz sayı", kul_veri)
# #     print("Tekrar deneyiniz")


# # Bir den fazla şart bulunan durumlar

# if 3>2 and 2>1:
#     print("İki şart da doğru")
# if 3>=2 and 3<=1 and 3<4 and 3!=4:
#     print("tüm şartlar doğru")

# print(True and True)
# print(1 and 1)
# print(False and False)
# print(0 and 0)
# print(True and False)
# print(1 and 0)
# print(False and True)
# print(0 and 1)


# print(True or True)
# print(1 or 1)
# print(False or False)
# print(0 or 0)
# print(True or False)
# print(1 or 0)
# print(False or True)
# print(0 or 1)

# import math

# vize =int(input("Vize sonuçunu giriniz: "))
# final_icin_gerekli_not = (50-0.4*vize)/0.6
# print("Final için almanız gereken not: " , math.ceil(final_icin_gerekli_not))

import math

vize =int(input("Vize sonuçunu giriniz: "))
if vize<50:
    final_icin_gerekli_not = (50-0.4*vize)/0.6
    print("Final için almanız gereken not: " , math.ceil(final_icin_gerekli_not))
else:
    print("Final için almanız gereken not: 50")

