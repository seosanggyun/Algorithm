import itertools


N = 13
factory_number = []
for i in range(N):
    factory_number += [str(i)]

print(factory_number)

factory_orders = itertools.permutations(factory_number)
print(len(list(factory_orders)))

