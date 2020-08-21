#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    print(len(max(re.split("0+",bin(int(input().strip()))[2:]))))

