import matplotlib.pyplot as plt
import numpy as np
import sys
# import pdb

# np.random.seed(19680801)

x: list[float] = []
y: list[float] = []
xDist: float
yDist: float
gnratd_pts: list[tuple] = []

jump_factor: float = 0.5
init_points: list[tuple] = [[1, 0], [1.5, 1], [2, 0]]
prev_pt = init_points[-1]

num_points: int = int(sys.argv[1])
prcnt = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

for i in range(num_points):
    for j in prcnt:
        if i == j * num_points:
            print("%i%% done" %(j * 100))

    # a = np.random.randint(0, len(init_points))
    # nxt_pt = init_points[a]
    nxt_pt = init_points[np.random.randint(0, len(init_points))]

    # xDist = (prev_pt[0] + nxt_pt[0]) / -2
    xDist = (prev_pt[0] - nxt_pt[0]) * -(jump_factor)

    # yDist = (prev_pt[1] + nxt_pt[1]) / -2
    yDist = (prev_pt[1] - nxt_pt[1]) * -(jump_factor)
        
    new_pt = prev_pt[0] + xDist, prev_pt[1] + yDist

    prev_pt = new_pt
    gnratd_pts.append(new_pt)
    
for i in range(0, len(init_points)):
    x.append(init_points[i][0])
    y.append(init_points[i][1])
plt.scatter(x, y, marker="x")

for i in range(0, len(gnratd_pts)):
    x.append(gnratd_pts[i][0])
    y.append(gnratd_pts[i][1])
plt.scatter(x, y, marker=".")

print("finished")
plt.show()