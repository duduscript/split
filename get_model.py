import jieba
import re
import os
import load

class Model(object):
    def __init__(self,dir):
        self.model = {'^':{}}
        self.training_dir = dir
        self.dict = load.Dictionary().getDic()
    def get_model(self):
        return self.model
    def train(self):
        def train_sentence(sentence):
            sentence_words = list(filter(lambda word:word in self.dict,jieba.cut(sentence,cut_all=False)))
            for i in range(len(sentence_words)):
                prev = '^' if i == 0 else sentence_words[i-1]
                #print(sentence_words[i])
                if sentence_words[i] not in self.model:
                    self.model[sentence_words[i]] = {}
                if sentence_words[i] in self.model[prev]:
                    self.model[prev][sentence_words[i]] += 1
                else:
                    self.model[prev][sentence_words[i]] = 1
        def train_paragraph(paragraph):
            #sentences = paragraph.split()
            sentences = filter(lambda x:len(x),re.split(',|\.|;|，|。|；|：|、|\?|？|　',paragraph))
            #print(sentences)
            for sentence in sentences:
                train_sentence(sentence)
        def print_model():
            print('model=',end='')
            print(self.model,end='')
        files = self.get_training_files()
        count = 1
        for file in files:
            train_paragraph(file.read())
            #print(count)
            count += 1
        #print_model()
    def get_training_files(self):
        for path in os.listdir(self.training_dir):
            with open('/'.join([os.getcwd(),self.training_dir,path])) as file:
                yield file


if __name__ == '__main__':
    pass
    #model = Model('training')
    #model.train()
