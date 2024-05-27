#Created By Ritu Raj

# calculate average temperatures

# taking input from user in integer format
'''
output:--
average temp and total count of temp gt than avg temp

input :--
no of days for calculating the avg
and temperature for each day

'''

numDays = int(input('How many days temperatures ? '))
total = 0
temp = []
for i in range(numDays):
    nextDay = int(input(f"day {i+1} 's high temperature :- "))
    temp.append(nextDay)
    total+= temp[i]

avg = round(total/numDays, 2)
print(f"average temp {avg}")

count_gt_avg_temp =0
for i in temp:
    if i >avg:
        count_gt_avg_temp +=1

print(f"{count_gt_avg_temp} above average")



