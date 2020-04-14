import matplotlib.pyplot as plt
import numpy as np
import serial
import time
Fs = 128.0;  # sampling rate
Ts = 1.0/Fs; # sampling interval
t = np.arange(0,10,Fs) # time vector; create Fs samples between 0 and 1.0 sec.
y1 = np.arange(-1.5,1.5,Ts) # signal vector; create Fs samples
y2 = np.arange(-1.5,1.5,Ts)
y3 = np.arange(-1.5,1.5,Ts)
y4 = np.arange(-0.5,1.5,Ts)

serdev = '/dev/ttyACM0'
s = serial.Serial(serdev,115200)
for x in range(0, int(Fs)):
    line=s.readline() # Read an echo string from K66F terminated with '\n'
    print(line)
    y1,y2,y3,y4=line.split(" ",3)
    print(y1)
    print(y2)
    print(y3)
    print(y4)
    y1[x] = float(y1)
    y2[x] = float(y2)
    y3[x] = float(y3)
    y4[x] = float(y4)


fig, ax = plt.subplots(2, 1)
ax[0].plot(y1,'r',label = 'x')
ax[0].plot(y2,'b',label = 'y')
ax[0].plot(y3,'g',label = 'z')
ax[0].plt.legend(loc='lower left')
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Acc Vector')
ax[1].plot(t,y4,'bo') # plotting the spectrum
ax[1].set_xlabel('Time')
ax[1].set_ylabel('Tilt')
plt.show()
s.close()