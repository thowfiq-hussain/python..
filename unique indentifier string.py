user=input("enter the sentence:")
words=user.split()
unique_words=[ ]
for word in words:
    if words.count(word)>1 and word not in unique_words:
        unique_words.append(word)
        if len(unique_words )>0:
            print("unique words was found",unique_words)
        else:
                print("unique words was not found")
