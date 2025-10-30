'''
meetings = [3,4,6,1]
print(meetings)
meetings.append(10)
print(meetings)
#----------------------
total = 0
for i in range(len(meetings)):
    print(i, meetings[i])
    total += meetings[i]
    
print("The average number of people at a meeting: " + str(round(total/len(meetings))))   
'''

import random

meeting = []
for i in range(4):
    rand = random.randint(1,50)
    meeting.append(rand)
    
print(meeting)    

