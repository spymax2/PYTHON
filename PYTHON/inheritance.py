class Human:
    def james(self):
        print("can walk")

    def tom(self):
        print("can run")


# kk = Human()
# print(kk.james())
# print(kk.tom())




class Racoon(Human):
    def racoon(self):
        print("can smile")



mm = Racoon()
print(mm.tom())
print(mm.racoon())
print(mm.james())
