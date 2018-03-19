import re
from glob import glob
from data import Data
import collections

class WordAnalysis:
    def __init__(self, data):
        self.data = data
    def splitEntries(self):
        self.entries = [i.strip().split(" ") for i in self.data.entries]
    def getFullList(self):
        self.words = []
        for i in self.entries:
            self.words += i
        for i in range(len(self.words)):
            self.words[i] = self.words[i].lower()
        self.occurences  = collections.Counter(self.words)
        print self.occurences

class Analysis:
    def getData(self,filename):
        self.data = Data(filename)
    def getApprovedReferences(self,filename):
        self.approved_references = Data(filename)
    def removeKeywordEntries(self, kw_file):
        kws = [i.strip().split(',') for i in open(kw_file)]
        for kw in kws:
            self.data.removeKeywordEntries(kw)
    def createWordAnalysis(self):
        self.wordanalysis = WordAnalysis(self.approved_references)
        self.wordanalysis.splitEntries()
        self.wordanalysis.getFullList()

def main():
    A = Analysis()
    A.getData("data.txt")
    A.getApprovedReferences("included.txt")
    A.removeKeywordEntries("kws.config")
    A.createWordAnalysis()
    # files = glob("*.txt")
    # data = Data("data.txt")
    # print len(data.entries)
    # print len(data.entries)
    # data.rebuildFile()
    # print len([line.strip() for line in open("data.txt")])
    # print len([line.strip() for line in open("data_shortened.txt")])

if (__name__ == "__main__"):
    main()
