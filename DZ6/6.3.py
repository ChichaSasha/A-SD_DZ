class Node:
    def __init__(self,lat,eng):
        self.lat =  lat
        self.eng  = [eng]
        self.next=None
        self.valid = True


class HashTable:
    M= 503
    N=31
    def __init__(self):
        self.values = [None for i in range(HashTable.M)]
        self.lat = []
        self.leng=0

    def  hash_str(self,s):
        h = 0
        for i in range(len(s)):
            h = h * HashTable.N + ord(s[i])
        return h % HashTable.M

    def open(self):
        with open("input63.txt", "r") as file:
            for line in file:
                eng, lat_str = line.strip().split(' - ')
                lat_lst = lat_str.split(', ')
                for lat in lat_lst:
                    self.add_new(lat,eng)

    def add_new(self,lat,eng):
        hash_key = self.hash_str(lat)
        slot = self.values[hash_key]
        while slot != None:
            if slot.lat == lat:
                slot.eng.append(eng)
                slot.valid = True
                return
            slot = slot.next
        self.leng += 1
        slot = Node(lat, eng)
        self.lat.append(lat)
        slot.next = self.values[hash_key]
        self.values[hash_key] = slot

    def findByLat(self,lat):
        hash_key = self.hash_str(lat)
        slot = self.values[hash_key]
        tmp = []
        while slot != None:
            tmp.append(slot.eng)
            slot = slot.next
        return tmp

    def write_to_file(self):
        with open('output63.txt', 'w') as file1:
            file1.write(str(self.leng) + '\n')
            self.lat = sorted(self.lat)
            for word in self.lat:
                ans = word + " - "
                tmp  = self.findByLat(word)
                counter = 0
                for eng in tmp:
                    eng.sort()
                    for el in eng:
                        if counter == 0:
                            counter+=1
                            ans+= el
                        else:
                            ans+= ", " + el
                file1.write(ans+'\n')

A = HashTable()
A.open()
A.write_to_file()
