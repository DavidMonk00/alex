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
