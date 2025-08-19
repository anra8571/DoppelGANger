# DoppelGANger
See original implementation [here](https://github.com/fjxmlzn/DoppelGANger), tested for Python 2.7.5, Python 3.5.2, and TensorFlow 1.4.0.

This version used TensorFlow's [migration tool](https://www.tensorflow.org/guide/migrate) to update the repositoryto TensorFlow 2.12 using Python 3.9.13.

## Replicating Figure 6
Run average_min_max() in DataProcessor.py for each dataset to compare (such as the original data and generated data). This will calculate the (max + min)/2 value for each time series, then store the values in a npy file. Then, run Plot.py to generate the plot using the new npy files.

## Citation
Zinan Lin, Alankar Jain, Chen Wang, Giulia Fanti, and Vyas Sekar. 2020. Using GANs for Sharing Networked Time Series Data: Challenges, Initial Promise, and Open Questions. In Proceedings of the ACM Internet Measurement Conference (IMC '20). Association for Computing Machinery, New York, NY, USA, 464–483. https://doi.org/10.1145/3419394.3423643
