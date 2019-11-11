import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
r = np.arange(0., 10., 0.3)
p1, = ax.plot(r, r, 'r--', label='line 1', linewidth=5)
p2, = ax.plot(r, r**0.5, 'bs', label='line 2', linewidth=5)
p3, = ax.plot(r, np.sin(r), 'g^', label='line 3', linewidth=5)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, fontsize=20)
ax.set_xlabel('x', fontsize=20)
ax.set_ylabel('y', fontsize=20)
fig.suptitle('figure 1', fontsize=20)
fig.savefig('figure_multiplelines.png')