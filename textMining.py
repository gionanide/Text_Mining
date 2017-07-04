#text example
#make the POS-Tagger Function
def pos_tag(sentences):
	pos = [nltk.pos_tag(sentence) for sentence in sentences]
	#adapt format
	pos = [[(word, word, [postag]) for (word, postag) in sentence] for sentence in pos]
	return pos

#iterate all the sentences
# I use two list for negative and positive words because some probles with the .yml files took place(dictionaries)
#I am going to search adjectives and tag them with my dictionaries
#The posTagged is a list/array with three dimensions for example posTagged[0][0][0] , the first 0 is for the first sentence,
#the second zero is for the first word in this sentence and the thris zero is for this word the argument i want to take
#because in my first approach i am going to check only the adjectives i search only for this checking the thrid dimension
#for example adjective = JJ , i only check the JJ words and enrich the word with an extra tag (negative,positive)
def DictionaryTagger(listA):
	negativeWords = ['bad','uninspired','expensive','dissapointed',]
	positiveWords = ['nice','awesome','cool','superb']
	for x in range(len(listA)):
		#check every word in the sentence
		for y in range(len(listA[x])):
			#check if the last dimension of the word is JJ , if the word is adjective
			#if(posTagged[x][y][2] == ['JJ']):
			word = listA[x][y][0]
			if word in negativeWords:
				#tag the word positive or negative
				listA[x][y][2].insert(0,'negative')
			elif word in positiveWords:
				# tag the word positive or negative
				listA[x][y][2].insert(0, 'positive')
	'''
				yaml files code, load yaml files
				import yaml
				files = [open(path, 'r') for path in dictionary_paths]
				dictionaries = [yaml.load(dict_file) for dict_file in files]
	'''
	return listA

def DictionaryTaggerIncDec(listA):
	# Incrementers and decrementers
	# same problem with the yml files so i make two tiny lists again
	inc = ['too', 'very', 'sorely']
	dec = ['barely', 'little']
	for x in range(len(listA)):
		#check every word in the sentence
		for y in range(len(listA[x])):
			#check if the last dimension of the word is JJ , if the word is adjective
			#if(posTagged[x][y][2] == ['JJ']):
			word = listA[x][y][0]
			if word in inc:
				#tag the word positive or negative
				listA[x][y][2].insert(0,'inc')
			elif word in dec:
				# tag the word positive or negative
				listA[x][y][2].insert(0, 'dec')
	'''
				yaml files code, load yaml files
				import yaml
				files = [open(path, 'r') for path in dictionary_paths]
				dictionaries = [yaml.load(dict_file) for dict_file in files]
	'''
	#print(posTagged)
	#posTagged[0][0][2].insert(0,'negative')
	return listA


def DictionaryTaggerInvPol(listA):
	# Incrementers and decrementers
	# same problem with the yml files so i make two tiny lists again
	inv = ['lack', 'not']
	for x in range(len(listA)):
		#check every word in the sentence
		for y in range(len(listA[x])):
			#check if the last dimension of the word is JJ , if the word is adjective
			#if(posTagged[x][y][2] == ['JJ']):
			word = listA[x][y][0]
			if word in inv:
				#tag the word positive or negative
				listA[x][y][2].insert(0,'inv')
				if (word == 'lack' and listA[x][y + 1][0] == 'of'):
					listA[x][y+1][2].insert(0, 'inv')
	'''
				yaml files code, load yaml files
				import yaml
				files = [open(path, 'r') for path in dictionary_paths]
				dictionaries = [yaml.load(dict_file) for dict_file in files]
	'''
	#print(posTagged)
	#posTagged[0][0][2].insert(0,'negative')
	return listA

#give some values for the positive and negative words
def value_of(sentiment):
    if sentiment == 'positive': return 1
    if sentiment == 'negative': return -1
    return 0

#more comple analysis considreing the inv , dec , inc
def sentence_score(sentence_tokens, previous_token, acum_score):
    if not sentence_tokens:
        return acum_score
    else:
        current_token = sentence_tokens[0]
        tags = current_token[2]
        token_score = sum([value_of(tag) for tag in tags])
        if previous_token is not None:
            previous_tags = previous_token[2]
			#find an inv this means the make the word stronger
            if 'inc' in previous_tags:
                token_score *= 2.0
            elif 'dec' in previous_tags:
			#finding a dec means that the emphasis of the word is weaker
                token_score /= 2.0
            elif 'inv' in previous_tags:
				#give a negative meaning in the word
                token_score *= -1.0
        return sentence_score(sentence_tokens[1:], current_token, acum_score + token_score)

def sentiment_score(review):
    return sum([sentence_score(sentence, None, 0.0) for sentence in review])

def sentiment_score(review):
    return sum([sentence_score(sentence, None, 0.0) for sentence in review])


'''
ADJ	    adjective	                    new, good, high, special, big, local
ADV	    adverb	                        really, already, still, early, now
CNJ	    conjunction	                    and, or, but, if, while, although
DET	    determiner	                    the, a, some, most, every, no
EX	    existential	                    there, there's
FW	    foreign word	                dolce, ersatz, esprit, quo, maitre
MOD	    modal verb	                    will, can, would, may, must, should
N	    noun	                        year, home, costs, time, education
NP	    proper noun	                    Alison, Africa, April, Washington
NUM	    number	                        twenty-four, fourth, 1991, 14:24
PRO	    pronoun	                        he, their, her, its, my, I, us
P	    preposition	                    on, of, at, with, by, into, under
TO	    the word to	to
UH	    interjection	                ah, bang, ha, whee, hmpf, oops
V	    verb	                        is, has, get, do, make, see, run
VD	    past tense	                    said, took, told, made, asked
VG	    present participle	            making, going, playing, working
VN	    past participle	                given, taken, begun, sung
WH	    wh determiner	                who, which, when, what, where, how

POS tag list:

CC	coordinating conjunction
CD	cardinal digit
DT	determiner
EX	existential there (like: "there is" ... think of it like "there exists")
FW	foreign word
IN	preposition/subordinating conjunction
JJ	adjective	'big'
JJR	adjective, comparative	'bigger'
JJS	adjective, superlative	'biggest'
LS	list marker	1)
MD	modal	could, will
NN	noun, singular 'desk'
NNS	noun plural	'desks'
NNP	proper noun, singular	'Harrison'
NNPS	proper noun, plural	'Americans'
PDT	predeterminer	'all the kids'
POS	possessive ending	parent's
PRP	personal pronoun	I, he, she
PRP$	possessive pronoun	my, his, hers
RB	adverb	very, silently,
RBR	adverb, comparative	better
RBS	adverb, superlative	best
RP	particle	give up
TO	to	go 'to' the store.
UH	interjection	errrrrrrrm
VB	verb, base form	take
VBD	verb, past tense	took
VBG	verb, gerund/present participle	taking
VBN	verb, past participle	taken
VBP	verb, sing. present, non-3d	take
VBZ	verb, 3rd person sing. present	takes
WDT	wh-determiner	which
WP	wh-pronoun	who, what
WP$	possessive wh-pronoun	whose
WRB	wh-abverb	where, when
 '''



text = 'What can I say about this place. The staff of the restaurant is nice and the eggplant is not bad. Apart from that, very uninspired food, lack of atmosphere and too expensive. I am a staunch vegetarian and was sorely dissapointed with the veggie options on the menu. Will be the last time I visit, I recommend others to avoid.'
#obviously we can see that this text constitutes a negative review about a restaurant
#I am going to use an approach based on dictionaries
#this means that there are negative words and other categories of words


#Building the ideal structure for the text
#there are many ways for example
#we can define the text as a list of words
#also we can define a more elaborated structure carrying every possible attribute of a processed text
import nltk



#splitting the text
#class Splitter(object):

#split the text into sentences
#and then split the sentences into words
#I will make every paragraph in POS-tagged paragraph
sentences = text.split('.')

#because i split sentences which means i split based on '.' this evoke that the last last sentence is after the last '.'
#so i take the len(stentences) - 1 in order to make a list of lists
textS = [[] for x in range(len(sentences)-1)]
#make a list of lists, which means the list is the text and the lists are the sentences
#I want to split every sentence with the gap so i make new lists
#put every sentence in the list of lists
for x in range(len(sentences)-1):
	textS[x] = sentences[x]

#the sentences is also a list of lists but in order to do this example more detailed i explain step by step
#now i am going to split every sentence based on gap ' '
for x in range(len(textS)):
	textS[x] = nltk.word_tokenize(textS[x])


#making every sentence POS-Tagged
posTagged = pos_tag(textS)
print(posTagged)

#I have already defined two tiny dictionaries for negative and positive words
#Tagging the text with dictionaries
posTagged = DictionaryTagger(posTagged)
print(posTagged)

#in this way only one function shoyld be made and check the words based on the dictionaries
#in this example because of the yml problems i make another function which test for dec or inc
posTagged = DictionaryTaggerIncDec(posTagged)
print(posTagged)

#checking the score
print(sentiment_score(posTagged))
#score -6 not a good one

#Inverters and polarity flips
#the same procedure the only fynction checking the words and find them but in our case i have to make a thrid function
#to check if this words exist
posTagged = DictionaryTaggerInvPol(posTagged)
print(posTagged)

print(sentiment_score(posTagged))
#score -4 a more accurate analysis of the text
