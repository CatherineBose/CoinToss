import random

def tossCoin():
    countHeads = 0 
    countTails = 0
    # myList = ["Head", "Tail"]
    # random.choice(myList)
    for i in range (1,10):
        toss= random.random()
        # print "toss random no: ", toss
        toss = round(toss)
        # print "toss random no: rounded ", toss
        if toss ==1:
            countHeads += 1
            print"Attempt #{}: Throwing a coin... It's a head! ... Got {} head(s) so far and {} tail(s) so far".format(i,countHeads,countTails)
        elif toss == 0:
            countTails += 1
            print"Attempt #{}: Throwing a coin... It's a tail! ... Got {} head(s) so far and {} tail(s) so far".format(i,countTails,countHeads)


tossCoin()