import load
import math

def get_word_prob(prev_word,word):
    model = load.Model()
    md,count = model.getModel(),0
    for back_word in md[prev_word]:
        count += md[prev_word][back_word]
    return math.log(md[prev_word][word]/count)

def smoothing(prev_word,word):
    md = load.Model().getModel()
    if prev_word in md:
        return math.log(1/(sum(map(lambda x:md[prev_word][x],md[prev_word]))+1))
    else:
        return math.log(1/len(md))

def get_sentence_prob(sentence):
    md = load.Model().getModel()
    prob_log = 0
    for i in range(len(sentence)):
        #先这样
        if i == 0 and sentence[0] not in md['^']:
            prob_log *= smoothing('^',sentence[i])
        elif i == 0:
            prob_log = get_word_prob('^',sentence[i])
        elif sentence[i-1] not in md or sentence[i] not in md[sentence[i-1]]:
            prob_log *= smoothing(sentence[i-1],sentence[i])
        else:
            prob_log *= get_word_prob(sentence[i-1],sentence[i])
    return prob_log

def bigram(split_sentences):
    max_prob,result = 0,''
    for sentence in split_sentences:
        if get_sentence_prob(sentence) > max_prob:
            result = sentence
    return sentence
