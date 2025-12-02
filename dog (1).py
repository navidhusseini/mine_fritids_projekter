
class Dog():
    """Et ultrasimpelt forsøg på at simulere en hund"""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("En ny hund er skabt! Den hedder " + self.name.title() + ". ")
        print("Den er " + str(self.age) + " år gammel.\n ")

    def goe(self):
        print(self.name.title() + " siger: VOV VOV")

    def sit(self):
        print(self.name.title() + " sitter nu. ")


minhund1 = Dog('willie', 6)
minhund2 = Dog('lucy', 3)

print(minhund1 == minhund2)

minhund1.goe()
minhund2.goe()
minhund2.sit()
minhund2.age = 12
print(minhund2.age)