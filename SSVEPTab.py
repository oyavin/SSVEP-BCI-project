from PyQt4 import Qt, QtGui, QtCore
from BlinkingWidget import BlinkingWidget
from PyQt4.QtCore import pyqtSlot, QPointF
from PyQt4.QtGui import QPixmap
# from scipy import fftpack, signal
# from matplotlib import pylab as plt
import Connector
from Cursor import CheckeredArrowGrid
from frmSSVEPTab import Ui_SSVEPTab
import matplotlib.pyplot as plt
import numpy as np
import csv
from sklearn import svm
from scipy import signal
import time
import threading
import os
import shutil
import Tkinter as tk
import PyQt4.Qwt5 as Qwt
import pygame as pg

class SSVEPTab(QtGui.QWidget, Ui_SSVEPTab):

    def __init__(self, *args):
        QtGui.QWidget.__init__(self, *args)
        self.setupUi(self)

        self.parent = None
        self.disco_win = CheckeredArrowGrid(self)  # DiscoWindow(self)
        # self.decision_thread = threading.Timer(0.05, lambda: self.decide())  # TODO test this number

         # CheckeredArrowGrid(self) # TODO copy one of the forms and use it to create UI for DiscoWindow
        self.disco_win.__init__(self)
        self.disco_win.setWindowTitle('Subject Window')
        self.disco_win.setWindowIcon(QtGui.QIcon('app_icon.png'))
        self.refresh_list()
        self.refresh_list_2()
        self.clf = svm.SVC(gamma=0.2, C=5.5) #,decision_function_shape=None) #, probability=True)
        self.decisiontimer = QtCore.QTimer()

        self.upFreq.setText(str(11))
        self.downFreq.setText(str(13))
        self.rightFreq.setText(str(20))
        self.leftFreq.setText(str(17))
        self.chosen_freq_and_harmony=[11,13,17,20,22,26,34,40]

        #self.EvaluationButton.setEnabled(False)

        #plot
        self.DFTPlot.setCanvasBackground(Qt.Qt.white)
        self.DFTPlot.CurveSignal = Qwt.QwtPlotCurve("DFT")
        self.DFTPlot.CurveSignal.attach(self.DFTPlot)
        self.DFTPlot.CurveSignal.setPen(Qt.QPen(Qt.Qt.blue))
        self.plot_status=1
        self.plotlabels=['Freeze Plot', 'Plot']
        self.axis = [i for i in range(128*4)]

        self.status = 0
        self.buttonLabels = ['Activate', 'Disable']
        self.recordButton.setEnabled(False)
        self.update()  # get frequencies from ui
        self.Y = np.zeros((128*3))
        self.d = np.zeros((128*5))
        self.av = np.zeros((128*3))
        self.w = np.zeros((128*3))
        self.signal_rec_i = np.zeros((128*3))
        self.signal_rec_1 = np.zeros((128*3))
        self.signal_rec = np.zeros((14, (128*60)))
        self.n = 0
        self.search_flag=0

        self.upWidget.pixmap_black=self.disco_win.upWidget.pixmap_black=QPixmap("new_arrow_up.png")
        self.downWidget.pixmap_black=self.disco_win.downWidget.pixmap_black=QPixmap("new_arrow_down.png")
        self.leftWidget.pixmap_black=self.disco_win.leftWidget.pixmap_black=QPixmap("new_arrow_left.png")
        self.rightWidget.pixmap_black=self.disco_win.rightWidget.pixmap_black=QPixmap("new_arrow_right.png")
        self.rightWidget.point=QPointF(50.0, 0.0)
        self.downWidget.point=QPointF(0.0, 40.0)
        self.disco_win.rightWidget.point=QPointF(70.0, 0.0)
        self.disco_win.downWidget.point=QPointF(0.0, 60.0)

        self.upWidget.pixmap_green=self.disco_win.upWidget.pixmap_green=QPixmap("checkered_arrow_3_up_G.png")
        self.downWidget.pixmap_green=self.disco_win.downWidget.pixmap_green=QPixmap("checkered_arrow_3_down_G.png")
        self.leftWidget.pixmap_green=self.disco_win.leftWidget.pixmap_green=QPixmap("checkered_arrow_3_left_G.png")
        self.rightWidget.pixmap_green=self.disco_win.rightWidget.pixmap_green=QPixmap("checkered_arrow_3_right_G.png")
        pixmap_M = QPixmap("cookiemonster.png")
        self.disco_win.pic_label.setPixmap(pixmap_M)
        pixmap_C = QPixmap("cookie.png")
        self.disco_win.midlabel.setPixmap(pixmap_C)
        pixmap_d = QPixmap("new_arrow_down_op.png")
        self.disco_win.downlabel.setPixmap(pixmap_d)
        pixmap_r = QPixmap("new_arrow_right_op.png")
        self.disco_win.rightlabel.setPixmap(pixmap_r)
        pixmap_l = QPixmap("new_arrow_left_op.png")
        self.disco_win.leftlabel.setPixmap(pixmap_l)
        pixmap_u = QPixmap("new_arrow_up_op.png")
        self.disco_win.uplabel.setPixmap(pixmap_u)

        root = tk.Tk()
        self.screen_width = root.winfo_screenwidth()-self.disco_win.grid_widget.geometry().width()
        self.screen_height = root.winfo_screenheight()-self.disco_win.grid_widget.geometry().height()-55

        p = self.disco_win.palette()
        p.setColor(self.disco_win.backgroundRole(),QtCore.Qt.white)
        self.disco_win.setPalette(p)

        self.p_up=self.disco_win.upWidget.palette()
        self.p_up.setColor(self.disco_win.upWidget.backgroundRole(),QtCore.Qt.white)
        self.disco_win.upWidget.setPalette(self.p_up)

        self.p_left=self.disco_win.leftWidget.palette()
        self.p_left.setColor(self.disco_win.leftWidget.backgroundRole(),QtCore.Qt.white)
        self.disco_win.leftWidget.setPalette(self.p_left)

        self.p_right=self.disco_win.rightWidget.palette()
        self.p_right.setColor(self.disco_win.rightWidget.backgroundRole(),QtCore.Qt.white)
        self.disco_win.rightWidget.setPalette(self.p_right)

        self.p_down=self.disco_win.downWidget.palette()
        self.p_down.setColor(self.disco_win.downWidget.backgroundRole(),QtCore.Qt.white)
        self.disco_win.downWidget.setPalette(self.p_down)

        QtCore.QObject.connect(self.activateButton, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("flicker()"))
        QtCore.QObject.connect(self.record_Eval_Button, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("record_Eval()"))
        QtCore.QObject.connect(self.EvaluationButton, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("Evaluation()"))
        QtCore.QObject.connect(self.RunButton, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("Runplot()"))
        QtCore.QObject.connect(self.updateButton, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("update()"))
        QtCore.QObject.connect(self.ShowButton, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("findParameters()"))
        QtCore.QObject.connect(self.recordButton, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("record()"))
        # QtCore.QObject.connect(self.ShowButton, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("DFT()"))
        QtCore.QObject.connect(self.discoButton, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("toggle_disco_win()"))
        QtCore.QObject.connect(self.refreshButton, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("refresh_list()"))
        QtCore.QObject.connect(self.refreshButton_2, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("refresh_list_2()"))
        QtCore.QObject.connect(self.trainButton, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("train()"))
        QtCore.QObject.connect(self.disco_win.SButton, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("train()"))
        QtCore.QObject.connect(self.decisiontimer, QtCore.SIGNAL("timeout()"), self, QtCore.SLOT("decide()"))
        #QtCore.QObject.connect(self.greenback, QtCore.SIGNAL("timeout()"), self, QtCore.SLOT("whiteback()"))

    @pyqtSlot()
    def toggle_disco_win(self):
        if self.disco_win.opened:
            self.disco_win.hide()
            self.disco_win.opened = False
        else:
            self.disco_win.show()
            self.disco_win.opened = True
        self.update_toggle_text()

    def update_toggle_text(self):
        if self.disco_win.opened:
            self.discoButton.setText('Hide Cursor')
        else:
            self.discoButton.setText('Show Cursor')

    @pyqtSlot()
    def flicker(self):
        self.status = 1 - self.status
        self.activateButton.setText(self.buttonLabels[self.status])

        if self.status:
            self.recordButton.setEnabled(True)
            self.upWidget.flicker()
            self.downWidget.flicker()
            self.leftWidget.flicker()
            self.rightWidget.flicker()

            if self.disco_win.opened:
                self.disco_win.upWidget.flicker()
                self.disco_win.downWidget.flicker()
                self.disco_win.leftWidget.flicker()
                self.disco_win.rightWidget.flicker()
        else:
            self.recordButton.setEnabled(False)
            self.upWidget.stop()
            self.downWidget.stop()
            self.leftWidget.stop()
            self.rightWidget.stop()
            if self.disco_win.opened:
                self.disco_win.upWidget.stop()
                self.disco_win.downWidget.stop()
                self.disco_win.leftWidget.stop()
                self.disco_win.rightWidget.stop()

    @pyqtSlot()
    def update(self):
        self.flicker()  # enables change of frequencies during flicker
        self.upWidget.frequency = self.upFreq.text().toFloat()[0]/2  # [0] because returned object is tuple
        self.leftWidget.frequency = self.leftFreq.text().toFloat()[0]/2
        self.rightWidget.frequency = self.rightFreq.text().toFloat()[0]/2
        self.downWidget.frequency = self.downFreq.text().toFloat()[0]/2

        self.disco_win.upWidget.frequency = self.upWidget.frequency
        self.disco_win.downWidget.frequency = self.downWidget.frequency
        self.disco_win.rightWidget.frequency = self.rightWidget.frequency
        self.disco_win.leftWidget.frequency = self.leftWidget.frequency

        self.flicker()

    @pyqtSlot()
    def DFT(self, eeg_signal, eeg_signal_rec):
        self.signal = eeg_signal
        self.n = len(self.Y)
        self.Dc_off_o1 =  eeg_signal[6, :]# -  eeg_signal[6, :].mean(axis=0, keepdims=True).mean(axis=-1, keepdims=True) #rmoving Dc
        self.Dc_off_o2 =  eeg_signal[7, :] -  eeg_signal[7, :].mean(axis=0, keepdims=True).mean(axis=-1, keepdims=True)

        self.Dc_off_p7 =  eeg_signal[5, :] -  eeg_signal[5, :].mean(axis=0, keepdims=True).mean(axis=-1, keepdims=True) #rmoving Dc
        self.Dc_off_p8 =  eeg_signal[8, :] -  eeg_signal[8, :].mean(axis=0, keepdims=True).mean(axis=-1, keepdims=True)

        b, a = signal.butter(8, 0.12, 'high')
        #self.w=eeg_signal[10, :]
        #self.o1_o2= (eeg_signal[9, :] + eeg_signal[10, :])/2
        self.av_o1 = signal.filtfilt(b, a, self.Dc_off_o1, axis=-1)
        self.av_o2 = signal.filtfilt(b, a, self.Dc_off_o2, axis=-1)
        #self.Y = np.fft.fft(self.av)/self.n
        self.w_o1, self.Pxx_den_o1 = signal.welch(self.av_o1, 128, nperseg=128)
        self.w_o2, self.Pxx_den_o2 = signal.welch(self.av_o2, 128, nperseg=128)

        self.av_p7 = signal.filtfilt(b, a, self.Dc_off_p7, axis=-1)
        self.av_p8 = signal.filtfilt(b, a, self.Dc_off_p8, axis=-1)
        #self.Y = np.fft.fft(self.av)/self.n
        self.w_p7, self.Pxx_den_p7 = signal.welch(self.av_p7, 128, nperseg=128)
        self.w_p8, self.Pxx_den_p8 = signal.welch(self.av_p8, 128, nperseg=128)

        zero_vec=np.zeros(65,)
        #self.Y = abs(self.Y)
        self.Pxx_den = np.maximum(zero_vec, self.Pxx_den_o1-self.Pxx_den_p8)
        '''
        for j in range(0,14,1):
            if j==0:
                self.filt_noise=signal.filtfilt(b, a, eeg_signal[j, :], axis=-1)
                self.f_noise,self.Pxx_noise=signal.welch(self.filt_noise, 128, nperseg=128)
                self.sum_noise=self.Pxx_noise
            elif j!=6 & j!=7:
                self.filt_noise=signal.filtfilt(b, a, eeg_signal[j, :], axis=-1)
                self.f_noise,self.Pxx_noise=signal.welch(self.filt_noise, 128, nperseg=128)
                self.sum_noise+=self.Pxx_noise
                '''
        self.Pxx_den_nc=abs(self.Pxx_den)# + self.Pxx_den_o2)/2
        #self.Y_fitted = [self.Y[i+1] for i in range(256, 347)]

        j=0
        temp=np.zeros(8)
        for i in self.chosen_freq_and_harmony:
            '''
            temp[j]=self.Pxx_den_nc[i-1]
            temp[j+1]=self.Pxx_den_nc[i]
            temp[j+2]=self.Pxx_den_nc[i+1]
            j+=3
            '''
            temp[j]=self.Pxx_den_nc[i]
            j+=1

        self.Pxx_den=temp
        #
        self.DFTPlot.updateAxes()
        if self.plot_status==0:
            if self.radioRaw.isChecked():
                self.DFTPlot.setAxisAutoScale(self.DFTPlot.yLeft)
                self.DFTPlot.setAxisAutoScale(self.DFTPlot.xBottom)
                self.DFTPlot.setAxisTitle(self.DFTPlot.yLeft, '[microVolt]')
                self.DFTPlot.setAxisTitle(self.DFTPlot.xBottom, '[sample]  ([sec/128])')
                self.DFTPlot.CurveSignal.setData(self.axis, eeg_signal[6, :])
                self.DFTPlot.replot()
            elif self.radioDC.isChecked():
                self.DFTPlot.setAxisAutoScale(self.DFTPlot.yLeft)
                self.DFTPlot.setAxisAutoScale(self.DFTPlot.xBottom)
                self.DFTPlot.setAxisTitle(self.DFTPlot.yLeft, '[microVolt]')
                self.DFTPlot.setAxisTitle(self.DFTPlot.xBottom, '[sample]  ([sec/128])')
                self.DFTPlot.CurveSignal.setData(self.axis, self.Dc_off_o1)
                self.DFTPlot.replot()
            elif self.radioHPF.isChecked():
                self.DFTPlot.setAxisAutoScale(self.DFTPlot.yLeft)
                self.DFTPlot.setAxisAutoScale(self.DFTPlot.xBottom)
                self.DFTPlot.setAxisTitle(self.DFTPlot.yLeft, '[microVolt]')
                self.DFTPlot.setAxisTitle(self.DFTPlot.xBottom, '[sample]  ([sec/128])')
                self.DFTPlot.CurveSignal.setData(self.axis, self.av_o1)
                self.DFTPlot.replot()
            elif self.radioFinal.isChecked():
                self.DFTPlot.setAxisScale(self.DFTPlot.yLeft, 0, 2.0, 0)
                self.DFTPlot.setAxisScale(self.DFTPlot.xBottom, 0, 65, 5)
                self.DFTPlot.setAxisTitle(self.DFTPlot.yLeft, 'Power')
                self.DFTPlot.setAxisTitle(self.DFTPlot.xBottom, 'Frequency[Hz]')
                self.DFTPlot.CurveSignal.setData(self.w_o1, self.Pxx_den_nc)
                self.DFTPlot.replot()

    @pyqtSlot()
    def plot(self):
        Fs = 128
        print self.disco_win.pic_label.pos().x(), self.cookie_pos_x  ,  (self.disco_win.pic_label.pos().x()+self.disco_win.pic_label.width())
        print self.disco_win.grid_widget.x(),(self.disco_win.grid_widget.width())/2

    @pyqtSlot()
    def record(self):
        self.t = threading.Timer(2, lambda: self.record2())
        self.t.start()

    @pyqtSlot()
    def record2(self):
        self.greenback = QtCore.QTimer()
        freq = str(self.freq.toPlainText())
        print "Started recording: " + str(freq)
        subject_name = str(self.subname.toPlainText())
        if os.path.isdir('D:\Project\Records'):
            folder_path = 'D:\Project\Records'
        else:
            folder_path = 'C:\Project\Records'
        path = folder_path + "\\" + str(subject_name)
        if not os.path.exists(path):
            os.mkdir(path)
        '''
        else:
            shutil.rmtree(path, ignore_errors=True)
            os.mkdir(path)
            '''
        # t = len(self.signal_rec_i)
        # c, d = signal.butter(1, 0.16, 'high')
        for i in range(0, 30, 1):
            if 1:# max(self.signal[13])<4140:
                self.signal_rec_i = abs(self.Pxx_den)
                np.savetxt(str(freq) + '_' + str(i)+'.csv', self.signal_rec_i, delimiter=',')

            else:
                time.sleep(2)
                continue
            time.sleep(2)
        for i in range(0, 30, 1):
            if os.path.exists(str(freq) + '_' + str(i)+'.csv'):
                shutil.copy(str(freq) + '_' + str(i)+'.csv', path)
                os.remove(str(freq) + '_' + str(i)+'.csv')
        print "Finished recording: " + str(freq)
        #self.disco_win.midlabel.setText('STOP')
        Connector.result = float(freq)
        self.green()
        time.sleep(2)
        self.whiteback()
        '''
        time.sleep(2)
        Connector.result = 0.0
        '''
    @pyqtSlot()
    def refresh_list(self):
        self.subjectList.clear()
        if os.path.isdir('D:\Project\Records'):
            folder_path = 'D:\Project\Records'
        else:
            folder_path = 'C:\Project\Records'
        # TODO if time is available - upgrade so all files are in one folder and frequencies for learning are displayed
        for subfolder in os.listdir(folder_path):
            if os.path.isdir(os.path.join(folder_path, subfolder)):
                self.subjectList.addItem(subfolder)

    @pyqtSlot()
    def refresh_list_2(self):
        self.subjectList_2.clear()
        if os.path.isdir('D:\Project\Data'):
            folder_path = 'D:\Project\Data'
        else:
            folder_path = 'C:\Project\Data'
        # TODO if time is available - upgrade so all files are in one folder and frequencies for learning are displayed
        for subfolder in os.listdir(folder_path):
            if os.path.isdir(os.path.join(folder_path, subfolder)):
                self.subjectList_2.addItem(subfolder)

    @pyqtSlot()
    def train(self):
        # self.EvaluationButton.setEnabled(True)
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
            elif '8.75_' in name:
                tag[i] = 8.75
            elif '10_' in name:
                tag[i] = 10
            elif '12_' in name:
                tag[i] = 12
            elif '17_' in name:
                tag[i] = 17
            elif '14_' in name:
                tag[i] = 14
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
        if hasattr(self, 'Pxx_den'):
            self.classify()

    def classify(self):
        '''
            freq_dict = {self.upFreq.text().toInt()[0]: "up", self.downFreq.text().toInt()[0]: "down",
                         self.rightFreq.text().toInt()[0]: "right", self.leftFreq.text().toInt()[0]: "left"}
            #self.decision_thread.start()
        '''
        self.sound()
        self.decisiontimer.start(500)

    @pyqtSlot()
    def decide(self):
        if not self.status:
            self.decisiontimer.stop()
        #self.Pxx_den=np.zeros(8)
        if self.Pxx_den.any():
            #Connector.result = float(self.clf.predict(self.Pxx_den))
            #result = np.argmax(abs(self.clf.decision_function(self.Pxx_den))[0,:])

            result= self.clf.decision_function(self.Pxx_den)[0 , :]
            #print result
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
                Connector.result=self.clf.classes_[final_result]
            else:
                Connector.result=0.0
            #print self.clf.decision_function(self.Pxx_den)


            if Connector.result==self.upFreq.text().toFloat()[0] and (float(self.disco_win.grid_widget.pos().y())-10.0)>=0.0:
                self.disco_win.grid_widget.move(self.disco_win.grid_widget.pos().x(),self.disco_win.grid_widget.pos().y()-10)
            elif Connector.result==self.leftFreq.text().toFloat()[0] and (float(self.disco_win.grid_widget.pos().x())-10.0)>=0.0:
                 self.disco_win.grid_widget.move(self.disco_win.grid_widget.pos().x()-10,self.disco_win.grid_widget.pos().y())
            elif Connector.result==self.rightFreq.text().toFloat()[0] and (float(self.disco_win.grid_widget.pos().x())+10.0)<=float(self.screen_width):
                 self.disco_win.grid_widget.move(self.disco_win.grid_widget.pos().x()+10,self.disco_win.grid_widget.pos().y())
            elif Connector.result==self.downFreq.text().toFloat()[0] and (float(self.disco_win.grid_widget.pos().y())+10.0)<=float(self.screen_height):
                 self.disco_win.grid_widget.move(self.disco_win.grid_widget.pos().x(),self.disco_win.grid_widget.pos().y()+10)

            self.cookie_pos_x=self.disco_win.grid_widget.x()+(self.disco_win.grid_widget.width())/2
            self.cookie_pos_y=self.disco_win.grid_widget.y()+(self.disco_win.grid_widget.height())/2
            #self.greenback.start(100)
            self.decision_func.setText(str(result))
            if  self.disco_win.pic_label.pos().x() <= self.cookie_pos_x  and  (self.disco_win.pic_label.pos().x()+self.disco_win.pic_label.width()) >= self.cookie_pos_x and self.cookie_pos_y >=self.disco_win.pic_label.pos().y() and (self.disco_win.pic_label.pos().y()+self.disco_win.pic_label.height())>=self.cookie_pos_y:
                self.decisiontimer.stop()
                self.finish()

            '''
            probability = self.clf.predict_proba(self.Y_fitted)
            i = 0
            print self.clf.classes_
            print probability
            for proba_ in probability[0]:
                print i + self.clf.classes_[i] + proba_
                if proba_ > 0.4:
                    Connector.result = self.clf.classes_[i]
                else:
                    Connector.result = 0.0
                i += 1
                '''
        else:
            Connector.result = 0.0
        #print "decision is " + str(Connector.result)
        self.decision.setText(str(Connector.result))
        #self.decision_func.setText(str(result))
        '''
        if self.status:
            self.classify()
            '''


    @pyqtSlot()
    def whiteback(self):

        self.disco_win.upWidget.pixmap_black=self.upWidget.pixmap_black
        self.p_up.setColor(self.disco_win.upWidget.backgroundRole(),QtCore.Qt.white)
        self.disco_win.upWidget.setPalette(self.p_up)

        self.disco_win.leftWidget.pixmap_black=self.leftWidget.pixmap_black
        self.p_left.setColor(self.disco_win.leftWidget.backgroundRole(),QtCore.Qt.white)
        self.disco_win.leftWidget.setPalette(self.p_left)

        self.disco_win.rightWidget.pixmap_black=self.rightWidget.pixmap_black
        self.p_right.setColor(self.disco_win.rightWidget.backgroundRole(),QtCore.Qt.white)
        self.disco_win.rightWidget.setPalette(self.p_right)

        self.disco_win.downWidget.pixmap_black=self.downWidget.pixmap_black
        self.p_down.setColor(self.disco_win.downWidget.backgroundRole(),QtCore.Qt.white)
        self.disco_win.downWidget.setPalette(self.p_down)



    @pyqtSlot()
    def green(self):

        if Connector.result==self.upFreq.text().toFloat()[0]:
            self.disco_win.upWidget.pixmap_black=self.disco_win.upWidget.pixmap_green
            self.p_up.setColor(self.disco_win.upWidget.backgroundRole(),QtCore.Qt.green)
            self.disco_win.upWidget.setPalette(self.p_up)

        elif Connector.result==self.leftFreq.text().toFloat()[0]:
            self.disco_win.leftWidget.pixmap_black=self.disco_win.leftWidget.pixmap_green
            self.p_left.setColor(self.disco_win.leftWidget.backgroundRole(),QtCore.Qt.green)
            self.disco_win.leftWidget.setPalette(self.p_left)

        elif Connector.result==self.rightFreq.text().toFloat()[0]:
            self.disco_win.rightWidget.pixmap_black=self.disco_win.rightWidget.pixmap_green
            self.p_right.setColor(self.disco_win.rightWidget.backgroundRole(),QtCore.Qt.green)
            self.disco_win.rightWidget.setPalette(self.p_right)

        elif Connector.result==self.downFreq.text().toFloat()[0]:
            self.disco_win.downWidget.pixmap_black=self.disco_win.downWidget.pixmap_green
            self.p_down.setColor(self.disco_win.downWidget.backgroundRole(),QtCore.Qt.green)
            self.disco_win.downWidget.setPalette(self.p_down)


    @pyqtSlot()
    def Runplot(self):

        self.plot_status = 1 - self.plot_status
        self.RunButton.setText(self.plotlabels[self.plot_status])

    @pyqtSlot()
    def sound(self):
        freq = 44100     # audio CD quality
        bitsize = -16    # unsigned 16 bit
        channels = 2     # 1 is mono, 2 is stereo
        buffer = 2048    # number of samples (experiment to get best sound)
        pg.mixer.init(freq, bitsize, channels, buffer)
        # volume value 0.0 to 1.0
        pg.mixer.music.set_volume(0.5)
        clock = pg.time.Clock()
        if self.disco_win.opened:
            pg.mixer.music.load('hello.mp3')
            pg.mixer.music.play()

            while pg.mixer.music.get_busy():
                #check if playback has finished
                clock.tick(30)

        '''
        sound = pyglet.media.load('hello_wav.wav')
        sound.play()
        #pyglet.app.run()
        '''

    @pyqtSlot()
    def record_Eval(self):
        self.r = threading.Timer(2, lambda: self.record_Eval_2())
        self.r.start()

    @pyqtSlot()
    def finish(self):
        freq = 44100     # audio CD quality
        bitsize = -16    # unsigned 16 bit
        channels = 2     # 1 is mono, 2 is stereo
        buffer = 2048    # number of samples (experiment to get best sound)
        pg.mixer.init(freq, bitsize, channels, buffer)
        # volume value 0.0 to 1.0
        pg.mixer.music.set_volume(0.5)
        clock = pg.time.Clock()
        if self.disco_win.opened:
            pg.mixer.music.load('cookie_sound.mp3')
            pg.mixer.music.play()

            while pg.mixer.music.get_busy():
                #check if playback has finished
                clock.tick(30)
        '''
        sound = pyglet.media.load('cookie_sound_wav')
        sound.play()
        '''

    @pyqtSlot()
    def record_Eval_2(self):
        freq = str(self.freq.toPlainText())
        print "Started recording: " + str(freq)
        subject_name = str(self.subname.toPlainText())
        if os.path.isdir('D:\Project\Data'):
            folder_path = 'D:\Project\Data'
        else:
            folder_path = 'C:\Project\Data'
        path = folder_path + "\\" + str(subject_name)
        if not os.path.exists(path):
            os.mkdir(path)
        '''
        else:
            shutil.rmtree(path, ignore_errors=True)
            os.mkdir(path)
            '''
        # t = len(self.signal_rec_i)
        # c, d = signal.butter(1, 0.16, 'high')
        for i in range(0, 15, 1):
            if 1:# max(self.signal[13])<4140:
                self.signal_rec_i = abs(self.Pxx_den)
                np.savetxt(str(freq) + '_' + str(i)+'.csv', self.signal_rec_i, delimiter=',')

            else:
                time.sleep(2)
                continue
            time.sleep(2)
        for i in range(0, 15, 1):
            if os.path.exists(str(freq) + '_' + str(i)+'.csv'):
                shutil.copy(str(freq) + '_' + str(i)+'.csv', path)
                os.remove(str(freq) + '_' + str(i)+'.csv')
        print "Finished recording: " + str(freq)

        Connector.result = float(freq)
        self.green()
        time.sleep(2)
        self.whiteback()


    @pyqtSlot()
    def Evaluation(self):
        subject_name = str(self.subjectList_2.currentItem().text())
        # import data and tags
        data = {}
        data_cut = {}
        tag = np.zeros(60)
        all_freq=np.zeros(60)
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
                all_freq[i]=13
            elif '8.75_' in name:
                tag[i] = 8.75
                all_freq[i]=8.75
            elif '10_' in name:
                tag[i] = 10
                all_freq[i]=10
            elif '12_' in name:
                tag[i] = 12
            elif '17_' in name:
                tag[i] = 17
                all_freq[i]=17
            elif '14_' in name:
                tag[i] = 14
                all_freq[i]=14
            elif '15_' in name:
                tag[i] = 15
                all_freq[i]=15
            elif '20_' in name:
                tag[i] = 20
                all_freq[i]=20
            elif '25_' in name:
                tag[i] = 25
                all_freq[i]=25
            elif '30_' in name:
                tag[i] = 30
                all_freq[i]=30
            elif '16_' in name:
                tag[i] = 16
                all_freq[i]=16
            elif '37_' in name:
                tag[i] = 37
                all_freq[i]=37
            elif '11_' in name:
                tag[i] = 11
                all_freq[i]=11
            elif '9_' in name:
                tag[i] = 9
                all_freq[i]=9
            elif '23_' in name:
                tag[i] = 23
                all_freq[i]=23
            i += 1
            csvfile.close()

        #X, y = [data[i] for i in range(1, data_size)], [tag[k] for k in range(1, data_size)]
        #freq = [self.upFreq.text().toFloat()[0], self.downFreq.text().toFloat()[0], self.rightFreq.text().toFloat()[0], self.leftFreq.text().toFloat()[0]]
        freq = np.unique(all_freq)
        if not self.search_flag:
            print "Frequencies used: " +str(freq)
        test=np.zeros(60)
        unfiltered_test=np.zeros(60)
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
            unfiltered_test[w]=self.clf.classes_[final_result]

        TP=np.zeros(4)
        FP=np.zeros(4)
        TN=np.zeros(4)
        FN=np.zeros(4)

        #correct=np.sum(test == tag)

        for i in range(4):
            TP[i]=np.sum(test[tag == freq[i]] == freq[i])
            FP[i]=np.sum(test[tag != freq[i]] == freq[i])
            TN[i]=np.sum(test[tag != freq[i]] != freq[i])
            FN[i]=np.sum(test[tag == freq[i]] != freq[i])

        self.acc = (np.sum(TP)+np.sum(TN))/(np.sum(TP)+np.sum(FP)+np.sum(TN)+np.sum(FN))


        if (self.search_flag):
            return

        UTP=np.zeros(4)
        UFP=np.zeros(4)
        UTN=np.zeros(4)
        UFN=np.zeros(4)

        #ucorrect=np.sum(unfiltered_test == tag)

        for i in range(4):
            UTP[i]=np.sum(unfiltered_test[tag == freq[i]] == freq[i])
            UFP[i]=np.sum(unfiltered_test[tag != freq[i]] == freq[i])
            UTN[i]=np.sum(unfiltered_test[tag != freq[i]] != freq[i])
            UFN[i]=np.sum(unfiltered_test[tag == freq[i]] != freq[i])

        uacc = (np.sum(UTP)+np.sum(UTN))/(np.sum(UTP)+np.sum(UFP)+np.sum(UTN)+np.sum(UFN))
        ufsensitivity=(np.sum(UTP))/(np.sum(UTP)+np.sum(UFN))
        ufspecificity=(np.sum(UTN))/(np.sum(UFP)+np.sum(UTN))
        sensitivity=(np.sum(UTP))/(np.sum(UTP)+np.sum(UFN))
        specificity=(np.sum(TN))/(np.sum(FP)+np.sum(TN))

        #print "UF correct=" + str(ucorrect)
        print "UF Sensitivity=" + str(ufsensitivity)
        print "UF Specificity=" + str(ufspecificity)
        print "total unfiltered accuracy=" + str(uacc)
        #print "correct=" + str(correct)
        print "Sensitivity=" + str(sensitivity)
        print "Specificity=" + str(specificity)
        print "total accuracy=" + str(self.acc)





    @pyqtSlot()
    def findParameters(self):
        gamma_range=[10 ** i for i in range(-5, 5)]
        C_range = [2 ** j for j in range(-2,7)]
        Acc= np.zeros((len(gamma_range),len(C_range)))
        i=0
        j=0
        self.search_flag=1

        for gamma in gamma_range:
            j=0
            for c in C_range:
                self.clf = svm.SVC(gamma=gamma, C=c)
                self.train()
                self.Evaluation()
                Acc[i][j]=self.acc
                j+=1
            i+=1

        optimal_gamma, optimal_C= np.unravel_index(Acc.argmax(), Acc.shape)

        print "Maximum accuracy for large-scale search, " +str(Acc[optimal_gamma, optimal_C])+ ", was achieved for gamma = "\
              +str(gamma_range[optimal_gamma])+ " and C = " + str(C_range[optimal_C]) + "."

        fig, ax = plt.subplots()
        ax.set_yscale('log', basey=10)
        ax.set_xscale('log', basex=2)

        plt.pcolor(np.array(C_range), np.array(gamma_range), Acc)
               #norm=LogNorm(vmin=Acc.min(), vmax=Acc.max()))
        plt.xlabel('C')
        plt.ylabel('gamma')
        plt.colorbar()
        plt.show()

        gamma_res = gamma_range[optimal_gamma]/2.0
        C_res = C_range[optimal_C]/4.0
        gamma_range_res=np.array([gamma_res * i for i in range(20)]) +gamma_res
        C_range_res = np.array([C_res * i for i in range(8)]) + C_res
        Acc_res= np.zeros((len(gamma_range_res),len(C_range_res)))
        i=0
        j=0
        print "Now the following parameters will be searched:"
        print "For gamma - " +str(gamma_range_res)
        print "For C - " +str(C_range_res)
        for gamma in gamma_range_res:
            j=0
            for c in C_range_res:
                self.clf = svm.SVC(gamma=gamma, C=c)
                self.train()
                self.Evaluation()
                Acc_res[i][j]=self.acc
                j+=1
            i+=1

        self.search_flag=0
        optimal_gamma_res, optimal_C_res = np.unravel_index(Acc_res.argmax(), Acc_res.shape)
        print "Maximum accuracy, " +str(Acc_res[optimal_gamma_res, optimal_C_res])+ ", was achieved for gamma = "\
              +str(gamma_range_res[optimal_gamma_res])+ " and C = " + str(C_range_res[optimal_C_res]) + "."
        plt.pcolor(np.array(C_range_res), np.array(gamma_range_res), Acc_res)
               #norm=LogNorm(vmin=Acc.min(), vmax=Acc.max()))
        plt.xlabel('C')
        plt.ylabel('gamma')
        plt.colorbar()
        plt.show()

        self.clf = svm.SVC(gamma=gamma_range_res[optimal_gamma_res], C=C_range_res[optimal_C_res])
        self.train()
        print "For these parameters:"
        self.Evaluation()
        print "Parameters are now set."








