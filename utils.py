import lzma
import dill as pickle

def load_pickle(path):
    with lzma.open(path,"rb") as fp:
        file = pickle.load(fp)
    return file

def save_pickle(path):
    pass

def save_pickle(path,obj):
    with open(path,"wb") as fp:
        pickle.dump(obj,fp)