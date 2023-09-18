fruit_basket=input("enter the unique fruits:")
words=fruit_basket.lower().split()
unique_fruits=[ ]
for word in words:
    if words.count(word)>1 and word not in unique_fruits:
        unique_fruits.append(word)
        if len(unique_fruits )>0:
            print("unique fruits was found",unique_fruits)
        else:
                print("unique fruits was not found")
