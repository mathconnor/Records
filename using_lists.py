bob = ['Bob Smith', 42, 30000, 'software']
sue = ['Sue Jones', 45, 40000, 'hardware']

# fetch name, pay
# print((f"Bob's first name: {bob[0]}", f"Sue's salary: {sue[2]}"))
print((bob[0], sue[2]))

# What is Bob's last name?
print(bob[0].split()[-1])

# Give Sue a 25% raise
sue[2] *= 1.25
print(sue)

print()

# refernce in list of lists
people = [bob, sue]
for person in people:
    print(person)

print()

# print just the last names and give everyone a 20% raise
for person in people:
    print(person[0].split()[-1])
    print("Before raise...")
    print(person)
    person[2] *= 1.2
    print("After raise...")
    print(person)

print()

# collect all pay (list comprehension)
pays = [person[2] for person in people]
print(f"List of salaries: {pays}")

print()

# collect all pay (map and lambda)
pays = map((lambda x: x[2]), people)
print(f"List of salaries: {list(pays)}")

# add Tommy Boy
people.append(["Tom", 50, 0, None])
print(f"The number of people now: {len(people)}")
print(f"The name of the person in last position of the people list: {people[-1][0]}")
print(f"The list of people now: {people}")

print()
print("+++++++++++++++++++++++++++++++++++++++++++++FIELD LABELS++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print()

NAME, AGE, PAY = range(3)
bob = ['Bob Smith', 42, 30000, 'software']
print(bob[NAME])
print((PAY, bob[PAY]))

print()

bob = [['name', 'Bob Smith'], ['age', 42], ['pay', 10000]]
sue = [['name', 'Sue Jones'], ['age', 45], ['pay', 20000]]
people = [bob, sue]

for person in people:
    print((f"name: {person[0][1]}", f"pay: {person[2][1]}"))

print()

# collect names
print([f"name: {person[0][1]}" for person in people])

print()
print()

# fetcher function
def field(record, label):
    for (fname, fvalue) in record:
        if fname == label:
            return fvalue


print(field(bob, 'name'))
print(field(sue, 'pay'))
