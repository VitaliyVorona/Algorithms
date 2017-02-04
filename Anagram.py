class Anagram:
    def anagramSolution(self, string1, string2):
        alist = list(string1)

        position1 = 0
        stillOk = True

        while position1 < len(string1) & stillOk:
            position2 = 0
            found = False
            while position2 < len(alist) and not found:
                if string2[position1] == alist[position2]:
                    found = True
                else:
                    position2 += 1

            if found:
                alist[position2] = None
            else:
                stillOk = False

            position1 += 1

        return stillOk

    def anagramSolution2(self, string1, string2):
        c1 = [0] * 26
        c2 = [0] * 26

        s1 = 'apple'
        s2 = 'pleap'

        for i in range(len(s1)):
            pos = ord(s1[i]) - ord('a')
            c1[pos] += 1

        for i in range(len(s2)):
            pos = ord(s2[i]) - ord('a')
            c2[pos] += 1

        j = 0
        stillOK = True
        while j < 26 & stillOK:
            if c1[j] == c2[j]:
                j += 1
            else:
                stillOK = False

        return stillOK

a = Anagram()
v = a.anagramSolution('apple', 'pplea')
x = a.anagramSolution2('apple', 'pplea')

print(v)
print(x)
