import csv

f=open("path/Transportation card statistics.csv")
main_data = csv.reader(f)

subways=[]
for idx, row in enumerate(main_data):
    subways.append(row)
f.close()

'''
출근시간(7:00~9:00)에 하차 인원이 가장 많은 역이 어디인가?
index 11 13 15
'''

index=0

def add_staytion(row1,row2,row3):
    return int(row1.replace(',', ''))+ int(row2.replace(',', '')) + int(row3.replace(',', ''))

max=0

for idx, row in enumerate(subways[2:]):
    if max<add_staytion(row[11],row[13],row[15]):
        max = add_staytion(row[11],row[13],row[15])
        index=idx+2

print(subways[index][1],subways[index][3],
      subways[index][11],subways[index][13],subways[index][15])
print(max)
