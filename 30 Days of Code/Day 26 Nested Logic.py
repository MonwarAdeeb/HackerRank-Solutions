# Enter your code here. Read input from STDIN. Print output to STDOUT
import datetime

r_date = list(map(int, (input().split())))
e_date = list(map(int, (input().split())))

return_date = datetime.datetime(r_date[2], r_date[1], r_date[0])
expected_date = datetime.datetime(e_date[2], e_date[1], e_date[0])

if return_date < expected_date:
    print("0")
else:
    day_difference = return_date - expected_date

    if (day_difference.days>0) and (r_date[1]==e_date[1]) and r_date[2]==e_date[2]:
        fine = day_difference.days * 15
        print(fine)
    elif (day_difference.days>0) and (r_date[1]>e_date[1]) and r_date[2]==e_date[2]:
        months_late = r_date[1] - e_date[1]
        fine = months_late * 500
        print(fine)
    else:
        print("10000")