import matplotlib.pyplot as plt
import numpy as np
import serial
import time

Fs = 512.0;  # sampling rate
Ts = 1.0/Fs; # sampling interval
t = np.arange(0,10,Fs) # time vector; create Fs samples between 0 and 1.0 sec.
y1 = np.arange(-1.5,1.5,Ts) # signal vector; create Fs samples
y2 = np.arange(-1.5,1.5,Ts)
y3 = np.arange(-1.5,1.5,Ts)
y4 = np.arange(-0.5,1.5,Ts)
y1k = np.arange(-1.5,1.5,Ts)
y2k = np.arange(-1.5,1.5,Ts)
y3k = np.arange(-1.5,1.5,Ts)
y4k = np.arange(-1.5,1.5,Ts)

serdev = '/dev/ttyACM0'
s = serial.Serial(serdev,115200)
for x in range(0, int(Fs)):
    line=s.readline() # Read an echo string from K66F terminated with '\n'
    print(line)
    y1=line.decode().strip().split(" ")[0]
    y1k[x] = float(y1)
    y2=line.decode().strip().split(" ")[1]
    y2k[x] = float(y1)
    y3=line.decode().strip().split(" ")[2]
    y3k[x] = float(y3)
    y4=line.decode().strip().split(" ")[3]
    y4k[x] = float(y4)
    print(y4k[x])

fig, ax = plt.subplots(2, 1)
plt.plot(t,y4k)
'''
ax[0].plot(x,y1k,'r',label = 'x')
ax[0].plot(x,y2k,'b',label = 'y')
ax[0].plot(x,y3k,'g',label = 'z')
ax[0].plot.legend(loc='lower left')
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Acc Vector')
ax[1].plot(x,y4k,'bo') # plotting the spectrum
ax[1].set_xlabel('Time')
ax[1].set_ylabel('Tilt')
'''
plt.show()
s.close()