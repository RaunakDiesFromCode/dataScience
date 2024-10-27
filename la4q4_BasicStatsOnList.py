# write a program to return mean, median, mode, variance, and standard deviation of a list of numbers using statistics module

import statistics

# Define a sample list
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calculate the mean
mean = statistics.mean(sample_list)
print("Mean:", mean)

# Calculate the median
median = statistics.median(sample_list)
print("Median:", median)

# Calculate the mode
mode = statistics.mode(sample_list)
print("Mode:", mode)

# Calculate the variance
variance = statistics.variance(sample_list)
print("Variance:", variance)

# Calculate the standard deviation
std_dev = statistics.stdev(sample_list)
print("Standard Deviation:", std_dev)

