import os
import csv
from collections import Counter
import statistics

csvpath = os.path.join('C:\\Users\\cdj3e\\vu_bootcamp\\Python\\Module_3_Challenge\\python_challenge\\PyBank\\resources\\budget_data.csv')

input_list = ["Jan-10", "Feb-10", "Mar-10", "Apr-10", "May-10", "Jun-10", "Jul-10", "Aug-10", "Sep-10", "Oct-10", "Nov-10", "Dec-10", "Jan-11", "Feb-11", "Mar-11", "Apr-11", "May-11", "Jun-11", "Jul-11", "Aug-11", "Sep-11", "Oct-11", "Nov-11", "Dec-11", "Jan-12", "Feb-12", "Mar-12", "Apr-12", "May-12", "Jun-12", "Jul-12", "Aug-12", "Sep-12", "Oct-12", "Nov-12", "Dec-12", "Jan-13", "Feb-13", "Mar-13", "Apr-13", "May-13", "Jun-13", "Jul-13", "Aug-13", "Sep-13", "Oct-13", "Nov-13", "Dec-13", "Jan-14", "Feb-14", "Mar-14", "Apr-14", "May-14", "Jun-14", "Jul-14", "Aug-14", "Sep-14", "Oct-14", "Nov-14", "Dec-14", "Jan-15", "Feb-15", "Mar-15", "Apr-15", "May-15", "Jun-15", "Jul-15", "Aug-15", "Sep-15", "Oct-15", "Nov-15", "Dec-15", "Jan-16", "Feb-16", "Mar-16", "Apr-16", "May-16", "Jun-16", "Jul-16", "Aug-16", "Sep-16", "Oct-16", "Nov-16", "Dec-16", "Jan-17", "Feb-17"]
items = Counter(input_list).keys()
print("The total number of months is " + str(len(items)))

index = {}
file = open('C:\\Users\\cdj3e\\vu_bootcamp\\Python\\Module_3_Challenge\\python_challenge\\PyBank\\resources\\budget_data.csv')
myreader = csv.DictReader(file)
profit_loss = list((1088983, -354534, 276622, -728133, 852993, 563721, -535208, 632349, -173744, 950741, -785750, -1194133, -589576, -883921, 443564, 837887, 1081472, 464033, -1066544, 323846, -806551, 487053, 1128811, 791398, 739367, -197825, 666016, 589771, 489290, -471439, 120417, 175347, 855449, 605195, -235220, 347138, 298510, 163254, 1141840, 542630, 99841, 752765, -252949, 914424, 679524, 514377, 462102, 159782, 878810, -946748, 340335, 292032, 502266, 265852, 851017, -549615, 290162, 755391, 1073202, 313000, 241132, 1036589, 853904, -388932, 982952, 537759, 547784, -496214, 854181, 934719, -288531, -184383, 659541, -1149123, 355882, 662284, 518681, -748256, -910775, 951227, 898241, -729004, -112209, 516313, 607208, 382539))

for column in myreader: 
    profit_loss.append(float(column['Profit/Losses']))
print("The total profit is $", sum(profit_loss))