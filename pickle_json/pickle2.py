import pickle

pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)
print(data1)

data2 = pickle.load(pkl_file)
print(data2)

data3 = pickle.load(pkl_file)
print(data3)
