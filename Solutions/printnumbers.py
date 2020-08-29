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