import re
class Node:
    def __init__(self,word):
        self.word =  word
        self.amount  = 0
        self.next=None
        self.valid = True

class HashTable:
    M= 100007
    N=31
    def __init__(self):
        self.values = [None for i in range(HashTable.M)]

    def  hash_str(self,s):
        h = 0
        for i in range(len(s)):
            h = h * HashTable.N + ord(s[i])
        return h % HashTable.M

    def open_file(self):
        file = open('input64.txt', 'r', encoding="UTF-8")
        for l in file:
            line = re.sub('[^A-Za-z]', ' ', l)
            line_ar = line.lower().split()
            for word in line_ar:
                self.add_word(word)
        file.close()

    def add_word(self,word):
        hash_key = self.hash_str(word)
        slot = self.values[hash_key]
        while slot != None:
            if slot.word == word:
                slot.amount +=1
                slot.valid = True
                return
            slot = slot.next
        slot = Node(word)
        slot.next = self.values[hash_key]
        self.values[hash_key] = slot

    def write_to_file(self):
        file1 = open('output64.txt', 'w')
        ar = []
        for i in range(HashTable.M):
            if self.values[i]==None:
                continue
            else:
                ar.append(self.values[i].word)
        ar = sorted(ar)
        for i in ar:
            file1.write(i + "\n")
        file1.close()

A = HashTable()
A.open_file()
A.write_to_file()
