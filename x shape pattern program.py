def pattern_program() :
    letters="program"
    length=len(letters)
    for i in range (length):
        for j in range (length):
            if j==i or j==length-i-1:
                print(letters[j],end="")
            else:
                print(" ",end="")
        print()
pattern_program()