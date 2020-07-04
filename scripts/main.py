def pattern_f():
    return [
        ''.join([
            'F' if (col == 0 or col == 1 or row == 0 or row ==2) else ' '
            for col in range(7)]) for row in range(5)
    ]

def pattern_u():
    return [
        ''.join([
            'U' if ((col==0 or col==6) and row<3) or (row==3 and (col==1 or col==5)) or (row==4 and col>1 and col<5) else ' '
            for col in range(7)]) for row in range(5)
    ]

def pattern_n():
    return [
        ''.join([
            'N' if (col==0 or col==1 or col==6 or col==7) or (row==col-1) else ' '
            for col in range(7)]) for row in range(5)
    ]

if __name__ == "__main__":
    ##separate printing:
    for string in pattern_f():
        print(string)
    print()

    for string in pattern_u():
        print(string)
    print()

    for string in pattern_n():
        print(string)    
    print()