import operator
def count(article):

    words = article.split()
    wordcount = len(words)
    dictword = {}
    for word in words:
        if word in dictword:
            dictword[word] += 1
        else:
            dictword[word] = 1

    vardict = sorted(dictword.items(), key=operator.itemgetter(1), reverse=True)
    return vardict, wordcount
