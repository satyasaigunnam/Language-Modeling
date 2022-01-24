"""
Language Modeling Project
Name:
Roll No:
"""

from enum import unique
from itertools import count
from pickle import APPEND, EMPTY_LIST
from re import I
from sqlite3 import Row
from tkinter.tix import COLUMN
from types import new_class
from unittest import result
import language_tests as test

project = "Language" # don't edit this

### WEEK 1 ###

'''
loadBook(filename)
#1 [Check6-1]
Parameters: str
Returns: 2D list of strs
'''
def loadBook(filename):
    emlist=[]
    ins= open(filename,"r").read()
    list=ins.split('\n')
    for i in list:
        r = i.split(" ")
        if r!=['']:           
            emlist.append(r)
    
        
    
    return emlist


'''
getCorpusLength(corpus)
#2 [Check6-1]
Parameters: 2D list of strs
Returns: int
'''
def getCorpusLength(corpus):
    total_length =sum(len(Row) for Row in corpus)
    return total_length 


'''
buildVocabulary(corpus)
#3 [Check6-1]
Parameters: 2D list of strs
Returns: list of strs
'''
def buildVocabulary(corpus):
    result= list(set(i for j in corpus for i in j))
    return result


'''
countUnigrams(corpus)
#4 [Check6-1]
Parameters: 2D list of strs
Returns: dict mapping strs to ints
'''
def countUnigrams(corpus):
    nuber_c={}
    new_v=list(i for j in corpus for i in j)
    print
    
    for i in new_v:
        if i not in nuber_c:
            nuber_c[i]= new_v.count(i)
    print(nuber_c)        
    return nuber_c


'''
getStartWords(corpus)
#5 [Check6-1]
Parameters: 2D list of strs
Returns: list of strs
'''
def getStartWords(corpus):
    new_list=[] 
    for i in corpus: 
        new_list.append(i[0]) 
    return list(set(new_list))

'''
countStartWords(corpus)
#5 [Check6-1]
Parameters: 2D list of strs
Returns: dict mapping strs to ints
'''
def countStartWords(corpus):
    new_count ={}
    emp_list=[]
    
    for i in corpus:
        emp_list.append(i[0])
        
        for j in emp_list:
            new_count[j]= emp_list.count(j)
        
    return new_count

'''
countBigrams(corpus)
#6 [Check6-1]
Parameters: 2D list of strs
Returns: dict mapping strs to (dicts mapping strs to ints)
'''
def countBigrams(corpus):
    new_dist={}
    for p in range (len(corpus)):
        for j in range (len(corpus[p])-1):
            ver = corpus[p][j]
            ver2 = corpus[p][j+1]
            if ver not in new_dist:
                new_dist[ver]={}
            if ver2 not in new_dist[ver]:
                new_dist[ver][ver2]=0
            new_dist[ver][ver2]+=1
            
            
    return new_dist


### WEEK 2 ###

'''
buildUniformProbs(unigrams)
#1 [Check6-2]
Parameters: list of strs
Returns: list of floats
'''
def buildUniformProbs(unigrams):
    new_list =[]
    r_len = len(unigrams)
    for i in unigrams:
        new_list.append(1/r_len)
        print(new_list)
    return new_list


'''
buildUnigramProbs(unigrams, unigramCounts, totalCount)
#2 [Check6-2]
Parameters: list of strs ; dict mapping strs to ints ; int
Returns: list of floats
'''
def buildUnigramProbs(unigrams, unigramCounts, totalCount):
    new_list = []
    for i in unigrams:
        for j in  unigramCounts:
            if i==j:
                new_list.append(unigramCounts[j]/totalCount)
                
    return new_list


'''
buildBigramProbs(unigramCounts, bigramCounts)
#3 [Check6-2]
Parameters: dict mapping strs to ints ; dict mapping strs to (dicts mapping strs to ints)
Returns: dict mapping strs to (dicts mapping strs to (lists of values))
'''
def buildBigramProbs(unigramCounts, bigramCounts):
    new_dict={}
    
    for i in bigramCounts:
        words =[]
        probs =[]
        for j in bigramCounts[i]:
            words.append(j)
            probs.append(bigramCounts[i][j]/unigramCounts[i])
            new_dict[i]={"words":words, "probs": probs}

    return new_dict


'''
getTopWords(count, words, probs, ignoreList)
#4 [Check6-2]
Parameters: int ; list of strs ; list of floats ; list of strs
Returns: dict mapping strs to floats
'''
def getTopWords(count, words, probs, ignoreList):
   
    new_dict= dict(zip(words,probs )) 
    sorted_dict=dict(sorted(new_dict.items(),key=lambda x:x[1],reverse=True))
    
    dicts={}
    for key,values in sorted_dict.items():
        if key not in ignoreList and len(dicts)<count:
            dicts[key]=values
    return dicts


'''
generateTextFromUnigrams(count, words, probs)
#5 [Check6-2]
Parameters: int ; list of strs ; list of floats
Returns: str
'''
from random import choices, random
def generateTextFromUnigrams(count, words, probs):
    new_list=[]
    str1=""
    
    i =0
    while i < count:
        randomtext= choices(words,probs)
        new_list += randomtext
        i+=1
    for ele in new_list:
        str1= str1 +" "+ ele
    return str1


'''
generateTextFromBigrams(count, startWords, startWordProbs, bigramProbs)
#6 [Check6-2]
Parameters: int ; list of strs ; list of floats ; dict mapping strs to (dicts mapping strs to (lists of values))
Returns: str
'''
def generateTextFromBigrams(count, startWords, startWordProbs, bigramProbs):
    new_string=""
    list1=[]    #["dear", "sir"]
    for i in range (count):
        if len(list1)==0 or list1[-1]==".":
            ramdomtxt=choices(startWords,startWordProbs) #["dear"]
            list1=list1+ramdomtxt
        else:
            lwords=list1[-1]
            word=bigramProbs[lwords]["words"]  #[ "sir", "madam" ]
            prob=bigramProbs[lwords]["probs"]   #[0.5, 0.5] 
            list1=list1+choices(word,prob)
    for i in list1:
        new_string=new_string+" "+i
    return new_string


### WEEK 3 ###

ignore = [ ",", ".", "?", "'", '"', "-", "!", ":", ";", "by", "around", "over",
           "a", "on", "be", "in", "the", "is", "on", "and", "to", "of", "it",
           "as", "an", "but", "at", "if", "so", "was", "were", "for", "this",
           "that", "onto", "from", "not", "into" ]

'''
graphTop50Words(corpus)
#3 [Hw6]
Parameters: 2D list of strs
Returns: None
'''
def graphTop50Words(corpus):
    
    count_on=countUnigrams(corpus)
    words_no=buildVocabulary(corpus)
    probs=buildUnigramProbs(words_no,count_on,len(corpus))
    top_words=getTopWords(50, words_no, probs, ignore)
    barPlot(top_words, "top 50 words")
    return


'''
graphTopStartWords(corpus)
#4 [Hw6]
Parameters: 2D list of strs
Returns: None
'''
def graphTopStartWords(corpus):
    count=countStartWords(corpus)
    words=getStartWords(corpus)
    probs=buildUnigramProbs(words,count,len(corpus))
    top_words=getTopWords(50, words, probs, ignore)
    barPlot(top_words, "top start words")
    return


'''
graphTopNextWords(corpus, word)
#5 [Hw6]
Parameters: 2D list of strs ; str
Returns: None
'''
def graphTopNextWords(corpus, word):
    count_no=countUnigrams(corpus)
    count_o=countBigrams(corpus)
    probs=buildBigramProbs(count_no,count_o)
    top_words=getTopWords(10, probs[word]["words"], probs[word]["probs"], ignore)
    barPlot(top_words, "top next words")

    return


'''
setupChartData(corpus1, corpus2, topWordCount)
#6 [Hw6]
Parameters: 2D list of strs ; 2D list of strs ; int
Returns: dict mapping strs to (lists of values)
'''
def setupChartData(corpus1, corpus2, topWordCount):
    top_words=[]
    corpus1_probs=[]
    corpus2_probs=[]
    dict1={}

    count1=countUnigrams(corpus1)
    words1=buildVocabulary(corpus1)
    probs1=buildUnigramProbs(words1,count1,getCorpusLength(corpus1))
    top1 =getTopWords(topWordCount, words1, probs1, ignore)
    

    count2=countUnigrams(corpus2)
    words2=buildVocabulary(corpus2)
    probs2=buildUnigramProbs(words2,count2,getCorpusLength(corpus2))
    top2=getTopWords(topWordCount, words2, probs2, ignore)
    
    top_words=top_words+list(top1.keys())
    for i in top2.keys():
        if i not in top_words:
            top_words.append(i)
    for j in top_words:
        if j in words1:
            r=words1.index(j)
            corpus1_probs.append(probs1[r])
        else:
            corpus1_probs.append(0)
        if j in words2:
            z=words2.index(j)
            corpus2_probs.append(probs2[z])
        else:
            corpus2_probs.append(0)
    dict1["topWords"]=top_words
    dict1["corpus1Probs"]=corpus1_probs
    dict1["corpus2Probs"]=corpus2_probs


    return dict1


'''
graphTopWordsSideBySide(corpus1, name1, corpus2, name2, numWords, title)
#6 [Hw6]
Parameters: 2D list of strs ; str ; 2D list of strs ; str ; int ; str
Returns: None
'''
def graphTopWordsSideBySide(corpus1, name1, corpus2, name2, numWords, title):
    new=setupChartData(corpus1,corpus2,numWords)
    # xValues=new["topWords"]
    # values1=new["corpus1Probs"]
    # values2=new["corpus2Probs"]
    sideBySideBarPlots(new["topWords"], new["corpus1Probs"], new["corpus2Probs"], name1, name2, title)
    return


'''
graphTopWordsInScatterplot(corpus1, corpus2, numWords, title)
#6 [Hw6]
Parameters: 2D list of strs ; 2D list of strs ; int ; str
Returns: None
'''
def graphTopWordsInScatterplot(corpus1, corpus2, numWords, title):
    new=setupChartData(corpus1,corpus2,numWords)
    # labels=new["topWords"]
    # xs=new["corpus1Probs"]
    # ys=new["corpus2Probs"]
    scatterPlot(new["corpus1Probs"],new["corpus2Probs"], new["topWords"], title)
    return


### WEEK 3 PROVIDED CODE ###

"""
Expects a dictionary of words as keys with probabilities as values, and a title
Plots the words on the x axis, probabilities as the y axis and puts a title on top.
"""
def barPlot(dict, title):
    import matplotlib.pyplot as plt

    names = []
    values = []
    for k in dict:
        names.append(k)
        values.append(dict[k])

    plt.bar(names, values)

    plt.xticks(rotation='vertical')
    plt.title(title)

    plt.show()

"""
Expects 3 lists - one of x values, and two of values such that the index of a name
corresponds to a value at the same index in both lists. Category1 and Category2
are the labels for the different colors in the graph. For example, you may use
it to graph two categories of probabilities side by side to look at the differences.
"""
def sideBySideBarPlots(xValues, values1, values2, category1, category2, title):
    import matplotlib.pyplot as plt

    w = 0.35  # the width of the bars

    plt.bar(xValues, values1, width=-w, align='edge', label=category1)
    plt.bar(xValues, values2, width= w, align='edge', label=category2)

    plt.xticks(rotation="vertical")
    plt.legend()
    plt.title(title)

    plt.show()

"""
Expects two lists of probabilities and a list of labels (words) all the same length
and plots the probabilities of x and y, labels each point, and puts a title on top.
Note that this limits the graph to go from 0x0 to 0.02 x 0.02.
"""
def scatterPlot(xs, ys, labels, title):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()

    plt.scatter(xs, ys)

    # make labels for the points
    for i in range(len(labels)):
        plt.annotate(labels[i], # this is the text
                    (xs[i], ys[i]), # this is the point to label
                    textcoords="offset points", # how to position the text
                    xytext=(0, 10), # distance from text to points (x,y)
                    ha='center') # horizontal alignment can be left, right or center

    plt.title(title)
    plt.xlim(0, 0.02)
    plt.ylim(0, 0.02)

    # a bit of advanced code to draw a y=x line
    ax.plot([0, 1], [0, 1], color='black', transform=ax.transAxes)

    plt.show()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":
    # print("\n" + "#"*15 + " WEEK 1 TESTS " +  "#" * 16 + "\n")
    # test.week1Tests()
    # print("\n" + "#"*15 + " WEEK 1 OUTPUT " + "#" * 15 + "\n")
    # test.runWeek1()
    # test.testLoadBook()
    # test.testGetCorpusLength()
    # test.testBuildVocabulary()
    # test.testCountUnigrams()  
    # test.testGetStartWords() 
    # test.testCountStartWords()
    # test.testCountBigrams()
    #test.testBuildUniformProbs()
    # test.testBuildUnigramProbs()
    # test.testBuildBigramProbs()
    # test.testGetTopWords()
    # test.testGenerateTextFromUnigrams()
    # test.testGenerateTextFromBigrams()
    
    # test.runWeek3()
    
    

    ## Uncomment these for Week 2 ##

    # print("\n" + "#"*15 + " WEEK 2 TESTS " +  "#" * 16 + "\n")
    # test.week2Tests()
    # print("\n" + "#"*15 + " WEEK 2 OUTPUT " + "#" * 15 + "\n")
    # test.runWeek2()


    ## Uncomment these for Week 3 ##
    print("\n" + "#"*15 + " WEEK 3 OUTPUT " + "#" * 15 + "\n")
    test.runWeek3()
    test.testSetupChartData()
