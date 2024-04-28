import os

ifile=open("Trajectory_Dataset.txt")
ofile=open("Trajectory_Dataset_final.txt","w")
nums=[]
for line in ifile:
    line=line.split(':')[0]
    line=line.split(',')
    line=[x.split('.')[0] for x in line]
    fline=""
    for word in line:
        if word[1:] not in nums:
            nums.append(word[1:])
        fline=fline+word[1:]+','
    fline=fline[0:-1]
    ofile.write(fline+"\n")
ifile.close()
ofile.close()
nums=[int(s) for s in nums]
nums.sort()
print('Locations in Given Database:')
print(nums)

