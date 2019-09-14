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
print("++++++++++++++++++++++++++++++++++++++++++ ONE FIELD AT A TIME +++++++++++++++++++++++++++++++++++++++++++++++++++")
print()

names = ['name', 'age', 'pay', 'job']
values = ['Tammy L', 79, 222222, 'ret']
print(list(zip(names, values)))
tammy = dict(zip(names, values))
print(tammy)


