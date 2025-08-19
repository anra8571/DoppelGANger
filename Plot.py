import matplotlib.pyplot as plt
import numpy

averages_ori = numpy.load('averages_original_data.npy')
averages = numpy.load('averages_generated_data.npy')
# print(f"Averages: {averages.shape}")


plt.hist(averages_ori, bins=100, range=[-1, 1], color='blue', alpha=0.5)
plt.hist(averages, bins=100, range=[-1, 1], color='orange', alpha=0.5)
plt.legend(['Original Data', 'Generated Data'])
plt.show()