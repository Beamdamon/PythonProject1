from textblob import TextBlob
from textblob import Word
import random

# comments - name, assignment, estimate, actual
#Damon Beam - Python Project 1 - Expected time 5 hours - Actual time 4 hours
#Summary: I expexted the project to take around 5 hours, but I got a hang of it quicker than I thought. Once I learned more about how to use python and Textblob, it went pretty
#smoothly. I'm happy overall with how the project turned out (even if the sentences made can be a bit odd at times).



#Definite Article list of the three most common articles. Word list contains the 1000 most used words in English.
defArticleList = TextBlob("A The")
wordList = TextBlob(" of to and in is it you that he was for on are with as I his they be at one have this from or had by not word but what some we can out other were all there when up use your how said an each she which do their time if will way about many then them write would like so these her long make thing see him two has look more day could go come did number sound no most people my over know water than call first who may down side been now find any new work part take get place made live where after back little only round man year came show every good me give our under name very through just form sentence great think say help low line differ turn cause much mean before move right boy old too same tell does set three want air well also play small end put home read hand port large spell add even land here must big high such follow act why ask men change went light kind off need house picture try us again animal point mother world near build self earth father head stand own page should country found answer school grow study still learn plant cover food four between state keep eye never last let thought city tree cross farm hard start might story saw far sea draw left late run don't while press close night real life few north open seem together next white children begin got walk example ease paper group always music those both mark often letter until mile river car feet care second book carry took science eat room friend began idea fish mountain stop once base hear horse cut sure watch color face wood main enough plain girl usual young ready above ever red list though feel talk bird soon body dog family direct pose leave song measure door product black short numeral class wind question happen complete ship area half rock order fire south problem piece told knew pass since top whole king space heard best hour better true during hundred five remember step early hold west ground interest reach fast verb sing listen six table travel less morning ten simple several vowel toward war lay against pattern slow center love person money serve appear road map rain rule govern pull cold notice voice unit power town fine certain fly fall lead cry dark machine note wait plan figure star box noun field rest correct able pound done beauty drive stood contain front teach week final gave green oh quick develop ocean warm free minute strong special mind behind clear tail produce fact street inch multiply nothing course stay wheel full force blue object decide surface deep moon island foot system busy test record boat common gold possible plane stead dry wonder laugh thousand ago ran check game shape equate hot miss brought heat snow tire bring yes distant fill east paint language among grand ball yet wave drop heart am present heavy dance engine position arm wide sail material size vary settle speak weight general ice matter circle pair include divide syllable felt perhaps pick sudden count square reason length represent art subject region energy hunt probable bed brother egg ride cell believe fraction forest sit race window store summer train sleep prove lone leg exercise wall catch mount wish sky board joy winter sat written wild instrument kept glass grass cow job edge sign visit past soft fun bright gas weather month million bear finish happy hope flower clothe strange gone jump baby eight village meet root buy raise solve metal whether push seven paragraph third shall held hair describe cook floor either result burn hill safe cat century consider type law bit coast copy phrase silent tall sand soil roll temperature finger industry value fight lie beat excite natural view sense ear else quite broke case middle kill son lake moment scale loud spring observe child straight consonant nation dictionary milk speed method organ pay age section dress cloud surprise quiet stone tiny climb cool design poor lot experiment bottom key iron single stick flat twenty skin smile crease hole trade melody trip office receive row mouth exact symbol die least trouble shout except wrote seed tone join suggest clean break lady yard rise bad blow oil blood touch grew cent mix team wire cost lost brown wear garden equal sent choose fell fit flow fair bank collect save control decimal gentle woman captain practice separate difficult doctor please protect noon whose locate ring character insect caught period indicate radio spoke atom human history effect electric expect crop modern element hit student corner party supply bone rail imagine provide agree thus capital won't danger fruit rich thick soldier process operate guess necessary sharp wing create neighbor wash bat rather crowd corn compare poem string bell depend meat rub tube famous dollar stream fear sight thin triangle planet hurry chief colony clock mine tie enter major fresh search send yellow gun allow print dead spot desert suit current lift rose continue block chart hat sell success company subtract event particular deal swim term opposite wife shoe shoulder spread arrange camp invent cotton born determine quart nine truck noise level chance gather shop stretch throw shine property column molecule select wrong gray repeat require broad prepare salt nose plural anger claim continent oxygen sugar death pretty skill women season solution magnet silver thank branch match suffix especially fig afraid huge sister steel discuss forward similar guide experience score apple bought led pitch coat mass card band rope slip win dream evening condition feed tool total basic smell valley nor double seat arrive master track parent shore division sheet substance favor connect post spend chord fat glad original share station dad bread charge proper bar offer segment slave duck instant market degree populate chick dear enemy reply drink occur support speech nature range steam motion path liquid log meant quotient teeth shell neck")

#Sentence Parts of Speech:
#DT = Article
#IN = Preposition
#JJ = Adjective
#NN = Noun
#VB = verb
#RB = Adverb

#Creates a list for each of the different parts of speech. Theses are then used to create the sentences in the functions below.
adjList = list()
for word, tag in wordList.tags:
    if tag == 'JJ':
        adjList.append(word)

verbList = list()
for word, tag in wordList.tags:
    if tag == 'VB':
        verbList.append(word.pluralize())

advList = list()
for word, tag in wordList.tags:
    if tag == 'RB':
        advList.append(word)

dArticleList = list()
for word, tag in defArticleList.tags:
    if tag == 'DT':
        dArticleList.append(word)

articleList = list()
for word, tag in wordList.tags:
    if tag == 'DT':
        articleList.append(word)

prepositionList = list()
for word, tag in wordList.tags:
    if tag == 'IN':
        prepositionList.append(word)

nounList = list()
for word, tag in wordList.tags:
    if tag == 'NN':
        nounList.append(word)


#Creates a three word sentence using the strucure: Article Noun Verb.
def three_word_sentence():
    print(random.choice(dArticleList) + " " + random.choice(nounList) + " " + random.choice(verbList) + ".")

#Creates a four word sentence using the strucure: Article Adjective Noun Verb.
def four_word_sentence():
    print(random.choice(dArticleList) + " " + random.choice(adjList) + " " + random.choice(nounList) + " " + random.choice(verbList) + ".")

#Creates a five word sentence using the strucure: Article Adjective Noun Verb adverb.
def five_word_sentence():
    print(random.choice(dArticleList) + " " + random.choice(adjList) + " " + random.choice(nounList) + " " + random.choice(verbList) + " " + random.choice(advList) + ".")

#Creates a six word sentence using the strucure: Article Noun Verb Preposition Article Noun.
def six_word_sentence():
    print(random.choice(dArticleList) + " " + random.choice(nounList) + " " + random.choice(verbList) + " " + random.choice(prepositionList) + " " + random.choice(articleList) + " " + random.choice(nounList) + ".")


#Menu (1-5) with user input and error handling.
again = True
while (again):
    print("Main Menu")
    print("1 = Create a 3 word sentence (Article Noun Verb)")
    print("2 = Create a 4 word sentence (Article Adjective Noun Verb)")
    print("3 = Create a 5 word sentence (Article Adjective Noun Verb Adverb)")
    print("4 = Create a 6 word sentence (Article Noun Verb Preposition Article Noun)")
    print("5 = Exit")
    try:
        userInput = int(input("Please select a menu option (1-5) "))
        if userInput == 1:
            three_word_sentence()
        elif userInput == 2:
            four_word_sentence()
        elif userInput == 3:
            five_word_sentence()
        elif userInput == 4:
            six_word_sentence()
        elif userInput == 5:
            again = False
        elif userInput > 5 or userInput <= 0:
            print("Number invalid. Please enter a number between 1-5")
    except ValueError:
        print("This is not a number. Please enter a number between 1-5.")