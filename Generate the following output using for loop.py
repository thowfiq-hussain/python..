output = "a"
for letter in range(ord('b'), ord('h')):
    output += chr(letter) + output
    print(output)
