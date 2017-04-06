import numpy as np
import pandas as pd
#from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

trainsize = 80000
featuresize = 5 # 36 # start from 0
labelindex = 10 # 37-1

teststart = 80000
testsize = 20000 # 20000
testend = teststart+testsize

w = 50 # 80

data = pd.read_csv("output10.csv")
dataNewIndexList = []
X = data.iloc[0:trainsize,0:featuresize]
Y = data.iloc[0:trainsize,labelindex]

'''
# extract same amount of entires
train1,train0 = 0,0
for i in range(trainsize):
	if int(data.iloc[i,labelindex])==1:
		dataNewIndexList.append(i)
		train1+=1

for i in range(trainsize):
	if int(data.iloc[i,labelindex])==0:
		dataNewIndexList.append(i)
		train0+=1
		if train0>=train1:
			break

dataNew = data.iloc[dataNewIndexList,:]

# test x & y
X = dataNew.iloc[:,0:featuresize]
Y = dataNew.iloc[:,featuresize]
'''

# NB
#clf = GaussianNB()
#w = 50 # set in the beginning
#W = Y[:]*w+1 
#clf.fit(X,Y,sample_weight=W)
#GaussianNB(priors=None)

# SVM
clf = SVC()
W = Y[:]*w+1 
clf.fit(X, Y, sample_weight=W)

cright = 0	# count of correct predictions
cright1 = 0	# count of correct predictions of responded customers
cresp = 0	# count of responded customers

for i in range(teststart,testend):
	pred = clf.predict(data.iloc[i,range(featuresize)].values.reshape(1,-1))[0]
	ans = int(data.iloc[i,labelindex])
	if pred == ans:
		cright += 1
		if pred == 1:
			cright1 += 1
	if ans == 1:
		cresp += 1
		
print "########## Result ##########"
print "Accuracy:", cright*1.0/testsize
print "Bottomline:", 1-cresp*1.0/testsize
print "Weight:",w,"FeatureSize",featuresize
print "AccuracyOf1:", cright1*1.0/cresp
print "AccuracyOf0:", (cright-cright1)*1.0/(testsize-cresp)
print "Number:",testsize,"NumberOfResponse:",cresp