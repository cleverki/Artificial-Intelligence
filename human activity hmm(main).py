import hmm
import sys
import extra

'''
1 : WALKING
2 : WALKING UPSTAIR
3 : WALKING DOWNSTAIR
4 : SITTING
5 : STANDING
6 : LAYING
choose which action analyzed
choose number of symbols
'''

activity = [['1', '2', '3'], ['4','5', '6']]
num_of_symbol = 2
user_num = '1'

data_set = extra.get_data(activity, user_num)
num_of_state = len(activity)

##setting HMM
states = []
for i in range(num_of_state):
    states.append(i)
states = tuple(states)

symbols = []
for i in range(num_of_symbol):
    symbols.append(i)
symbols = tuple(symbols)

model = hmm.Model(states, symbols)

##training HMM
'''choose partition, # of partition + 1 = number of symbols'''
partition = [0.98]
if len(partition) + 1 != num_of_symbol:
    print("Wrong partition or Wrong num_of_symbol")
    sys.exit()
    
'''adjust type'''    
type = "acc"
aver_num = 20

observed_seq = []
given_seq = []
for data in data_set:
    observed_seq, given_seq = extra.get_sequences(data, type, aver_num,\
                                            partition, observed_seq, given_seq)

count = [[0 for i in range(num_of_symbol)], [0 for i in range(num_of_symbol)]]
for i in range(len(observed_seq)):
    count[given_seq[i]][observed_seq[i]]+=1

for k in count:
    s = sum(k)
    for j in range(len(k)):
        k[j] /= s
        k[j] = float(int(k[j]*10000))/100

#print(partition, count)


model = hmm.train([(given_seq, observed_seq)])
    
##Analysis HMM
right_count = 0
for data in data_set:
    observed_seq = []
    given_seq = []
    given_state = data[2]
    
    observed_seq, given_seq = extra.get_sequences(data, type, aver_num,\
                                            partition, observed_seq, given_seq)

    forward_seq = model._forward(observed_seq)
    last_state = extra.last_max_state(forward_seq)

    if last_state == given_state:
        right_count += 1
    #print(given_state, last_state, forward_seq[len(forward_seq)-1])

print(right_count/len(data_set))

