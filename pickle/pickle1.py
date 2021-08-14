import pickle

data1 = {'a': 1, 'b': 2, 'c': 3}
data2 = [1, 2, 3]
data3 = "stringOfText"

output = open('data.pkl', 'wb')
pickle.dump(data1, output)
pickle.dump(data2, output)
pickle.dump(data3, output)

output.close()