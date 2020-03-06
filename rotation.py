#Rotation: entered angle degree rotation around the origin

import numpy as np
import matplotlib.pyplot as plt

angle = float(input("Enter angle: "))
tx = int(input("Enter x: "))
ty = int(input("Enter y: "))

t1 = np.array([
    [1, 0, -tx],
    [0, 1, -ty],
    [0, 0, 1]
])

R = np.array([[ np.cos(np.radians(angle)), -np.sin(np.radians(angle)), 0.0],
              [ np.sin(np.radians(angle)), np.cos(np.radians(angle)), 0.0],
              [ 0, 0, 1]])

print('r ' , R)
t2 = np.array([
    [1, 0, tx],
    [0, 1, ty],
    [0, 0, 1]
])
print('t2: ',t2)

M = np.matmul(t2, np.matmul(R, t1))

#calculating points
p = np.array([tx, ty, 1])
p1 = M.dot(p)

p = np.array([-tx, ty, 1])
p2 = M.dot(p)

p = np.array([-tx, -ty, 1])
p3 = M.dot(p)

p = np.array([tx, -ty, 1])
p4 = M.dot(p)

#vector with x coordinate of all 4 points
pointsx = [p1[0],p2[0],p3[0],p4[0]]
#vector with y coordinate of all 4 points
pointsy = [p1[1],p2[1],p3[1],p4[1]]

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

#making coordinate system
ax.spines['left'].set_position(('data', 0.0))
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position(('data', 0.0))
ax.spines['top'].set_color('none')
ax.spines['left'].set_smart_bounds(True)
ax.spines['bottom'].set_smart_bounds(True)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

#show points and make lines between them - range 3 because the first and last point will be connected manually
for i in range(3):
	pointx = pointsx[i:i+2]
	pointy = pointsy[i:i+2]
	ax.plot(pointx,pointy,'ro-')


lastx = [p1[0], p4[0]]
lasty = [p1[1], p4[1]]
ax.plot(lastx, lasty, 'ro-')

plt.show()
