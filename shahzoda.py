faylnomi = 'matn.txt'
with open("faylnomi", "r") as fayl:
    matn = fayl.read()

print(matn)

print("____________________")

fayl_pi = 'pi_million_digits.txt'
with open("fayl_pi", "r") as pi:
    pi_million_digits = pi.read()
    if '23092007 ' in pi_million_digits:
        print("sizning tug'ilgan yilingiz pi ichida bor ekan")
    else:
        print("kechirasiz sizning tug'ilgan yilingiz pi ichida yo'q ekan")


import pickle

pi_yangi = pi_million_digits
yangi_fayl = "Pi_yangi.txt"
with open(yangi_fayl, "wb") as fayl:
    pickle.dump(pi_yangi, fayl)

filename = "malumotlar.txt"

while True:
    data = input("malumot kiriting (chiqish uchun 'exit' deb yozing): ")
    if data.lower() == "exit":
        print("dastur tugadi.")
        break

    with open(filename, "a") as file:
        file.write(data + "\n")

    print("malumot faylga saqlandi.\n")