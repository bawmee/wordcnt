from django.shortcuts import render
import operator


def home(requset):
    return render(requset, 'home.html')


def about(requset):
    return render(requset, 'about.html')

def result(requset):
    text = requset.GET['fulltext']
    wordlist = text.split()
    wordDic = dict()
    for w in wordlist:
        if w in wordDic:
            wordDic[w] += 1
        else:
            wordDic[w] = 1
    orderDic = sorted(wordDic.items(), key=operator.itemgetter(1), reverse=True)

    length = len(wordlist)
    return render(requset, 'result.html', { 'full':text, 'list':wordlist, 'len':length, 'cnt' : orderDic })