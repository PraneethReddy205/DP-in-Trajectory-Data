import os
import math
import numpy as np
from queue import Queue

def findheight(node):
    if len(node.children) == 0:
        return 1
    maxj=1
    for child in node.children:
        j=findheight(child)
        if j+1>maxj:
            maxj=j+1
    return maxj
        

def laplace_noise(original_value,  epsilon):
    scale = 1 / epsilon
    u = 0
    laplace_sample = -np.sign(u) * scale * np.log(1 - 2 * np.abs(u))
    noisy_value = original_value + laplace_sample
    return noisy_value


def prefixcount(prefix,root):
    arr=prefix.strip().split(',')
    root1=root
    till = root1.value+','
    for point in arr:
        till = till + point+','
        for child in root1.children:
            if child.value == till:
                root1 = child         
    return root1.count

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.count = 1
        self.height = 0
        self.children = []  

    def add_child(self, child_node):
        self.children.append(child_node)
        child_node.count = 1

ifile = open("Trajectory_Dataset_final.txt")
ofile=open("Sanitized_data.txt","w")
root = TreeNode('0')
count_traj=0
sum_len_record=0
for line in ifile:
    root1 = root
    arr = line.strip().split(',')
    till = root1.value+','
    sum_len_record+=len(arr)
    count_traj+=1
    for point in arr:
        till = till + point+','
        found = False
        for child in root1.children:
            if child.value == till:
                child.height=root1.height+1
                root1 = child
                root1.count += 1
                found = True
                break
        if not found:
            node_till = TreeNode(till)
            root1.add_child(node_till)
            node_till.height=root1.height+1
            root1 = node_till

# print(prefixcount("1,2",root))
# for child in root.children:
#             print(child.height)
#             print(laplace_noise(child.count,1/5))


set_height = 6
budget = 0.5
theta_threshold = 2*math.sqrt(2)/budget*set_height

curr_height=0
q = Queue(maxsize = 1000000)
q.put(root)
while (not q.empty()) and curr_height<=set_height:
    root1=q.get()
    new_children=[]
    for child in root1.children:
        tillx=child.value
        if child.height==set_height:
            child.children=[]
        noisy_count=laplace_noise(child.count,budget/set_height)
        if noisy_count >= theta_threshold:
            new_children.append(child)
            curr_height=child.height
            q.put(child)
            child.count=int(noisy_count)
            # print(tillx)
            # print(str(child.count)+"and"+str(noisy_count))
            # print(str(noisy_count)+"is greater than "+str(theta_threshold))
        # else:
        #     print(tillx)
        #     print(str(child.count)+"and"+str(noisy_count))
        #     print(str(noisy_count)+"is less than "+str(theta_threshold))
    root1.children=new_children



bfsq = Queue(maxsize = 100000)
bfsq.put(root)
while not bfsq.empty():
    root1=bfsq.get()
    if len(root1.children)==0:
        for i in range(root1.count):
            ofile.write(root1.value[2:-1]+'\n')
    for child in root1.children:
        bfsq.put(child)

ifile.close()
ofile.close()