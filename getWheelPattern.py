import serial as s
import time as t

sc = s.Serial(baudrate=115200, port="COM3")

#def getWheelPattern():
size = int()
pattern = str()

sc.open()

print("waiting the port is opened")
while sc.isOpen():
    print(".")
    t.sleep(0.001)

print("Requesting the size of the wheel (Num of theets)")
# Requesting the size of the wheel (Num of theets)
sc.write(b"p")

print("Waiting for the response of the microcontroller")
# Waiting for the response of the microcontroller
t.sleep(1)
aux = sc.inWaiting()
print(aux)

while aux < 2:
    t.sleep(0.0005)
    aux = sc.inWaiting()

print("Getting the value")
size = int(sc.readline())

# Requesting the pattern
sc.write(b"P")

# Waiting for the response of the microcontroller
while sc.inWaiting() < 2*size:
    t.sleep(1)

#t.sleep(0.001)

sizeBuff = sc.inWaiting()
buff = sc.read(sizeBuff)
buff = buff.decode()
buff = buff.split("\r\n", 1)

pattern = buff[0]

print("Size of pattern:" + str(size))
print("Pattern:\r\n" + pattern)

sc.close()


#getWheelPattern()
