def solution(number):
    print('number is', number)
    i = 0
    int_list=[]
    
    while 1:
        if i < number:
            if i in int_list:
                i += 3
                continue
            else:
                int_list.append(i)
                i += 3
        else:
            break

    i = 0
    while 1:
        if i < number:
            if i in int_list:
                i += 5
                continue
            else:
                int_list.append(i)
                i += 5
        else:
            break
    if i > number: print('yes')
    print(sum(int_list))
    return sum(int_list)
    
    # tried doing slightly different method. it seemed more efficient, though its still roughly the same.
    # the buffer still overflows for a large solution (7575)
    # by removing the console debug output it makes it use less memory.
    # completed in 1.79ms 