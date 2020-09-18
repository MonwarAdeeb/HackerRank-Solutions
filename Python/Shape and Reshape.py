import numpy

my_array = numpy.array(map(int, raw_input().split()))
print numpy.reshape(my_array, (3, 3))
