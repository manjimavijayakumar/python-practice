import random
print(random.random())
print(random.randint(2,10))
print(random.randrange(2,15,6))
items=['apple','cherry','mango']
print(random.choice(items))
random.shuffle(items)
print(items)