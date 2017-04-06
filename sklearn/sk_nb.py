import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt


featuresize = 36 # 35 # start from 0
labelindex = 36 # 35

w = 50 # 80
sen = 0.50


data = pd.read_csv("output.csv")
train,test = train_test_split(data, test_size=0.2)
testsize = len(test)

X = train.iloc[:,0:featuresize]
Y = train.iloc[:,labelindex]

# NB
clf = GaussianNB()
#w = 50 # set in the beginning
W = Y[:]*w+1 
clf.fit(X,Y,sample_weight=W)
score_ein = clf.score(X,Y)

Xtest = test.iloc[:,0:featuresize]
Ytest = test.iloc[:,labelindex]
#XtestSmall = data.iloc[teststart:teststart+10,0:featuresize]

Ypred = clf.predict(Xtest)
Yprob = clf.predict_proba(Xtest)[:,0] # probability, score

# gains and lift
Yfin = np.column_stack((Yprob, Ytest))
Yfins = Yfin[np.argsort(Yfin[:,0])]

listG = [0]
decsum = 0
for dec in range(0,testsize,testsize/10):
	decsum += sum(Yfins[dec:dec+testsize/10,1])
	listG.append(decsum)
	if len(listG)>10:
		break	
total = listG[-1]
listG = [x*1.0/total for x in listG]
listA = [x*0.1 for x in range(11)]
listL = [listG[i]/listA[i] for i in range(1,11)]
listAL = [1.0 for i in range(1,11)]
plt.figure(1)
plt.plot(listG)
plt.plot(listA)
plt.figure(2)
plt.plot(listL)
plt.plot(listAL)
plt.show()

score_eout = clf.score(Xtest,Ytest)

cm = confusion_matrix(Ytest,Ypred,labels=[0,1])
[[tn,fp],[fn,tp]] = cm
an = tn+fp
ay = fn+tp
pn = tn+fn
py = fp+tp

print "########## Result ##########"
print "Score","Ein",score_ein,"Eout",score_eout
print "Weight:",w,"FeatureSize:",featuresize,"Sen:",sen

print "Accuracy:", (tp+tn)*1.0/testsize
print "Sensitivity:",tp*1.0/ay
print "Specificity:",tn*1.0/an
print "Prevalence:",ay*1.0/testsize,"Response:",ay,"Testsize:",testsize

print "Confusion Matrix:"
print cm