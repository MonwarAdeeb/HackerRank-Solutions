# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics
from scipy import stats

#Taking inputs
i = int(input())

my_list = []

my_list = list(map(int,input().split()))


#Mean
mean = float(statistics.mean(my_list))
print(mean)

#Median
median = float(statistics.median(my_list))
print(median)

#Mode
mode = int(stats.mode(my_list)[0])
print(mode)
