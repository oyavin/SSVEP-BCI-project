import logging
from scipy import signal
from PyQt4 import QtCore
import numpy as np
import matplotlib.pyplot as plt

result = 0.0

class QHandler(logging.Handler):  # Inherit from logging.Handler
    def __init__(self, textEdit):
        logging.Handler.__init__(self)
        self.textEdit = textEdit

    def emit(self, record):
        self.textEdit.append(self.format(record))


class Connector():
    def __init__(self, MyUI, mode='online'):
        self.MyUI = MyUI

        logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=logging.DEBUG, datefmt='%H:%M:%S')
        self.logger = logging.getLogger(__name__)
        self.qHandler = QHandler(MyUI.textLog)
        self.qHandler.setFormatter(logging.Formatter(fmt='%(asctime)s %(levelname)s: %(message)s', datefmt='%H:%M:%S'))
        self.qHandler.setLevel(logging.DEBUG)
        self.logger.addHandler(self.qHandler)
        self.nchannels = 14
        self.Fs = 128
        self.buffersize = 1

        self.t = np.arange(0.0, 3.001, 1.0 / self.Fs)
        self.signal = np.zeros((self.nchannels, len(self.t)))
        self.Y = np.zeros((self.nchannels, len(self.t)))
        self.t_rec=np.arange(0.0, 60.001, 1.0 / self.Fs)
        self.signal_rec=np.zeros((self.nchannels, len(self.t_rec)))

        self.logger.info('Application started')

        self.configfile = 'settings.ini'
        self.settings = QtCore.QSettings(self.configfile, QtCore.QSettings.NativeFormat)

        if mode == 'offline':
           from MiniLogger import EEGLogger
           self.logger.info('Started in offline mode')

        else:
            from EEGLogger import EEGLogger
            self.logger.info('Started in online mode')

        # added logger
        self.logger.info('Connecting to EEG system')
        self.eeg_log = EEGLogger()  # TODO improve error handling
        if self.eeg_log.startup_failed:
            self.logger.info('EmoEngine Connection failed')

        if self.eeg_log.state != 0:
            self.logger.info('Connection Error')

        self.getConfiguration()
        self.initUI()

    def saveSettings(self):
        self.settings.setValue("nchannels", self.nchannels)
        self.settings.setValue("Fs", self.Fs)
        self.settings.setValue("buffersize", self.buffersize)
        self.settings.setValue("electrode_names", self.electrode_names)
        self.logger.info('Configuration saved to ' + self.configfile)

    def getConfiguration(self):
        # Signal properties
        #self.nchannels = 14
        #self.Fs = 128
        #self.buffersize = 1
        self.n_channels = len(self.eeg_log.eeg_channels)

        #self.t = np.arange(0.0, 3.001, 1.0 / self.Fs)
        #self.signal = np.zeros((self.nchannels, len(self.t)))

        self.electrode_names = self.eeg_log.eeg_channels
        # self.electrode_quality = [2, 0, 1] + [0] * (len(self.electrode_names) - 3)
        self.cube_command = 0

        self.logger.info('Configuration loaded from ' + self.configfile)
        self.saveSettings()  # TODO Rethink loading from external file

    def initUI(self):
        # self.MyUI.MyElectrodeMap.initUI(self.electrode_names, self.electrode_quality) # Contact Quality not required
        self.MyUI.MyEEGTab.initUI(self.electrode_names)

    def update(self):
        self.eeg_log.update()
        samples = self.eeg_log.nSam
        if samples != 0:
            for (channel, emotiv_channel) in zip(range(self.n_channels), self.eeg_log.eeg_channel_numbers):
                self.signal[channel, :] = np.concatenate(
                    (self.signal[channel, samples:], self.eeg_log.data[emotiv_channel, :]), 0)
            '''for channel in range(self.nchannels):
                self.signal[channel, :] = np.concatenate(
                    (self.signal[channel, samples:], self.eeg_log.data[channel, :]), 0)
                self.signal_rec[channel, :] = np.concatenate(
                    (self.signal_rec[channel, samples:], self.eeg_log.data[channel, :]), 0)'''

            self.MyUI.MyEEGTab.updatePlots(self.t, self.signal)
            self.MyUI.mySSVEPTab.DFT(self.signal, self.signal_rec)
            # self.MyUI.MyElectrodeMap.update(self.electrode_quality) # Electrode quality not required for EPOC
            '''
            Fs=128
            n = len(self.t)
            k = np.arange(n/2)
            time = n/Fs
            frq = k/time
            freq = frq[range(n/2)]
            self.Y1= np.fft.fft(self.signal[6,:])/n
            self.Y1 = self.Y1[range(n/2)]


            plt.ion()

            plt.plot(freq, abs(self.Y1), 'r-')

            #plt.axis([0,10,0,1])
            plt.draw()
            plt.clf()
            '''''

    def close(self):
        self.eeg_log.close()
