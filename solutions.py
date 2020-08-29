########################### 1st program ###################################
def printnumbers():
    # N = int(input())
    N = 17
    print("Input",N)
    print("Output")
    for i in range(1,N):
        # print(i)
        if ((i%3)==0 and (i%5)==0):
            # print("divided by three & five {} ".format(i))
            print("FizzBuzz")
        elif (i%3)==0 :
            # print("divided by three {} ".format(i))
            print("Fizz")
        elif (i%5)==0:
            # print("divided by five {} ".format(i))
            print("Buzz")

        else:
            print(i)

printnumbers()

################################ 2nd program ###############################
from collections import Counter
Inputs = [1, 2, 3, 5, 8, 4, 7, 9, 1, 4, 12, 5, 6, 5, 2, 1, 0, 8, 1]
print("\n\nInput",Inputs)
print("Output",Counter(Inputs))

############################### 3rd program ################################

def add_dic_val(input_dict):
    
    print("\n\nInput : ",input_dict)
    sum_of_all_values = sum(input_dict.values())
    print("Output",sum_of_all_values)

input_dict ={"Rick": 85, "Amit": 42, "George": 53, "Tanya": 60, "Linda": 35}
add_dic_val(input_dict)
    
################################### 4th program #################################

class Batsman_score_calculator(object):
    def __init__(self):
        self.player_1 = []
        self.player_2 = []
        self.player_1_total=[]
        self.player_2_total=[]
    def cric_(self,input):
        print("\nInput : ",input)
        for i,v in enumerate(input):
            z = i+1
            ####################### for first ball ###########################
            if 1==z:
                # print("############################# First over ##########################")
                if v==1 or v ==3 :
                    # print("\tplayer_1 socres        --- > ball {} score {}".format(z,v))
                    self.player_1.append(v)
                    self.player_1_total.append(v)
                elif v==2 or v==4 or v==6 or v==0:
                    # print("\tplayer_1 socres        --- > ball {} score {}".format(z,v))
                    self.player_1.append(v)
                    self.player_1_total.append(v)

            ###################### middle  ############################
            if z>1 and (z%7)!=0 :
                if len(self.player_1)>=1:
                    for p1 in self.player_1:
                        if p1 ==1 or p1 ==3:
                            if v==1 or v ==3 :
                                # print("\tplayer_2 socres  p1 2-1 --- > ball {} score {}".format(z,v))
                                self.player_1.pop()
                                self.player_2.append(v)
                                self.player_2_total.append(v)
                            elif v==2 or v==4 or v==6 or v==0:
                                # print("\tplayer_2 socres  p1 2-2--- > ball {} score {}".format(z,v))
                                self.player_1.pop()
                                self.player_2.append(v)
                                self.player_2_total.append(v)
                        elif p1==2 or p1 ==4 or p1 ==6 or p1==0:
                            if v==1 or v ==3 :
                                # print("\tplayer_1 socres  p1 1-1 --- > ball {} score {}".format(z,v))
                                self.player_1.pop()
                                self.player_1.append(v)
                                self.player_1_total.append(v)
                            elif v==2 or v==4 or v==6 or v==0:
                                # print("\tplayer_1 socres  p1 1-2 --- > ball {} score {}".format(z,v))
                                self.player_1.pop()
                                self.player_1.append(v)
                                self.player_1_total.append(v)
                        
                elif len(self.player_2)>=1:
                    for p2 in self.player_2:
                        if p2 ==1 or p2 ==3:
                            if v==1 or v ==3 :
                                # print("\tplayer_1 socres  p2 1-1--- > ball {} score {}".format(z,v))
                                self.player_2.pop()
                                self.player_1.append(v)
                                self.player_1_total.append(v)
                            elif v==2 or v==4 or v==6 or v==0:
                                # print("\tplayer_1 socres  p2 1-2--- > ball {} score {}".format(z,v))
                                self.player_2.pop()
                                self.player_1.append(v)
                                self.player_1_total.append(v)
                        elif p2==2 or p2 ==4 or p2 ==6 or p2==0:
                            if v==1 or v ==3 :
                                # print("\tplayer_2 socres  p2 2-2 --- > ball {} score {}".format(z,v))
                                self.player_2.pop()
                                self.player_2.append(v)
                                self.player_2_total.append(v)
                            elif v==2 or v==4 or v==6 or v==0:
                                # print("\tplayer_2 socres  p2 2-2--- > ball {} score {}".format(z,v))
                                self.player_2.pop()
                                self.player_2.append(v)
                                self.player_2_total.append(v)
                    
                #################### for new over ####################
            if (z%7)==0:
                # print("######################## Every New over #############################")
                if len(self.player_1)>=1:
                    for p1 in self.player_1:
                        if p1 ==1 or p1 ==3:
                            if v==1 or v ==3 :
                                # print("\tplayer_1 socres  p1 2-1 --- > ball {} score {}".format(z,v))
                                self.player_1.pop()
                                self.player_1.append(v)
                                self.player_1_total.append(v)
                            elif v==2 or v==4 or v==6 or v==0:
                                # print("\tplayer_1 socres  p1 2-2--- > ball {} score {}".format(z,v))
                                self.player_1.pop()
                                self.player_1.append(v)
                                self.player_1_total.append(v)
                        elif p1==2 or p1 ==4 or p1 ==6 or p1==0:
                            if v==1 or v ==3 :
                                # print("\tplayer_2 socres  p1 1-1 --- > ball {} score {}".format(z,v))
                                self.player_1.pop()
                                self.player_2.append(v)
                                self.player_2_total.append(v)
                            elif v==2 or v==4 or v==6 or v==0:
                                # print("\tplayer_2 socres  p1 1-2 --- > ball {} score {}".format(z,v))
                                self.player_1.pop()
                                self.player_2.append(v)
                                self.player_2_total.append(v)
                        
                elif len(self.player_2)>=1:
                    for p2 in self.player_2:
                        if p2 ==1 or p2 ==3:
                            if v==1 or v ==3 :
                                # print("\tplayer_2 socres  p2 1-1--- > ball {} score {}".format(z,v))
                                self.player_2.pop()
                                self.player_2.append(v)
                                self.player_2_total.append(v)
                            elif v==2 or v==4 or v==6 or v==0:
                                # print("\tplayer_2 socres  p2 1-2--- > ball {} score {}".format(z,v))
                                self.player_2.pop()
                                self.player_2.append(v)
                                self.player_2_total.append(v)
                        elif p2==2 or p2 ==4 or p2 ==6 or p2==0:
                            if v==1 or v ==3 :
                                # print("\tplayer_1 socres  p2 2-2 --- > ball {} score {}".format(z,v))
                                self.player_2.pop()
                                self.player_1.append(v)
                                self.player_1_total.append(v)
                            elif v==2 or v==4 or v==6 or v==0:
                                # print("\tplayer_1 socres  p2 2-2--- > ball {} score {}".format(z,v))
                                self.player_2.pop()
                                self.player_1.append(v)  
                                self.player_1_total.append(v)
        print("Output:")
        print("Batsman 1 Score : {} --->: {}".format(sum(self.player_1_total),self.player_1_total))
        print("Batsman 2 Score : {} --->: {}".format(sum(self.player_2_total),self.player_2_total))



cric_score = [1,2,0,0,4,1,6,2,1,3]

cri = Batsman_score_calculator()
cri.cric_(cric_score)   

####################### 5th program ######################################################

#Counting String if tie means using lexicographically
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    counts_x = sorted(counts.items(), key=lambda kv: kv[1])
    f = counts_x[-1]
    s = counts_x[-2]
    k,v = counts_x[-1]
    k2,v2 = counts_x[-2]
    l=[]
    
    if v == v2:
        l.append(k)
        l.append(k2)
        l.sort()
        print("\nOutput :")
        print("\tTie in the given string so using lexicographically order")
        print("\t",l)
    else:
        print("\nOutput :")
        print("\tThe most in the given string")
        print("\t",counts_x[-1])
        
########### get input from user ##################### 
# inp = str(input("\nEnter the input string : " ))
# word_count(inp)

############ passing direct input ####################
print(word_count("hey hi how are hey hell heat honey  hi hi hi"))