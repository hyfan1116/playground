import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt

trainsize = 80000
featuresize = 5 # 36 # start from 0
labelindex = 10 # 37-1

teststart = 80000
testsize = 20000 # 20000
testend = teststart+testsize

w = 50 # 80
sen = 0.50

data = pd.read_csv("output10.csv")
dataNewIndexList = []
X = data.iloc[0:trainsize,0:featuresize]
Y = data.iloc[0:trainsize,labelindex]

# NB
clf = GaussianNB()
#w = 50 # set in the beginning
W = Y[:]*w+1 
clf.fit(X,Y,sample_weight=W)
score_ein = clf.score(X,Y)

Xtest = data.iloc[teststart:testend,0:featuresize]
Ytest = data.iloc[teststart:testend,labelindex]
#XtestSmall = data.iloc[teststart:teststart+10,0:featuresize]

Ypred = clf.predict(Xtest)
# probability, score
Yprob = clf.predict_proba(Xtest)[:,0]

#Yfin = np.array((Yprob, Ypred))
Yfin = np.column_stack((Yprob, Ytest))
Yfins = Yfin[np.argsort(Yfin[:,0])]
'''
# gains and lift
listG = [0]
decsum = 0
for dec in range(0,testsize,testsize/10):
	decsum += sum(Yfins[dec:dec+testsize/10,1])
	listG.append(decsum)
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
'''
# ROC
listRocx = []
listRocy = []
for seni in range(0,100,5):
	sen = seni*0.01
	Ypred = [(y<sen)*1 for y in Yprob] # sen: sensitivity

	score_eout = clf.score(Xtest,Ytest)

	cm = confusion_matrix(Ytest,Ypred,labels=[0,1])
	[[tn,fp],[fn,tp]] = cm
	an = tn+fp
	ay = fn+tp
	pn = tn+fn
	py = fp+tp
	sens = tp*1.0/ay
	mspec = 1 - tn*1.0/an
	listRocx.append(mspec)
	listRocy.append(sens)
	
plt.figure(3)
plt.plot(listRocx,listRocy)
plt.plot([x*0.1 for x in range(11)],[x*0.1 for x in range(11)])
plt.show()

'''
print "########## Result ##########"
print "Score","Ein",score_ein,"Eout",score_eout
print "Weight:",w,"FeatureSize:",featuresize,"Sen:",sen

print "Accuracy:", (tp+tn)*1.0/testsize
print "Sensitivity:",tp*1.0/ay
print "Specificity:",tn*1.0/an
print "Prevalence:",ay*1.0/testsize,"Response:",ay,"Testsize:",testsize

print "Confusion Matrix:"
print cm
'''