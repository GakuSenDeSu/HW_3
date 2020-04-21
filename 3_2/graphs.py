import matplotlib.pyplot as plt
import numpy as np
import serial
import time

t = np.arange(0,10,0.1) # time vector; create Fs samples between -0.5 and 10 sec.
y1k = np.arange(0,10,0.1)
y2k = np.arange(0,10,0.1)
y3k = np.arange(0,10,0.1)
y4k = np.arange(0,10,0.1)

serdev = '/dev/ttyACM0'
s = serial.Serial(serdev,115200)
for x in range(0,int(100)):
    line=s.readline() # Read an echo string from K66F terminated with '\n'
    y1=line.decode().strip().split(" ")[0]
    y1k[x] = float(y1)
    y2=line.decode().strip().split(" ")[1]
    y2k[x] = float(y2)
    y3=line.decode().strip().split(" ")[2]
    y3k[x] = float(y3)
    y4=line.decode().strip().split(" ")[3]
    y4k[x] = float(y4)


fig, ax = plt.subplots(2, 1)
ax[0].plot(t,y1k,'r')
ax[0].plot(t,y2k,'b')
ax[0].plot(t,y3k,'g')
ax[0].legend(labels = ['x', 'y', 'z'], loc = 'best')
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Acc Vector')
ax[1].stem(t,y4k,use_line_collection=True) # plotting the spectrum
ax[1].set_xlabel('Time')
ax[1].set_ylabel('Tilt')
plt.show()
s.close()