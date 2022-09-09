#Rumus luas persegi
print ("\n1.luas persegi")
sisi = int(input("masukan nilai sisi"))
luas_p = sisi * sisi

print ("luas persegi adalah", luas_p)

#Rumus luas jajar genjang
print ("\n2.luas jajar genjang")
alas = int(input("masukan nilai alas"))
tinggi =int(input("masukan nilai tinggi"))
luas_j = alas * tinggi

print ("luas jajar genjang adalah", luas_j)

#luas persegi panjang
print ("\n3.luas persegi panjang")
panjang = int(input("masukan nilai panjang"))
lebar = int(input("masukan nilai lebar"))
luas_pp = panjang * lebar

print ("luas persegi panjang adalah", luas_pp)

#luas segitiga
print ("\n4.luas segitiga")
alas = int(input("masukan nilai alas"))
tinggi = int(input("masukan nilai tinggi"))
luas_s = 1/2 * alas * tinggi

print ("luas segitiga", luas_s)

#luas lingkaran
print ("\n5.luas lingkaran")
phi = 22/7
r = int(input("masukan nilai r")) 
luas_l = phi * r * r

print ("luas lingkaran", luas_l)