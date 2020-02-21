import pandas as pd


dataset = 'C:/Users/Lee Pollok/Downloads/student/student-por.csv'
d = pd.read_csv(dataset, sep=';')
print(len(d))

d['pass'] = d.apply(lambda row: 1 if (row['G1']+row['G2']+row['G3']) >= 35 else 0, axis=1)
d = d.drop(['G1', 'G2', 'G3'], axis=1)
print(d.head())
