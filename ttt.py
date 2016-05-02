from nltk.tokenize import sent_tokenize, word_tokenize
fileName = input("Enter file name: ")
f = open(fileName)
raw = f.read()



print(sent_tokenize(raw))
print(word_tokenize(raw))
print('number of sentences equal',len(sent_tokenize(raw)))
print('number of words equal',len(word_tokenize(raw)))


average =(len(word_tokenize(raw))/len(sent_tokenize(raw)))
print('average word per senetnces eqauls',average)
