import random
#215150309111002 Dimas Fariz Nabalah

class Karakter:
    def __init__(self, name, hp, attack):
        self._name = name
        self._hp = hp
        self._attack = attack

    def memukul(self, musuh):
        musuh.setHp(musuh.getHp() - self._attack)
        print(self._name + " memukul " + musuh.getName() + ". HP " + musuh.getName() + ": " + str(musuh.getHp()))
        if musuh.getHp() <= 0:
            print(musuh.getName() + " sudah kalah")

    def getName(self):
        return self._name

    def getHp(self):
        return self._hp

    def setHp(self, hp):
        self._hp = hp

class KarakterKebal(Karakter):
    def __init__(self, name, hp, attack):
        self._name = name
        self._hp = hp
        self._attack = attack

    #override
    def setHp(self, hp):
        self._hp = 9999999

class Party():
    def __init__(self, name=1):
        self._name = name
        #self._hp = hp
        #self._attack = attack
        self._anggota = []

    def tambahAnggota(self, name):
        self._anggota.append(name)

    def serang(self, musuh):
        print("[ {} menyerang {}!!! ]".format(self._name, musuh._name))
        for i in self._anggota:
            if i._hp <= 0:
                print(i._name + " Aduh!!!...")
            else:
                i.memukul(random.choice(musuh._anggota))
        print("")




        #musuh.setPartyHp(musuh.getPartyHp() - self._attack)
        #print(self._name + " memukul " + musuh.getName() + ". HP " + musuh.getName() + ": " + str(musuh.getHp()))
        #if musuh.getPartyHp() <= 0:
        #    print(musuh.getPartyName() + " sudah kalah")

#    def getPartyName(self):
#        return self._name

#    def getPartyHp(self):
#        return self._hp

#    def setPartyHp(self, hp):
#        self._hp = hp


    #Lengkapi kode program pada class Party sehingga dapat berjalan sesuai ilustrasi pada slide.

partyA = Party()
doraemon = Karakter("Doraemon", 60, 12)
batman = Karakter("Batman", 90, 18)
partyA.tambahAnggota(doraemon)
partyA.tambahAnggota(batman)

partyB = Party()
ultraman = Karakter("Ultraman", 100, 20)
upin = Karakter("Upin", 30, 7)
spongebob = Karakter("Spongebob", 20, 3)
partyB.tambahAnggota(ultraman)
partyB.tambahAnggota(upin)
partyB.tambahAnggota(spongebob)

partyA.serang(partyB)
partyB.serang(partyA)

