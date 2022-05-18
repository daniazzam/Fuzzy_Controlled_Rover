from mpu6050 import mpu6050
from time import sleep
mpu = mpu6050(0x68)

def getInclination():
    gyro_data = mpu.get_gyro_data()
    x=gyro_data['x']
    y=gyro_data['y']
    z=gyro_data['z']
    
    return float(x)

if __name__=='__main__':
    while True:
        print('x is: '+str(getInclination()))
        sleep(1)
    