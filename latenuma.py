b = 1 

for i in range(2,10):
    print(i)
    
while b == 1:
    a = int(input("Masukkan Nilai : "))

    if a > 100:
        print("Nilai Tidak Valid")
    elif a >= 90:
        print("Mantap")
    else:
        print("Gagal")

  
    b = int(input("Apakah anda ingin mengulang lagi? Jika iya ketik 1 : "))

for i in range(2,10):
    print(i)

array = ["Elvan", "Kamil", "Hafid", "Ridho", "Pedro"]
array.append("Nur C")
array.remove("Pedro")
array.insert(2, "Nur C")
print(array)

for i in array:
    print(i)

arr = ["apel", "Monyet", 2, 3.14]
print(arr)

for i in arr:
    print(i)

for i in range(0,3):
  print("MONYET", i)
  for j in range(0,3):
    print(" SAPI", j)
    for k in range(0,3):
      print("--BADAK", k)

for i in range(0,10,2):
  print("Ke-", i)
  if i > 6 :
    print("Wait", i)
    print("")
    break

for j in range(0,10):
  if j == 7:
    continue
  print(j)


b = 1

for i in range(2,10):
    print(i)

while b == 1:
    a = int(input("Masukkan Nilai : "))

    if a > 100:
        print("Nilai Tidak Valid")
    elif a >= 90:
        print("Mantap")
    else:
        print("Gagal")


    b = int(input("Apakah anda ingin mengulang lagi? Jika iya ketik 1 : "))







a = True

while a:
  print("a")
  a = False

def tambah(a,b,c):
  print(a+b+c)

for i in range(2,10):
  tambah(i,i+5,0)
tambah(1,2,0)
tambah(10,2,0)


i=0
while i <= 10:
  print("*" * i)
  i += 1



i=10
while i >= 0:
  print("*" * i)
  i -= 1


n = 10

for i in range(1, n+1):
 
    print(" " * (n - i), end="")
  
    print("*" * (2*i - 1))




