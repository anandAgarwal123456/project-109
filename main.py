import plotly.figure_factory as ff
import plotly.graph_objects as go
import csv
import pandas as pd
import statistics


df = pd.read_csv("StudentsPerformance.csv")
reading_data = df["reading_score"].tolist()
math_data = df["math_score"].tolist()


mean = statistics.mean(reading_data)
median = statistics.median(reading_data)
mode = statistics.mode(reading_data)
stdev = statistics.stdev(reading_data)

mean2 = statistics.mean(math_data)
median2 = statistics.median(math_data)
mode2 = statistics.mode(math_data)
stdev2 = statistics.stdev(math_data)

print("mean , mode, median of reading data is {},{} and {} respecitvely:".format(mean,mode,median))
print("mean , mode, median of maths data is {},{} and {} respecitvely:".format(mean2,mode2,median2))

# READING SCORES
reading_first_stdev_start, reading_first_stdev_end = mean - stdev, mean + stdev
reading_second_stdev_start, reading_second_stdev_end = mean-(2* stdev), mean+(2* stdev)
reading_third_stdev_start, reading_third_stdev_end = mean-(3*stdev), mean+(3* stdev)

reading_list_data_within_first_stdev = [result for result in reading_data if result > reading_first_stdev_start and result < reading_first_stdev_end]
reading_list_data_within_second_stdev = [result for result in reading_data if result > reading_second_stdev_start and result < reading_second_stdev_end]
reading_list_data_within_third_stdev = [result for result in reading_data if result > reading_third_stdev_start and result < reading_third_stdev_end]

#MATHS SCORE
maths_first_stdev_start, maths_first_stdev_end = mean2 - stdev2, mean2 + stdev2
maths_second_stdev_start, maths_second_stdev_end = mean2-(2* stdev2), mean+(2* stdev2)
maths_third_stdev_start, maths_third_stdev_end = mean2-(3*stdev2), mean2+(3* stdev2)

maths_list_data_within_first_stdev = [result for result in math_data if result > maths_first_stdev_start and result < maths_first_stdev_end]
maths_list_data_within_second_stdev = [result for result in math_data if result > maths_second_stdev_start and result < maths_second_stdev_end]
maths_list_data_within_third_stdev = [result for result in math_data if result > maths_third_stdev_start and result < maths_third_stdev_end]


print("{}% of data for reading lies within first standard deviation".format(len(reading_list_data_within_first_stdev)*100.0/len(reading_data)))
print("{}% of data  for reading lies within second standard deviation".format(len(reading_list_data_within_second_stdev)*100.0/len(reading_data)))
print("{}% of data for reading lies within third standard deviation".format(len(reading_list_data_within_third_stdev)*100.0/len(reading_data)))

print("{}% of data for maths lies within first standard deviation".format(len(maths_list_data_within_first_stdev)*100.0/len(math_data)))
print("{}% of data  for maths lies within second standard deviation".format(len(maths_list_data_within_second_stdev)*100.0/len(math_data)))
print("{}% of data for maths lies within third standard deviation".format(len(maths_list_data_within_third_stdev)*100.0/len(math_data)))







