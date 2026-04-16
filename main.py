class avto:
    def __init__(self, model, rang, korobka, narh, kilometr=0):
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narh = narh
        self.kilometr = kilometr

    def get_info(self):
        return f"{self.model}, {self.rang}, {self.korobka}, {self.narh}$, {self.kilometr}km"

    def update_km(self, km):
        if km >= self.kilometr:
            self.kilometr = km
        else:
            print("kilometrni kamaytirib bo'maydi")


class avtosalon:
    def __init__(self, nomi, manzil):
        self.nomi = nomi
        self.manzil = manzil
        self.avtolar = []

    def add_avto(self, avto):
        self.avtolar.append(avto)

    def get_avtolar(self):
        return [avto.get_info() for avto in self.avtolar]

# avtolar yaratamiz
avto1 = avto("nexia 3", "oq", "avtomat", 12000)
avto2 = avto("malibu", "qora", "avtomat", 200000, 100)

# kilometr yangilash
avto2.update_km(160)

# avtosalon yaratish
salon = avtosalon("GM avtosalon", "Xorazm")

salon.add_avto(avto1)
salon.add_avto(avto2)

for avto in salon.get_avtolar():
    print(avto)

print(dir(avto1))

print(avto1.__dict__)

print(dir(avto))