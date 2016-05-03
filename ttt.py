from nltk.tokenize import sent_tokenize, RegexpTokenizer #importing features from nltk library
fileName = input("Enter file name: ")#asks user to put .txt file into cmd
f = open(fileName,'r')
text = f.read()


tokenizer = RegexpTokenizer(r'\w+')#will make string only output words and not punctuation
N=3
acceptable_words = [x for x in tokenizer.tokenize(text) if len(x) >= N]
average =int(len(acceptable_words)/len(sent_tokenize(text)))#dividing

if text   ((".txt")):
    print(sent_tokenize(text))#all sentnces that end with (.!?)
    print(tokenizer.tokenize(text))#all words outputed
    print(acceptable_words)#is words 3 letters or more.
    print('number of sentences equal',len(sent_tokenize(text)))
    print('number of words equal',len(tokenizer.tokenize(text)))
    print('number of acceptable words is',len(acceptable_words))
    print('average word per senetnces eqauls',average)
else:
    print("Extension must be a .txt file")




