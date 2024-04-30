sentence = input("Type Something\n")
result = {word: len(word) for word in sentence.split()}
print(result)
