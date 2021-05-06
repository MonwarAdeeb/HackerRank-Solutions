#!/bin/python3

import math
import os
import random
import re
import sys

time = input().strip()
hour, minute, second = map(int, time[:-2].split(':'))
meridiem = time[-2:]

hour = hour % 12 + (meridiem.upper() == 'PM') * 12

print(('%02d:%02d:%02d') % (hour, minute, second))
