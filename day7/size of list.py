size=int(input("enter the size of list:"))
wordList=[]
for i in range(size):
    val=input("enter the word:")
    wordList.append(val)
print("user entered List is:",wordList)
len=list(map(lambda w:len(w),wordList))
print("length of the words in the list :",len)
