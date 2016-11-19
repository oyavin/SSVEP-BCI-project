import ctypes
import os
from ctypes import *
import numpy as np
from ctypes.util import find_library

print find_library('edk.dll')
print os.path.exists('.\\edk.dll')
libEDK = cdll.LoadLibrary(".\\edk.dll")


class EEGLogger():
    def __init__(self):
        self.eeg_channels = ('AF3', 'F7', 'F3', 'FC5', 'T7', 'P7', 'O1', 'O2', 'P8', 'T8', 'FC6', 'F4', 'F8', 'AF4')
        self.channels = ('COUNTER', 'INTERPOLATED', 'RAW_CQ') + self.eeg_channels + ('GYROX', 'GYROY', 'TIMESTAMP',
                                                                                     'FUNC_ID', 'FUNC_VALUE', 'MARKER',
                                                                                     'SYNC_SIGNAL')
        # INTERPOLATED tells if package was dropped, RAW_CQ is muxed contact quality

        self.targetChannelList = range(len(self.channels))
        self.eeg_channel_numbers = [self.channels.index(self.eeg_channels[i]) for i in range(len(self.eeg_channels))]
        self.eEvent = libEDK.EE_EmoEngineEventCreate()
        # self.eState = libEDK.EE_EmoStateCreate()
        self.userID = c_uint(0)
        self.nSam = 0
        buffer_in_secs = c_float(1) # set buffer len at 1 sec
        self.ready_to_collect = False
        self.data = np.zeros((len(self.channels), 0))

        self.startup_failed = False
        if libEDK.EE_EngineConnect("Emotiv Systems-5") != 0:  # if not OK
            self.startup_failed = True

        self.hData = libEDK.EE_DataCreate()  # create data handle
        libEDK.EE_DataSetBufferSizeInSec(buffer_in_secs)  # def buffer len TODO might shorten buffer because redundant
        self.state = libEDK.EE_EngineGetNextEvent(self.eEvent)

    def update(self):
        c_nSam = c_uint()

        self.state = libEDK.EE_EngineGetNextEvent(self.eEvent)

        if self.state == 0:  # 0 means OK
            event_type = libEDK.EE_EmoEngineEventGetType(self.eEvent)
            libEDK.EE_EmoEngineEventGetUserId(self.eEvent, byref(self.userID))
            if event_type == 16:  # Log the EmoState if it has been updated
                print "User added"
                libEDK.EE_DataAcquisitionEnable(self.userID, True)
                self.ready_to_collect = True

        if self.ready_to_collect:
            libEDK.EE_DataUpdateHandle(0, self.hData)
            libEDK.EE_DataGetNumberOfSample(self.hData, byref(c_nSam))
            self.nSam = c_nSam.value
            if self.nSam != 0:

                arr = (ctypes.c_double * self.nSam)()
                ctypes.cast(arr, ctypes.POINTER(ctypes.c_double))

                temp = np.zeros((len(self.channels), self.nSam))
                for i in self.targetChannelList:
                    libEDK.EE_DataGet(self.hData, self.targetChannelList[i], byref(arr), self.nSam)
                    temp[i, :] = np.array(arr)

                self.data = temp

    def close(self):
        libEDK.EE_DataFree(self.hData)
        libEDK.EE_EngineDisconnect()
        # libEDK.EE_EmoStateFree(self.eState)
        libEDK.EE_EmoEngineEventFree(self.eEvent)
        print "Disconnected"
