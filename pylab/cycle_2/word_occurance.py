text=input("ENTER A LINE OF TEXT\n")
words=text.split()
word_count={}
for word in words:
	words=word.lower()
	if words in word_count:
		word_count[word]+=1
	else:
		word_count[word]=1
print("WORD OCCURANCE",word_count)
