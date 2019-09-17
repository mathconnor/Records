# Examples all from Learning Python, Lutz

bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}

print((bob['name'], sue['pay']))

print(bob['name'].split()[-1])

sue['pay'] *= 1.1
print(sue['pay'])

print()
print("++++++++++++++++++++++++++++++++++++++++++ PASS SETS TO DICTS +++++++++++++++++++++++++++++++++++++++++++++++++++")
print()

bob = dict(name='Bob Smith', age=42, pay=30000, job='dev')
sue = dict(name='Sue Jones', age=45, pay=40000, job='hdw')

print(bob)
print(sue)


print()
print("++++++++++++++++++++++++++++++++++++++++++ ONE FIELD AT A TIME +++++++++++++++++++++++++++++++++++++++++++++++++++")
print()

tom = {}
tom['name'] = 'Tommy Boy'
tom['age'] = 50
tom['pay'] = 0
tom['job'] = None

print(tom)

print()
print("++++++++++++++++++++++++++++++++++++++++++ ZIP LISTS +++++++++++++++++++++++++++++++++++++++++++++++++++")
print()

names = ['name', 'age', 'pay', 'job']
values = ['Tammy L', 79, 222222, 'ret']
print(list(zip(names, values)))
tammy = dict(zip(names, values))
print(tammy)


print()
print("++++++++++++++++++++++++++++++++++++++++++ INIT EMPTY DICT +++++++++++++++++++++++++++++++++++++++++++++++++++")
print()

fields = ['name', 'age', 'pay', 'job']
record = dict.fromkeys(fields, '?')
print(record)

print()
print("++++++++++++++++++++++++++++++++++++++++++ LISTS OF DICTS +++++++++++++++++++++++++++++++++++++++++++++++++++")
print()

print(f"Bob: {bob}")
print(f"Sue: {sue}")

people =[bob, sue]
for person in people:
    print(person['name'], person['pay'], sep=', ')

for person in people:
    if person['name'] == 'Sue Jones':
        print(person['pay'])

print()
print("++++++++++++++++++++++++++++++++++++++++++ LISTS COMP ('SQL-LIKE') +++++++++++++++++++++++++++++++++++++++++++++++++++")
print()

print([rec['name'] for rec in people if rec['age'] >= 45])
print([(rec['age']**2 if rec['age'] >= 45 else rec['age']) for rec in people ])

G = ((rec['name']**2 if rec['age'] >= 45 else rec['age']) for rec in people)
print(G.__next__())
