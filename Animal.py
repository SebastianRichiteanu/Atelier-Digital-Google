class Animal(object):
    def __init__(self, age):
        self.years = age
        self.name = None

    def get_age(self):
        return self.years

    def get_name(self):
        return self.name

    def set_age(self, new_age):
        self.years = new_age

    def set_name(self, new_name=""):
        self.name = new_name

    def __str__(self):
        return f"animal: {self.name}, {self.years}"


class Dog(Animal):
    def speak(self):
        print("Ham Ham")

    def __str__(self):
        return f"dog: {self.name}, {self.years}"


class Person(Animal):
    id = 1

    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = set()
        self.tag = Person.id
        Person.id += 1

    def get_friends(self):
        return self.friends

    def add_friend(self, new_friend):
        if new_friend:
            self.friends.add(new_friend)

    def __str__(self):
        return f"Person: {self.tag} - {self.name}, {self.years}"


cat = Animal(4)

print("Cat's age: ", cat.get_age())
print("Cat's name: ", cat.get_name())
cat.set_name("Tom")
cat.size = 'Big'
print(cat.size)

print('--------------')
lassie = Dog(10)
lassie.set_name("Lassie")
print(lassie)
lassie.speak()

print('--------------')
ion = Person("Ion", 21)
maria = Person("Maria", 18)

print(ion)
print(maria.get_friends())
maria.add_friend("Ion")
maria.add_friend("George")
print(maria.get_friends())
print(maria)

print(Person.id)
