import os
ifile = open("Trajectory_Dataset_final.txt")
ofile=open("Sanitized_data.txt")

node_dict={}
cnt=0
for line in ifile:
    arr = line.strip().split(',')
    temp_dict={}
    for point in arr:
        temp_dict[point]=1
    for x in temp_dict:
        if x in node_dict:
            node_dict[x]+=temp_dict[x]
        else:
            node_dict[x]=temp_dict[x]
    cnt+=1

node_dict_sanitized={}
cnt=0
for line in ofile:
    arr = line.strip().split(',')
    temp_dict={}
    for point in arr:
        temp_dict[point]=1
    for x in temp_dict:
        if x in node_dict_sanitized:
            node_dict_sanitized[x]+=temp_dict[x]
        else:
            node_dict_sanitized[x]=temp_dict[x]
    cnt+=1
    
query='2'   
total_query_error=0
for i in range(20): 
    query=str(i+1)
    # print(query)
    # if query in node_dict:    
        # print(node_dict[query])
    # else:
        # print("queried node not present in original data")
    # if query in node_dict_sanitized:  
        # print(node_dict_sanitized[query])
    # else:
        # print("queried node not present in sanitized data")
    total_query_error+=(node_dict[query]-node_dict_sanitized[query])/node_dict[query]

avg_query_error=total_query_error/20
print(avg_query_error)
ifile.close()
ofile.close()