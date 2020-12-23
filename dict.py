##dict
cat = {}
print(cat)
cat = {'name':'Tom','color':'grey','age':5, }
del cat['age']
cat['food'] = 'fish'
cat['salary'] = 50
print(cat,cat['name'])
print("cat's name is "
    + cat['name'])
print("""cat's color is
    """ + cat['color'])
print(cat.items())
print(cat.keys())
for key, value in cat.items():
    print("\nKey:" + key)
    print("Value:" + str(value))
for key in sorted(cat.keys()):
    print("\nKey:" + key)
for key in cat:
    print("\nKey:" + key)
if 'name' in cat.keys():
    print ('cat has name')
cat['age'] = 50
for value in cat.values():
    print("\nValue:" + str(value))
print("*******************")
for value in set(cat.values()):
    print("\nValue:" + str(value))
cats = [cat,cat,cat]
for cat in cats:
    print(cat)
cat['food'] = ['fish','mouse']
animal = {'cat':cat,'dog':cat}
print(cat)
print(animal)
name = "Hello:"
name +=input("input your name:")
print(name+"!")

