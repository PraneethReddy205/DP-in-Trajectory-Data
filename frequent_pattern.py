from prefixspan import PrefixSpan


def read_sequences_from_file(file_path):
    sequences = []
    with open(file_path, 'r') as file:
        for line in file:
            sequence = line.strip().split(',') 
            sequences.append(sequence)
    return sequences


file_path = 'Trajectory_Dataset_final.txt' 
sequences = read_sequences_from_file(file_path)


formatted_sequences = [[str(item) for item in sequence] for sequence in sequences]

ps = PrefixSpan(formatted_sequences)
patterns = ps.frequent(2)  

sorted_patterns = sorted(patterns, key=lambda x: x[1], reverse=True)

topk_original=[]
cnt=0
max_height=7
top_k=200
for i, (pattern, support) in enumerate(sorted_patterns, start=1):
    
    if len(support)<=max_height:
        # print(support)
        topk_original.append(support)
        cnt+=1
    if cnt==top_k:
        break

file_path = 'Sanitized_data.txt'  
sequences = read_sequences_from_file(file_path)


formatted_sequences = [[str(item) for item in sequence] for sequence in sequences]


ps = PrefixSpan(formatted_sequences)
patterns = ps.frequent(2)  

sorted_patterns = sorted(patterns, key=lambda x: x[1], reverse=True)

topk_sanitized=[]
cnt=0
for i, (pattern, support) in enumerate(sorted_patterns, start=1):
    
    if len(support)<=max_height:
        # print(support)
        topk_sanitized.append(support)
        cnt+=1
    if cnt==top_k:
        break

cnt=0
for seq in topk_original:
    if seq in topk_sanitized:
        cnt+=1

print("Number of matches in top",top_k,"frequent patterns :",cnt)