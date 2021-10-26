from statistics import mean

data = list(range(1, 21))
avg = mean(data)
above_avg = list(filter(lambda x: x > avg, data))
below_avg = list(filter(lambda x: x < avg, data))
print(data)
print(avg)
print(above_avg)
print(below_avg)
