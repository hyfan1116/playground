
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
#from sklearn.ensemble import RandomForestClassifier
#from sklearn.svm import SVC

TRAINSIZE = 1000
FEATURESIZE = 15
LABELINDEX = 37
TESTINDEX = 68072
TESTSTART = 60000
TESTSIZE = 500

data = pd.read_csv("output.csv")
#x = data.iloc[0:TRAINSIZE,1:FEATURESIZE]
#y = data.iloc[0:TRAINSIZE,LABELINDEX]
#w = y[:]*1000+1
#w = np.array([1000 if i == 1 else 1 for i in y])
#print x
#print y
#print w

list = []
count = 0
for i in range(50000):
	if int(data.iloc[i,LABELINDEX]) == 1:
		list.append(i)
		count += 1
	if count >=1000:
		break
for i in range(50000, 51000):
	list.append(i)

x = data.iloc[list,1:FEATURESIZE]
y = data.iloc[list,LABELINDEX]

clf = DecisionTreeClassifier()
#clf = RandomForestClassifier(n_estimators=10)
#clf = SVC()
#clf.fit(x, y, w)
clf.fit(x, y)


xtest = data.iloc[TESTSTART:TESTSIZE,1:FEATURESIZE]

cright = 0
cresp = 0
#for i in range(TRAINSIZE,TRAINSIZE+TESTSIZE):
for i in range(TESTSTART,TESTSTART+TESTSIZE):
	pred = clf.predict(data.iloc[i,range(1,FEATURESIZE)].values.reshape(1,-1))[0]
	ans = int(data.iloc[i,LABELINDEX])
	if pred == ans:
		cright += 1
		if pred == 1:
			print i
	if ans == 1:
		cresp += 1

print "Accuracy:", cright*1.0/TESTSIZE
print "Bottomline:", 1-cresp*1.0/TESTSIZE
