import random as rn
from tqdm import tqdm
import math
import bisect

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
    with open("AoC\\2025\\data3.txt", "w") as file:
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



def main70() :
    size = -1
    S_index = -1
    splitters = []
    with open("AoC\\2025\\input7.txt", "r") as file :
        for line in file :
            line = "".join([c for c in line if c != "\n"])
            size = len(line)
            S_index = int((size - 1) / 2)
            if "^" in line :
                dict = {}
                for i, c in enumerate(line) :
                    if c == "^" :
                        dict[i] = [i-1,i+1]
                splitters.append(dict)
    beams = {S_index: 1}
    used_splitters = set()
    for i, splitter in tqdm(enumerate(splitters)) :
        new_beams = {}
        for beam in beams :
            new_beam = splitter.get(beam,[beam])
            if new_beam != [beam] :
                used_splitters.add((i,beam))
            for b in new_beam :
                new_beams[b] = new_beams.get(b,0) + beams[beam]
        beams = new_beams
        print(beams)
    print(len(used_splitters))



def main71() :
    S_index = -1
    splitters = []
    with open("AoC\\2025\\input7.txt", "r") as file :
        for line in file :
            line = "".join([c for c in line if c != "\n"])
            S_index = int((len(line) - 1) / 2)
            if "^" in line :
                dict = {}
                for i, c in enumerate(line) :
                    if c == "^" :
                        dict[i] = [i-1,i+1]
                splitters.append(dict)
    beams = {S_index: 1}
    for i, splitter in enumerate(splitters) :
        new_beams = {}
        for beam in beams :
            new_beam = splitter.get(beam,[beam])
            for b in new_beam :
                new_beams[b] = new_beams.get(b,0) + beams[beam]
        beams = new_beams
    acc = 0
    for beam in beams :
        acc += beams[beam]
    print(acc)



def main80() :
    points = {}
    with open("AoC\\2025\\input8.txt", "r") as file :
        for i, line in enumerate(file) :
            line = "".join([c for c in line if c != "\n"])
            corrds = [int(corrd) for corrd in line.split(",")]
            points[i] = corrds
    dist_dict = {}
    dist_list = []
    for i in range(len(points)-1) :
        for j in range(i+1, len(points)) :
            distans = sum([(x1-x2)**2 for x1,x2 in list(zip(points[i], points[j]))])
            dist_dict[(i,j)] = distans
            dist_list.append(((i,j),distans))
    dist_list.sort(key= lambda x : x[1])
    
    conections = {}
    total_connections = 0
    for i in range(len(points)) :
        conections[i] = []
    for (i, j), d in dist_list :
        lowest_con_i = -1
        lowest_con_j = -1
        con_i = conections.get(i)
        con_j = conections.get(j)
        if len(con_i) == 0 :
            lowest_con_i = i
        else :
            con_i.sort()
            lowest_con_i = con_i[0]
            if i < lowest_con_i :
                lowest_con_i = i
            
        if len(con_j) == 0 :
            conections[j].append(lowest_con_i)
            conections[lowest_con_i].append(j)
        else :
            con_j.sort()
            lowest_con_j = con_j[0]
            if j < lowest_con_j :
                lowest_con_j = j
            index_to_dominate = -1
            index_to_merge = -1
            if lowest_con_i != lowest_con_j :
                if lowest_con_i < lowest_con_j :
                    index_to_dominate = lowest_con_i
                    index_to_merge = lowest_con_j
                else :
                    index_to_dominate = lowest_con_j
                    index_to_merge = lowest_con_i
                for index in conections[index_to_merge] :
                    conections[index_to_dominate].append(index)
                    conections[index] = [index_to_dominate]
                conections[index_to_dominate].append(index_to_merge)
                conections[index_to_merge] = [index_to_dominate]
        total_connections += 1
        if total_connections >= 1000 :
            break 
    size_circuits = []
    for i in conections :
        size_circuits.append(len(conections[i]) + 1)
    size_circuits.sort(reverse=True)
    # print(size_circuits)
    sol = 1
    for size in size_circuits[:3] :
        sol *= size
    print(sol)



def main81() :
    points = {}
    with open("AoC\\2025\\input8.txt", "r") as file :
        for i, line in enumerate(file) :
            line = "".join([c for c in line if c != "\n"])
            corrds = [int(corrd) for corrd in line.split(",")]
            points[i] = corrds
    dist_dict = {}
    dist_list = []
    for i in range(len(points)-1) :
        for j in range(i+1, len(points)) :
            distans = sum([(x1-x2)**2 for x1,x2 in list(zip(points[i], points[j]))])
            dist_dict[(i,j)] = distans
            dist_list.append(((i,j),distans))
    dist_list.sort(key= lambda x : x[1])
    
    conections = {}
    total_connections = 0
    last_connection = (-1,-1)
    for i in range(len(points)) :
        conections[i] = []
    for (i, j), d in dist_list :
        lowest_con_i = -1
        lowest_con_j = -1
        con_i = conections.get(i)
        con_j = conections.get(j)
        if len(con_i) == 0 :
            lowest_con_i = i
        else :
            con_i.sort()
            lowest_con_i = con_i[0]
            if i < lowest_con_i :
                lowest_con_i = i
            
        if len(con_j) == 0 :
            conections[j].append(lowest_con_i)
            conections[lowest_con_i].append(j)
        else :
            con_j.sort()
            lowest_con_j = con_j[0]
            if j < lowest_con_j :
                lowest_con_j = j
            index_to_dominate = -1
            index_to_merge = -1
            if lowest_con_i != lowest_con_j :
                if lowest_con_i < lowest_con_j :
                    index_to_dominate = lowest_con_i
                    index_to_merge = lowest_con_j
                else :
                    index_to_dominate = lowest_con_j
                    index_to_merge = lowest_con_i
                for index in conections[index_to_merge] :
                    conections[index_to_dominate].append(index)
                    conections[index] = [index_to_dominate]
                conections[index_to_dominate].append(index_to_merge)
                conections[index_to_merge] = [index_to_dominate]
        total_connections += 1
        if len(conections[0]) >= len(points) - 1 :
            last_connection = (i,j)
            break 
    # size_circuits = []
    # for i in conections :
    #     size_circuits.append(len(conections[i]) + 1)
    # size_circuits.sort(reverse=True)
    # # print(size_circuits)
    # sol = 1
    # for size in size_circuits[:3] :
    #     sol *= size
    sol = points[last_connection[0]][0] * points[last_connection[1]][0]
    print(sol)



def main90() :
    points = []
    with open("AoC\\2025\\input9.txt", "r") as file :
        for i, line in enumerate(file) :
            line = "".join([c for c in line if c != "\n"])
            corrds = [int(corrd) for corrd in line.split(",")]
            points.append(corrds)
    areas = []
    for p1 in range(len(points)-1) :
        for p2 in range(p1+1,len(points)) :
            dx = abs(points[p1][0]-points[p2][0]+1)
            dy = abs(points[p1][1]-points[p2][1]+1)
            areas.append(dx*dy)
    areas.sort(reverse=True)
    print(areas[0])



def main91() :
    points = []
    biggest_x = -1
    biggest_y = -1
    with open("AoC\\2025\\input9.txt", "r") as file :
        for i, line in enumerate(file) :
            line = "".join([c for c in line if c != "\n"])
            corrds = [int(corrd) for corrd in line.split(",")]
            if corrds[0] > biggest_x :
                biggest_x = corrds[0]
            if corrds[1] > biggest_y :
                biggest_y = corrds[1]
            points.append(corrds)
    # print("Startar med grid")
    # grid = [["." for i in range(biggest_y+3)] for j in range(biggest_x+2)]
    # print("färdig med grid")
    nbr_points = len(points)
    grid = {}
    grid2 = {}
    u_counter = set()
    # print_grid(grid, biggest_x+2, biggest_y+3)
    for i, point in enumerate(points) :
        print(i+1, "out of", nbr_points, end='\r')
        x,y = point
        grid[(x,y)] = "#"
        grid2[(x,y)] = "#"
        oldx, oldy = points[i-1]
        start_int, end_int, const = (-1,-1,-1)
        direction = 0
        if x == oldx :
            const = x
            if y > oldy :
                start_int = oldy
                end_int = y
                direction = -1
            else :
                start_int = y
                end_int = oldy
                direction = 1
        else :
            const = y
            if x > oldx :
                start_int = oldx
                end_int = x
                direction = 1
            else :
                start_int = x
                end_int = oldx
                direction = -1
        for j in range(start_int+1, end_int) :
            if x == oldx :
                if grid.get((const-direction,j),".") == "." :
                    grid[(const-direction,j)] = "U"
                    u_counter.add((const-direction,j))
                if "U" in grid.get((const,j),".") or "I" in grid.get((const,j),".") :
                    print("Collition")
                grid[(const,j)] = "X"
                grid2[(const,j)] = "*"
                if grid.get((const+direction,j),".") == "." :
                    grid[(const+direction,j)] = "I"
            else :
                if grid.get((j,const-direction),".") == "." :
                    grid[(j,const-direction)] = "U"
                    u_counter.add((j,const-direction))
                if "U" in grid.get((j,const),".") or "I" in grid.get((j,const),".") :
                    print("Collition")
                grid[(j,const)] = "X"
                grid2[(j,const)] = "*"
                if grid.get((j,const+direction),".") == "." :
                    grid[(j,const+direction)] = "I"
    print()
    # print_grid(grid, biggest_x+2, biggest_y+3)
    # print(len(u_counter))
    areas = []
    for p1 in range(len(points)-1) :
        for p2 in range(p1+1,len(points)) :
            dx = abs(points[p1][0]-points[p2][0])+1
            dy = abs(points[p1][1]-points[p2][1])+1
            areas.append((dx*dy,(points[p1],points[p2])))
    areas.sort(reverse=True)
    sol = -1
    for i, (area, ((x1,y1),(x2,y2))) in enumerate(areas) :
        print(i+1, "out of", len(areas), end='\r')
        xs = [x1,x2]
        ys = [y1,y2]
        xs.sort()
        ys.sort()
        # print(xs, ys)
        valid = True
        # for i in range(xs[0],xs[1]) :
        #     for j in range(ys[0],ys[1]) :
        #         if grid.get((i,j),".") == "U" :
        #             valid = False
        #             break
        #     if not valid :
        #         break

        for (x,y) in u_counter :
            if xs[0] < x and x < xs[1] :
                if ys[0] < y and y < ys[1] :
                    valid = False
                    break
        if valid :
            sol = area
            grid2[(x1,y1)] = "O"
            grid2[(x2,y2)] = "O"
            break
    # print_grid(grid, biggest_x+2, biggest_y+3)
    # print_grid(grid2, biggest_x+2, biggest_y+3)
    print()
    print(sol)

def print_grid(grid, x_size, y_size) :
    new_grid = [[grid.get((i,j)," ") for i in range(x_size)] for j in range(y_size)]
    for row in new_grid :
        print("".join(row))

def generateInput9() :
    mod = 20
    with open("AoC\\2025\\data9.txt", "w") as file:
            first = 1
            second = 1
            file.write(str(first) + "," + str(second) + "\n")
            for i in range(3) :
                first = int((first + rn.randint(2,mod-2)) % mod)
                file.write(str(first) + "," + str(second) + "\n")
                second = int((second + rn.randint(2,mod-2)) % mod)
                file.write(str(first) + "," + str(second) + "\n")
            file.write(str(1) + "," + str(second) + "\n")



## Does a lot of dubbel counting, want to fix that!
def main100() :
    machines = []
    with open("AoC\\2025\\input10.txt", "r") as file :
        for i, line in enumerate(file) :
            line = "".join([c for c in line if c != "\n"])
            machine = []
            buttons = []
            for elem in line.split(" ") :
                if "[" in elem :
                    lamps = [1 if c == "#" else 0 for c in elem[1:-1]]
                    machine.append(lamps)
                elif "(" in elem :
                    button = [1 if str(n) in elem else 0 for n in range(len(lamps))]
                    buttons.append(button)
                else :
                    machine.append(buttons)
                    machine.append([int(n) for n in elem[1:-1].split(",")])
            machines.append(machine)
    sol = 0
    
    for i, (lamps, buttons, joltages) in enumerate(machines) :
        print(i+1, "out of", len(machines), end='\r')
        combs = [[0]*len(lamps)]
        presses = 0
        check = True
        while check :
            presses += 1
            temp = []
            for comb in combs :
                for button in buttons :
                    new_comb = addMod(comb, button)
                    if new_comb != lamps :
                        temp.append(new_comb)
                    else :
                        check = False
                        break
                if not check :
                    break
            combs = temp
        sol += presses
    print()
    print(sol)

def addMod(l1, l2) :
    return [(l1[i] + l2[i]) % 2 for i in range(len(l1))]


# Not Working...
def main101() :
    machines = []
    with open("AoC\\2025\\input10_test.txt", "r") as file :
        for i, line in enumerate(file) :
            line = "".join([c for c in line if c != "\n"])
            machine = []
            buttons = []
            for elem in line.split(" ") :
                if "[" in elem :
                    lamps = [1 if c == "#" else 0 for c in elem[1:-1]]
                    machine.append(lamps)
                elif "(" in elem :
                    button = [1 if str(n) in elem else 0 for n in range(len(lamps))]
                    buttons.append(button)
                else :
                    machine.append(buttons)
                    machine.append([int(n) for n in elem[1:-1].split(",")])
            machines.append(machine)
    sol = []
    
    for i, (lamps, buttons, joltages) in enumerate(machines) :
        print(i+1, "out of", len(machines), end='\r')
        combs = [[0]*len(joltages)]
        presses = 0
        check = True
        while check :
            presses += 1
            temp = []
            for comb in combs :
                for button in buttons :
                    new_comb = add(comb, button)
                    if new_comb != joltages :
                        temp.append(new_comb)
                    else :
                        check = False
                        break
                if not check :
                    break
            combs = temp
        print()
        print(presses)
        sol.append(presses)
    print()
    print(sol)
    print(sum(sol))

def add(l1, l2) :
    return [(l1[i] + l2[i]) for i in range(len(l1))]



def main110() :
    nodes = []
    dict = {}
    you = -1
    out = -1
    with open("AoC\\2025\\input11.txt", "r") as file :
        for i, line in enumerate(file) :
            line = "".join([c for c in line if c != "\n"])
            temp = []
            for node in line.split(" ") :
                if ":" in node :
                    dict[node[:-1]] = len(dict)
                else :
                    temp.append(node)
            nodes.append(temp)
        you = dict["you"]
        out = len(dict)
        nodes = [[dict[con] if con != "out" else out for con in node] for node in nodes]
    
    current = [you]

    while set(current) != set([out]) :
        temp = []
        for node in current :
            if node != out :
                temp += nodes[node]
            else :
                temp += [node]
        current = temp
    print(len(current))



def main111() :
    nodes = []
    dict = {}
    svr = -1
    out = -1
    fft = -1
    dac = -1
    with open("AoC\\2025\\input11.txt", "r") as file :
        for i, line in enumerate(file) :
            line = "".join([c for c in line if c != "\n"])
            temp = []
            for node in line.split(" ") :
                if ":" in node :
                    dict[node[:-1]] = len(dict)
                else :
                    temp.append(node)
            nodes.append(temp)
        svr = dict["svr"]
        fft = dict["fft"]
        dac = dict["dac"]
        out = len(dict)
        nodes = [[dict[con] if con != "out" else out for con in node] for node in nodes]
    
    current_no = [svr]
    current_fft = []
    current_dac = []
    current_done = []

    while set(current_no).union(set(current_fft)).union(set(current_dac)).union(set(current_done)) != set([out]) :
        print("Size of Nodes:", len(current_no) + len(current_fft) + len(current_dac) + len(current_done), end='\r')
        temp_no = []
        temp_fft = []
        temp_dac = []
        temp_done = []
        for node in current_no :
            if node == out :
                print("Be Gone")
            elif node == fft :
                temp_fft += nodes[node]
            elif node == dac :
                temp_dac += nodes[node]
            else :
                temp_no += nodes[node]
        
        for node in current_fft :
            if node == out :
                print("Be Gone")
            elif node == dac :
                temp_done += nodes[node]
            else :
                temp_fft += nodes[node]
        
        for node in current_dac :
            if node == out :
                print("Be Gone")
            elif node == fft :
                temp_done += nodes[node]
            else :
                temp_dac += nodes[node]

        for node in current_done :
            if node == out :
                temp_done += [node]
            else :
                temp_done += nodes[node]

        current_no = temp_no
        current_fft = temp_fft
        current_dac = temp_dac
        current_done = temp_done
    print()
    print(len(current_done))

main111()
