A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))   # обычный словарь
A1 = range(10)  # обычный range
A2 = sorted([i for i in A1 if i in A0]) # [] - тут все дело в словаре((((
A3 = sorted([A0[s] for s in A0])        # обходим словарь по ключам и хватаем значения A0[s] по ключам
A4 = [i for i in A1 if i in A3]     # [1, 2, 3, 4, 5]
A5 = {i:i*i for i in A1}    # генератор-коллекции (словаря). пара {ключ:ключ в квадрате}
A6 = [[i,i*i] for i in A1]  # генератор-коллекции (списка списков).
A7 = [i if i%2 else 0 for i in A1 if 2 < i < 8]
print(','.join(str(j**2) for j in range(10))) # 0,1,4,9,...