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