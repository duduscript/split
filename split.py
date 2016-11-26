import load

def isindir(word):
    return word in dic

def isalnum(char):
    return char.isdigit() or char.isupper() or char.islower()

def initSplit(sentence):
    isal_or_num = isalnum(sentence[0])
    for i in range(len(sentence)):
        if isalnum(sentence[i]) and isal_or_num == False:
            return [sentence[:i]] + initSplit(sentence[i:])
        elif (not isalnum(sentence[i])) and isal_or_num == True:
            return [sentence[:i]] + initSplit(sentence[i:])
    return [sentence]

def split(sentence):
    def splitChinses(words,sentence,sentences):
        if len(sentence) == 0:
            sentences.append(words)
            return
        if isalnum(sentence[0]):
            sentences.append([sentence])
            return
        result,hasfind = [],False
        dic = load.Dictionary()
        for i in range(1,len(sentence)):
            if sentence[:i+1] in dic.getDic():
                hasfind = True
                splitChinses(words+[sentence[:i+1]],sentence[i+1:],sentences)
        if not hasfind:
            splitChinses(words+[sentence[0]],sentence[1:],sentences)
    result = []
    splitChinses([],sentence,result)
    return result

def sentence_combination(sentence):
    def comb(snt, path, paths):
        if len(snt) == 0:
            paths.append(path)
            return
        for i in range(len(snt[0])):
            comb(snt[1:], path+snt[0][i], paths)
    result = []
    comb(sentence, [], result)
    return result

def splitSentence(sentence):
    sentence = initSplit(sentence)
    return sentence_combination(list(map(split,sentence)))


def printSplit(sentence):
    print(sentence+':')
    results = splitSentence(sentence)
    for result in results:
        print('        '+'/'.join(result))

def test():
    printSplit('我爱北京天安门')
    printSplit('我们是共产主义的接班人')
    printSplit('这种乒乓球拍卖的很好')
    printSplit('我来自武汉理工大学计算机学院１２０２班')
    printSplit('我在北京邮电大学网络空间安全学院')
    printSplit('你们啊还是太年轻naive')
    printSplit('教育要面向现代化面向科技面向未来')
    printSplit('中央决定了就让你来当主席')

if __name__ == '__main__':
    test()
