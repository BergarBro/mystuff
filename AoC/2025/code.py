

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
    list = []
    with open("AoC\\2025\\input3_test.txt", "r") as file :
        for line in file :
            list.append(str(int(line)))
    sol = []
    for number in list :
        
        indexs = []
        for j in range(11) :
            biggest = 0
            index = 0
            for i, c in enumerate(number[:-1]) :
                n =  int(c)
                if biggest < n and not contains(indexs, i) :
                    index = i
                    biggest = n
            indexs.append(index)
        print(indexs)
        # for c in number[index+1:] :
        #     n =  int(c)
        #     if secondNum < n :
        #         secondNum = n
        # sol.append(firstNum*10 + secondNum)
    # print(sum(sol))


def contains(list, value) :
    for n in list :
        if n == value :
            return True
    return False

main31()
