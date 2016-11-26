import jieba
import os

class Model(object):
    def __init__(self,dir):
        self.model = {'^':{}}
        self.words = load.Dictionary().getDic()
        self.training_dir = dir
    def get_model(self):
        return self.model
    def train(self):
        def train_sentence(sentence):
            self.words = jieba.cut(sentence,cut_all=False)
            for i in range(len(words)):
                prev = '^' if i == 0 else words[i-1]
                if words[i] not in model[words[i-1]]:
                    self.model[prev][words[i]] = 1
                else:
                    self.model[prev][words[i]] += 1
        def train_paragraph(paragraph):
            sentences = paragraph.split()
            for sentence in sentences:
                train_sentence(sentence)
        def print_model():
            print(self.model)
        files = self.get_training_files()
        for file in files:
            train_paragraph(file.read())
        print(self.model)
    def get_training_files(self):
        for path in os.listdir(self.training_dir):
            with open(path) as file:
                yield file


if __name__ == '__main__':
    model = Model('training')
    model.train()
