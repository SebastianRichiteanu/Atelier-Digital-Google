print("Acesta este cursul al 2-lea!")

name = "Ana"
if name:
    print(name)
    print(type(name))
else:
    print(names)  # this is an inline comment
    print("Nu avem definit niciun nume")

first_person = {"Name": "John"}
second_person = {"Name": "John"}

if first_person is second_person:
    print("they are the same")
else:
    print("they are not the same")

if first_person == second_person:
    print("they are the same")
else:
    print("they are not the same")

my_str = "Ana are mere"
print(my_str[2])

print(ord('a'))

my_str2 = r'Owner\'s \n\tmanual'  # escape

print(my_str2)

print("""fjkdjkafjklda
fda
fd
af
da


f""")

name = 'Ion'
age = 18

msg = "{} has {} years".format(name, age)
print(msg)

msg_2 = f"{name} has {age + 2} years"
print(msg_2)

l = [1, 2, 3, "Ana are mere", True, False, None, [4, 5, 6]]

print(l[2])

l[2] = '99'

print(l[2])

inventar = ["faina", "drojdie", "apa", "sare"]
for item in inventar:
    print(item)

for index, value in enumerate(inventar):
    print(f'{value} la pozitia {index}')

print(inventar[-1])
print(inventar[len(inventar)-1])

l1 = [2, 3, 0, 9]
l2 = [12, [13, 10], 19]


l1.extend(l2)
print(l1)

my_dict = {1: "Home", 2: "Office", 3: "Restaurant"}
for key, value in my_dict.items():
    print(f"{key} => {value}")

print(my_dict.get(4, "Nu exista cheia"))

# v = my_dict[4]

l1 = [1, 2, 2, 3]
l2 = [1, 9, 2, 0]

s1 = set(l1)
s2 = set(l2)

print(list(s1 & s2))
