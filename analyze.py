import matplotlib.pyplot as plt
import sys
import os
import pandas as pd

folder = r"Data\20251004" + "\\"

fileName = "AprilTagTester_20251004-105624.csv"

file = os.path.join(folder, fileName)
print(file)

#Timestamp	X_Pos	Y_Pos	ID	pose_X	pose_Y	pose_yaw	pose_bearing	raw_x	raw_y	raw_z	raw_pitch	raw_roll	raw_yaw

tagID = []

timeStamp1 = []
xPos1 = []
yPos1 = []
poseX1 = []
poseY1 = []
poseYaw1 = []
poseBearing1 = []
rawX1 = []
rawY1 = []
rawZ1 = []
rawPitch1 = []
rawRoll1 = []
rawYaw1 = []

timeStamp2 = []
xPos2 = []
yPos2 = []
poseX2 = []
poseY2 = []
poseYaw2 = []
poseBearing2 = []
rawX2 = []
rawY2 = []
rawZ2 = []
rawPitch2 = []
rawRoll2 = []
rawYaw2 = []


with open(file, "r",errors='ignore') as f:
    for lineNumber, readLine in enumerate(f,1):
        if lineNumber == 1:
            continue
        readLine = readLine.rstrip()
        myList = readLine.split(",")

        if float(myList[3]) == 20:
            timeStamp1.append(float(myList[0]))
            xPos1.append(float(myList[1]))
            yPos1.append(float(myList[2]))
            poseX1.append(float(myList[4]))
            poseY1.append(float(myList[5]))
            poseYaw1.append(float(myList[6]))
            poseBearing1.append(float(myList[7]))
        else:
            timeStamp2.append(float(myList[0]))
            xPos2.append(float(myList[1]))
            yPos2.append(float(myList[2]))
            poseX2.append(float(myList[4]))
            poseY2.append(float(myList[5]))
            poseYaw2.append(float(myList[6]))
            poseBearing2.append(float(myList[7]))


fig, ax1 = plt.subplots(layout='constrained',dpi=300)
ax1.plot(timeStamp1,poseX1,label='Red X')
ax1.plot(timeStamp2,poseX2,label='Blue X')
ax1.plot(timeStamp1,poseY1,label='Red Y')
ax1.plot(timeStamp2,poseY2,label='Blue Y')

ylim = ax1.get_ylim()
ax1.set_ylim(ylim[0],ylim[1])
ax1.set_xlabel('Time (sec)')
ax1.set_ylabel('Bearing (degrees)')
ax1.legend()
fig.savefig(f"test1.png")
plt.close(fig)

# fig, ax1 = plt.subplots(layout='constrained',dpi=300)
# ax1.plot(timeStamp,current,label='Current')
# ylim = ax1.get_ylim()
# ax1.set_ylim(ylim[0],ylim[1])
# ax1.set_xlabel('Time (sec)')
# ax1.set_ylabel('Current (amps)')
# fig.savefig("test2.png")
# plt.close(fig)

