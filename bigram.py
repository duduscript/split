import model

def smoothing(prev,now):
    return 1

def get_prob(sentence):
    md = model.model
    prob = 1
    for i in range(len(sentence)):
        #先这样
        if i == 0 and sentence[0] not in md['^']:
            prob *= smoothing('^',sentence[i])
        elif i == 0:
            prob *= md['^'][sentence[i]]
        elif sentence[i-1] not in md or sentence[i] not in md[sentence[i-1]]:
            prob *= smoothing(sentence[i-1],sentence[i])
        else:
            prob *= md[sentence[i-1]][sentence[i]]
    return prob

def bigram(split_sentences):
    max_prob,result = 0,''
    for sentence in split_sentences:
        if get_prob(sentence) > max_prob:
            result = sentence
    return sentence
