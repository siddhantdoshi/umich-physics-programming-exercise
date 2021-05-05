import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import axes as ax
from mpl_toolkits.mplot3d import Axes3D

import numpy as np

x, y, z, vx, vy, vz = np.loadtxt('./coordAa.dat.txt', unpack=True)
print(len(x))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c='r', marker='.', s=0.1)

#Axes3D.scatter(x,y,z)
ax.set_xlabel('X [kpc]')
ax.set_ylabel('Y [kpc]')
ax.set_zlabel('Z [kpc]')

#plt.axis([-1500., 1500., -1500., 1500, -1500, 1500])
ax.set_xlim3d(-1500, 1500)
ax.set_ylim3d(-1500, 1500)
ax.set_zlim3d(-1500, 1500)
plt.show()

radius = sorted([np.sqrt(i**2 + j**2 + k**2) for i, j, k in zip(x, y, z) if np.sqrt(i**2 + j**2 + k**2) <= 300])
max_radius = max(radius)
min_radius = min(radius)

print(max_radius, min_radius)

num_bins = 50
n, bins, patches = plt.hist(radius, num_bins, facecolor="blue", alpha=0.5, ec="black")

plt.title = "Radius Histogram"
plt.xlabel = "Radius / kpc"
plt.ylabel = "Frequency"

plt.show()

num_elements = 0
bin_content = []
median = []

for bin_size in n:
	bin_content = radius[int(num_elements) : int(num_elements + bin_size)]

	if bin_size == 0:
		median.append(0)

	elif bin_size % 2 == 1:
		median.append(float(bin_content[int(((bin_size + 1) / 2) - 1)]))

	else:
		median.append((bin_content[int((bin_size / 2) - 1)] + bin_content[int(bin_size / 2)]) / 2.0)
	
	num_elements += bin_size

print(median)

volume_slices = (4.0 / 3.0) * np.pi * (bins[1] - bins[0]) ** 3
print(volume_slices)

mass = 1.0
radial_mass_density = [(float(i) * mass / volume_slices) for i in n]
print(radial_mass_density)
