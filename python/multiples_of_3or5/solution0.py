def solution(number):
    i = 0
    int_list=[]
    while i < number:
        print(i, ' : ', int_list)
        if (i % 3) == 0:
            int_list.append(i)
        elif (i % 5) == 0:
            print("i % 5 condition met")
            int_list.append(i)
        i += 1
    # remember to return values ...
    return sum(int_list)
    
    # original method of solving NOTE: the max buffer size gets reached, so we should probably write an algorithm to optimzie this. 
    # completed in 1.86 ms