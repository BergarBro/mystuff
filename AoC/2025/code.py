import random as rn
from tqdm import tqdm
import math

def main30() :
    list = []
    with open("AoC\\2025\\input3.txt", "r") as file :
        for line in file :
            list.append(str(int(line)))
    sol = []
    for number in list :
        firstNum = 0
        secondNum = 0
        index = 0
        for i, c in enumerate(number[:-1]) :
            n =  int(c)
            # print(n)
            if firstNum < n :
                # print(firstNum, n)
                index = i
                firstNum = n
            # print(c, i)

        for c in number[index+1:] :
            n =  int(c)
            if secondNum < n :
                secondNum = n
        sol.append(firstNum*10 + secondNum)
    print(sum(sol))



def main31() :
    solSize = 12
    print_ = False
    brute = False
    list = []
    with open("AoC\\2025\\input3.txt", "r") as file :
        for line in file :
            list.append(str(int(line)))
    sol = []
    for number in list :
        l = len(number)
        indexes = {}
        lastIndexes = []
        startIndex = 0
        endIndex = l
        for j in range(solSize) :
            newInt = False
            i = startIndex
            biggest = -1
            biggestIndex = -1
            while not newInt :
                n = int(number[i])
                if biggest < n and (indexes.get(i, -1) == -1) :
                    biggest = n
                    biggestIndex = i
                i += 1
                if i >= endIndex :
                    if biggest != -1 :
                        indexes[biggestIndex] = biggest
                        lastIndexes.append(biggestIndex)
                        newInt = True
                        startIndex = biggestIndex
                    else :
                        endIndex = startIndex
                        if len(lastIndexes) != 0 :
                            lastIndex = lastIndexes[-1]
                            if sum([1 for key in indexes if key > lastIndex]) == (l - lastIndex - 1) :
                                i = lastIndexes.pop()
                            else :
                                i = lastIndex
                        else :
                            i = 0
        num = ""
        for k in range(l) :
            num += str(indexes.get(k, ""))
        num = int(num)
        sol.append(num)
    if brute :
        altSol = []
        for n in tqdm(list) :
            allComb = []
            for i1 in range(l-11) :
                for i2 in range(i1+1,l-10) :
                    for i3 in range(i2+1,l-9) :
                        for i4 in range(i3+1,l-8) :
                            for i5 in range(i4+1,l-7) :
                                for i6 in range(i5+1,l-6) :
                                    for i7 in range(i6+1,l-5) :
                                        for i8 in range(i7+1,l-4) :
                                            for i9 in range(i8+1,l-3) :
                                                for i10 in range(i9+1,l-2) :
                                                    for i11 in range(i10+1,l-1) :
                                                        for i12 in range(i11+1,l) :
                                                            allComb.append(n[i1] + n[i2] + n[i3] + n[i4] + n[i5] + n[i6] + n[i7] + n[i8] + n[i9] + n[i10] + n[i11] + n[i12])
            allComb.sort()
            altSol.append(int(allComb[-1]))
        # print(altSol)
    if print_ :
        for i in range(len(sol)) :
            print(i, ":", list[i], "\nMySol", sol[i])
            if brute :
                print("Brute", altSol[i])
                if sol[i] == altSol[i] :
                    print("Pass")
                else :
                    print("-----------------------------> Fail")
        print(len(sol), len(list))
    print(sum(sol))

def makeInput() :
    with open("AoC\\2025\\data.txt", "w") as file:
        for i in range(20) :
            n = 0
            while "0" in str(n) :
                n = rn.randint(10000000000000000,99999999999999999)
            file.write(str(n) + "\n")



def main40() :
    size = 1
    list = []
    with open("AoC\\2025\\input4.txt", "r") as file :
        ln = 0
        for line in file :
            list.append("".join([c for c in line if c != "\n"]))
    print(list)
    m = len(list)
    n = len(list[0])
    counter = {}
    acc = 0
    for i in range(m) :
        for j in range(n) :
            if list[i][j] == "@" :
                for k in range(-size, size + 1) :
                    for l in range(-size, size + 1) :
                        if k != 0 or l != 0 :
                            counter.setdefault(((i + k),(j + l)), 0)
                            counter[((i + k),(j + l))] += 1
    for i in range(m) :
        for j in range(n) :
            if counter.get((i,j), 0) < 4 and list[i][j] == "@" :
                acc += 1
    print(acc)



def main41() :
    size = 1
    list = []
    with open("AoC\\2025\\input4.txt", "r") as file :
        ln = 0
        for line in file :
            list.append("".join([c for c in line if c != "\n"]))
    print(list)
    m = len(list)
    n = len(list[0])
    acc = 0
    change = -1
    while change != 0 :
        counter = {}
        change = 0
        for i in range(m) :
            for j in range(n) :
                if list[i][j] == "@" :
                    for k in range(-size, size + 1) :
                        for l in range(-size, size + 1) :
                            if k != 0 or l != 0 :
                                counter.setdefault(((i + k),(j + l)), 0)
                                counter[((i + k),(j + l))] += 1
        for i in range(m) :
            for j in range(n) :
                if counter.get((i,j), 0) < 4 and list[i][j] == "@" :
                    change += 1
                    string = list[i] 
                    list[i] = string[:j] + "." + string[j+1:]
        # print(list)
        acc += change
    print(acc)



def main50() :
    list1 = []
    list2 = []
    with open("AoC\\2025\\input5.txt", "r") as file :
        for line in file :
            line = "".join([c for c in line if c != "\n"])
            if "-" in line :
                index = line.find("-")
                list1.append((int(line[:index]),int(line[index+1:])))
            else :
                if len(line) != 0 :
                    list2.append(int(line))
    acc = 0
    for n in list2 :
        for f, s in list1 :
            if n >= f and n <= s :
                acc += 1
                break
    print(acc)


# Does not work!
def main51() :
    brute = False
    list1 = []
    list2 = []
    with open("AoC\\2025\\input5.txt", "r") as file :
        for line in file :
            line = "".join([c for c in line if c != "\n"])
            if "-" in line :
                index = line.find("-")
                list1.append((int(line[:index]),int(line[index+1:])))
            else :
                if len(line) != 0 :
                    list2.append(int(line))
    list1.sort()
    if brute :
        acc = set()
        for i, j in tqdm(list1) :
            interval = set([n for n in range(i, j+1)])
            acc = acc | interval
    else :
        acc = []
        newFirst = 0
        newSecond = 0
        firstIndex = -1
        secondIndex = -1
        for testFirst, testSecond in list1 :
            newFirst = testFirst
            newSecond = testSecond
            for index, (first, second) in enumerate(acc) :
                if testFirst >= first and testFirst <= second :
                    newFirst = first
                    firstIndex = index
                if testSecond >= first and testSecond <= second :
                    newSecond = second
                    secondIndex = index

            if secondIndex != -1 :
                if firstIndex == secondIndex :
                    del acc[firstIndex]
                else :
                    if firstIndex != -1 :
                        print("delete", secondIndex, "and", firstIndex)
                        del acc[secondIndex]
                        del acc[firstIndex]
                    else :
                        del acc[secondIndex]
            else :
                if firstIndex != -1 :
                    del acc[firstIndex]
            acc.append((newFirst, newSecond))
            acc.sort()
            firstIndex = -1
            secondIndex = -1
    sol = 0
    for f, s in acc :
        sol += s+1 - f
    print(sol)



def main60() :
    list = []
    oper = []
    with open("AoC\\2025\\input6.txt", "r") as file :
        for line in file :
            line = "".join([c for c in line if c != "\n"])
            if "+" in line :
                oper = [c for c in line if c != " "]
            else :
                numbers = []
                number = ""
                for c in line :
                    if c != " " :
                        number += c
                    else :
                        if number != "" :
                            numbers.append(int(number))
                            number = ""
                if number != "" :
                    numbers.append(int(number))
                list.append(numbers)
    trans_list = [[list[j][i] for j in range(len(list))] for i in range(len(list[0]))]
    sums = []
    for i, op in enumerate(oper) :
        if op == "+" :
            sums.append(sum(trans_list[i]))
        else :
            sums.append(math.prod(trans_list[i]))
    print(sum(sums))



def main61() :
    list = []
    oper = []
    with open("AoC\\2025\\input6.txt", "r") as file :
        for line in file :
            line = "".join([c for c in line if c != "\n"])
            if "+" in line :
                oper = [c for c in line if c != " "]
            else :
                list.append(line)
    trans_list = ["".join([list[j][i] for j in range(len(list))]) for i in range(len(list[0]))]
    removed_spaces = ["".join([c for c in number if c not in " "]) for number in trans_list]
    numbers = []
    sub_numbers = []
    for str in removed_spaces :
        if str != "" :
            sub_numbers.append(int(str))
        else :
            numbers.append(sub_numbers)
            sub_numbers = []
    numbers.append(sub_numbers)

    sums = []
    for i, op in enumerate(oper) :
        if op == "+" :
            sums.append(sum(numbers[i]))
        else :
            sums.append(math.prod(numbers[i]))
    print(sum(sums))

main51()
