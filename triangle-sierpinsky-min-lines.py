import matplotlib.pyplot as plt, numpy as np, sys

x: list[float] = []
y: list[float] = []
xDist: float = 0
yDist: float = 0
gnratd_pts: list[tuple] = []

jump_factor: float = 0.5
init_points: list[tuple] = [[1, 0], [1.5, 1], [2, 0]]
prev_pt = init_points[-1]

num_points: int = int(sys.argv[1])

for i in range(num_points):
    nxt_pt = init_points[np.random.randint(0, len(init_points))]
    
    xDist = (prev_pt[0] - nxt_pt[0]) * -(jump_factor)
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

plt.show()