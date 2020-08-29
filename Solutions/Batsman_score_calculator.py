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
