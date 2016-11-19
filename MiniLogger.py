import numpy as np
import os
import ctypes
from ctypes.util import find_library

print ctypes.util.find_library('edk.dll')
print os.path.exists('.\\edk.dll')
libEDK = ctypes.cdll.LoadLibrary(".\\edk.dll")


class EEGLogger():
    def __init__(self):
        print 'connected'
        self.eeg_channels = ['AF3', 'F7', 'F3', 'FC5', 'T7', 'P7', 'O1', 'O2', 'P8', 'T8', 'FC6', 'F4', 'F8', 'AF4']
        self.channels = ['COUNTER', 'INTERPOLATED', 'RAW_CQ'] + self.eeg_channels + ['GYROX', 'GYROY', 'TIMESTAMP',
                                                                                     'FUNC_ID', 'FUNC_VALUE', 'MARKER',
                                                                                     'SYNC_SIGNAL']
        self.phase = 0
        self.data = 0
        self.nSam = 1
        self.startup_failed = False
        self.state = 0

    def update(self):
        # self.nSam=1-self.nSam #used for testing of behaviour for empty data
        if self.phase > np.pi - 0.0001:
            self.phase = 0.0

        temp = 0.8 - (2.0 * self.phase / np.pi) + 0.4 * np.random.random()
        self.data = np.tile(temp, [len(self.channels), 1])
        self.phase += np.pi * 0.02

    def close(self):
        print 'closing'