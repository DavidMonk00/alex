import re

class Data:
    def __init__(self,filename):
        data = [line for line in open(filename)]
        self.entries = []
        entry = []
        for i in data:
            if (i.strip() == ''):
                self.entries.append(" ".join(entry))
                entry = []
            else:
                entry.append(i)
    def getKeywordEntries(self,kw):
        entries = list(self.entries)
        for word in kw:
            matches = []
            for i in entries:
                if word in i.lower():
                    matches.append(i)
            entries = matches
        return matches
    def removeKeywordEntries(self, kw):
        matches = self.getKeywordEntries(kw)
        for i in matches[::-1]:
            self.entries.remove(i)
    def rebuildFile(self):
        string = "\r\n".join(self.entries)
        f = open("data_shortened.txt", "w")
        f.write(string)


def main():
    data = Data("data.txt")
    print len(data.entries)
    kws = [i.strip().split(',') for i in open("kws.txt")]
    for kw in kws:
        data.removeKeywordEntries(kw)
    print len(data.entries)
    data.rebuildFile()
    print len([line.strip() for line in open("data.txt")])
    print len([line.strip() for line in open("data_shortened.txt")])



if (__name__ == "__main__"):
    main()
