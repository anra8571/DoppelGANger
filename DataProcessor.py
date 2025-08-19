import settings
import numpy
import matplotlib.pyplot as plt

def average_min_max(data_path, save_path, notification_frequency=1000):
    generated_data = numpy.load(data_path)

    # Figure 6 - (max+min)/2 for each feature
    averages_arr = numpy.zeros(shape=(len(generated_data['data_feature']),), dtype=float)
    for i in range(0, len(generated_data['data_feature'])):
        if i % notification_frequency == 0:
            print(f"Processing sample {i}")
        max = numpy.max(generated_data['data_feature'][i])
        min = numpy.min(generated_data['data_feature'][i])
        average = (max + min) / 2
        # print(average)
        averages_arr[i] = average

    # print(averages_arr)
    numpy.save(save_path, averages_arr)
    print(f"Averages: {averages_arr.shape}")