__author__ = 'Omer'

import numpy as np
import csv
import pyglet
from sklearn import svm
from scipy import signal
import time
import threading
import os
import shutil


class findParameters():

    def __init__(self, *args):
        gamma=0.1
        C=1
        self.clf = svm.SVC(gamma=gamma, C=C)
    '''
    for values of gamma
        for values of C
            learn(gamma, C)
            evaluate
            store in matrix

    plot matrix
    '''

    def learn(self):

        #self.EvaluationButton.setEnabled(True)
        subject_name = str(self.subjectList.currentItem().text())
        # import data and tags
        data = {}
        data_cut = {}
        tag = {}
        # success = 0

        i = 1
        if os.path.isdir('D:\Project\Records'):
            folder_path_1 = 'D:\Project\Records'
        else:
            folder_path_1 = 'C:\Project\Records'
        subfolder_path = folder_path_1 + "\\" + subject_name
        data_size = len(os.listdir(subfolder_path))
        for cFile in os.listdir(subfolder_path):
            name = os.path.splitext(cFile)[0]
            with open(subfolder_path+'\\'+cFile, 'rb') as csvfile:
                reader = csv.reader(csvfile)
                data[i] = []
                data_cut[i] = []
                j = 0
                for row in reader:
                   ''' j += 1
                    if j > 129:
                        break
                    elif j > 346:
                       break'''
                   data[i].extend(row)
            data[i] = [float(x) for x in data[i]]
            if '13_' in name:
                tag[i] = 13
            elif '10_' in name:
                tag[i] = 10
            elif '15_' in name:
                tag[i] = 15
            elif '20_' in name:
                tag[i] = 20
            elif '25_' in name:
                tag[i] = 25
            elif '30_' in name:
                tag[i] = 30
            elif '16_' in name:
                tag[i] = 16
            elif '37_' in name:
                tag[i] = 37
            elif '11_' in name:
                tag[i] = 11
            elif '9_' in name:
                tag[i] = 9
            elif '23_' in name:
                tag[i] = 23
            i += 1
            csvfile.close()

        # learn the data
        learn = []
        # test = [] # TODO - if necessary check the classification before running the actual test

        # print test
        X, y = [data[i] for i in range(1, data_size)], [tag[k] for k in range(1, data_size)]
        self.clf.fit(X, y)

    # Evaluate
    def eval(self):
        subject_name = str(self.subjectList_2.currentItem().text())
        # import data and tags
        data = {}
        data_cut = {}
        tag = np.zeros(60)
        # success = 0
        i = 0
        if os.path.isdir('D:\Project\Data'):
            folder_path_1 = 'D:\Project\Data'
        else:
            folder_path_1 = 'C:\Project\Data'
        subfolder_path = folder_path_1 + "\\" + subject_name
        data_size = len(os.listdir(subfolder_path))
        for cFile in os.listdir(subfolder_path):
            name = os.path.splitext(cFile)[0]
            with open(subfolder_path+'\\'+cFile, 'rb') as csvfile:
                reader = csv.reader(csvfile)
                data[i] = []
                data_cut[i] = []
                j = 0
                for row in reader:
                   data[i].extend(row)
            data[i] = [float(x) for x in data[i]]
            if '13_' in name:
                tag[i] = 13
            elif '10_' in name:
                tag[i] = 10
            elif '15_' in name:
                tag[i] = 15
            elif '20_' in name:
                tag[i] = 20
            elif '25_' in name:
                tag[i] = 25
            elif '30_' in name:
                tag[i] = 30
            elif '16_' in name:
                tag[i] = 16
            elif '37_' in name:
                tag[i] = 37
            elif '11_' in name:
                tag[i] = 11
            elif '9_' in name:
                tag[i] = 9
            elif '23_' in name:
                tag[i] = 23
            i += 1
            csvfile.close()

        #X, y = [data[i] for i in range(1, data_size)], [tag[k] for k in range(1, data_size)]
        freq = [self.upFreq.text().toFloat()[0], self.downFreq.text().toFloat()[0], self.rightFreq.text().toFloat()[0], self.leftFreq.text().toFloat()[0]]
        test=np.zeros(60)
        for w in range(0, data_size-1):
            result= self.clf.decision_function(data[w])[0, :]
            votes=np.zeros(4)
            p=0
            for i in range(4):
                for j in range(i+1,4):
                    if result[p]>0:
                        votes[i]+=1
                    else:
                        votes[j]+=1
                    p+=1
            final_result=np.argmax(votes)
            if np.max(votes)==3:#or (np.max(votes)==2 and Connector.result==self.clf.classes_[final_result]):
                #print self.clf.classes_
                #print final_result
                test[w]=self.clf.classes_[final_result]
            else:
                test[w]=0
            unfiltered_test=final_result

        TP=np.zeros(4)
        FP=np.zeros(4)
        TN=np.zeros(4)
        FN=np.zeros(4)
        UTP=np.zeros(4)
        UFP=np.zeros(4)
        UTN=np.zeros(4)
        UFN=np.zeros(4)

        for i in range(4):
            correct=np.sum(test == tag)
            TP[i]=np.sum(test[tag == freq[i]] == freq[i])
            FP[i]=np.sum(test[tag != freq[i]] == freq[i])
            TN[i]=np.sum(test[tag != freq[i]] != freq[i])
            FN[i]=np.sum(test[tag == freq[i]] != freq[i])
            ucorrect=np.sum(unfiltered_test == tag)
            UTP[i]=np.sum(unfiltered_test[tag == freq[i]] == freq[i])
            UFP[i]=np.sum(unfiltered_test[tag != freq[i]] == freq[i])
            UTN[i]=np.sum(unfiltered_test[tag != freq[i]] != freq[i])
            UFN[i]=np.sum(unfiltered_test[tag == freq[i]] != freq[i])

        acc = (np.sum(TP)+np.sum(TN))/(np.sum(TP)+np.sum(FP)+np.sum(TN)+np.sum(FN))
        uacc = (np.sum(UTP)+np.sum(UTN))/(np.sum(UTP)+np.sum(UFP)+np.sum(UTN)+np.sum(UFN))

        print "unfiltered correct=" + str(ucorrect)
        print "UTP=" + str(TP)
        print "UTN=" + str(TN)
        print "total unfiltered accuracy=" + str(uacc)
        print "correct=" + str(correct)
        print "TP=" + str(TP)
        print "TN=" + str(TN)
        print "total accuracy=" + str(acc)





