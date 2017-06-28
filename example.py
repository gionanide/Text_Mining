#!usr/bin/python
#First example
#introduction to text mining Level : Begginer
print('First text mining example by Gionanide:')

print('The text of the input file is the following:')
with open('/home/manos/test','r') as inputFIle:
    for line in inputFIle.readlines():
        print line

negativeWords =['ugly', 'awful']
positiveWords=['beautiful','delicious']
emotionalWords=negativeWords+positiveWords

words = line.split(' ')
print(words)
print('after split:')
print(len(words))
print('before split:')
print(len(line))

for word in words:
    if word in negativeWords:
        print('Negative text has been detected')
        print(word)




#Second example checking the frequency of the words, with this way you are able
#to make conlcusions for the most common use words'''
import textmining
import numpy as np
import operator

# Create some very short sample documents
doc1 = 'John and Bob are brothers.'
doc2 = 'John went to the store. The store was closed.'
doc3 = 'Bob went to the store too.'
# Initialize class to create term-document matrix
tdm = textmining.TermDocumentMatrix()
# Add the documents
tdm.add_doc(doc1)
tdm.add_doc(doc2)
tdm.add_doc(doc3)
# Write out the matrix to a csv file. Note that setting cutoff=1 means
# that words which appear in 1 or more documents will be included in
# the output (i.e. every word will appear in the output). The default
# for cutoff is 2, since we usually aren't interested in words which
# appear in a single document. For this example we want to see all
# words however, for this we are going to us  cutoff=1.
tdm.write_csv('matrix.csv', cutoff=1)
# Instead of writing out the matrix we can also access its rows directly.
# Let's print them to the screen.
mostCommonWord = [0]*12
i=1
#make a sum of the words of the three sentences
for row in tdm.rows(cutoff=1):
    if(i>1):
    	for i in range(0,12):
		mostCommonWord[i]+=row[i]
    print row
    i+=1
print(mostCommonWord)
#convert numpy array to list structure python
np.array(mostCommonWord).tolist()
print('The most common word is: ')
for row in tdm.rows(cutoff=1):
#find the max in the list and print the word in this position
	index, value = max(enumerate(mostCommonWord), key=operator.itemgetter(1))
	print row[index]
#break the loop
#we have to make a loop because only the in the first loop we can get the words and the we get the amount
	break
