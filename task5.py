word1 = input("enter word1: ")
word2 = input("enter word2: ")

if sorted(word1.lower()) == sorted(word2.lower()):
    print("anagram")
else:
    print("not anagram")
