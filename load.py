import model
import dictionary


def singleton(cls, *args, **kw):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton

'''
@singleton
class Dictionary(object):
    def __init__(self, x=0):
        self.dic = set()
        with open('GWDic.dic') as file:
            for word in file.readlines():
                self.dic.add(word[:-1])
    def getDic(self):
        return self.dic
'''

@singleton
class Dictionary(object):
    def __init__(self, x=0):
        self.dic = dictionary.dic
    def getDic(self):
        return self.dic

@singleton
class Model(object):
    """docstring for Model."""
    def __init__(self):
        #super(Model, self).__init__()
        self.model = model.model
    def getModel(self):
        return self.model
