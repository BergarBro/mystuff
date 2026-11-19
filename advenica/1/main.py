
def print_list(list) :
    for i, member in enumerate(list) :
        print(f"{i:<2}: {member}")

def print_text(list) :
    print(" ".join(list))

def shift_letter_right(letter, n) :
    return chr(((ord(letter) + n - 65) % 26) + 65)

def shift_word_right(word, n) :
    return "".join([shift_letter_right(l,n) for l in word])

def ceaser(words) :
    n = 26
    if type(words) == type("str") :
        words = [words]
    return [[shift_word_right(word, i) for i in range(n)] for word in words]

def count_freq(words) :
    count = {}
    all_words = "".join(words)
    len_words = len(all_words)
    all_letters = set(all_words)
    len_letters = len(all_letters)
    for letter in all_words :
        count[letter] = count.get(letter, 0) + 1
    freq = {letter: round(amount/len_words,5) for letter, amount in count.items()}
    return (count, freq)
    # print(len_letters)

def letter_freq() :
    with open("1/letter_freq", "r") as f :
        lines = f.readlines()
    freq = {}
    for line in lines :
        line = line.replace(" ","")
        letter = line[0]
        value = float(line[1:])
        freq[letter] = value
    return freq

def sort(dic) :
    return {k:v for k,v in sorted(dic.items(),key= lambda item : -item[1])}

def substitution(freq, real_freq) :
    size = min(len(freq),len(real_freq))
    freq_list = list(freq.keys())
    real_freq_list = list(real_freq.keys())
    sub = {}
    for i in range(size) :
        sub[freq_list[i]] = real_freq_list[i]
    return sub

def correct_sub(sub, l1, l2) :
    k1 = ""
    k2 = ""
    for k, v in sub.items() :
        if v == l1 :
            k1 = k
        if v == l2 :
            k2 = k
    sub[k1] = l2
    sub[k2] = l1
    return sub

def convert(words, sub) :
    return ["".join([sub[l] for l in word]) for word in words]

def find_sl(words, sizes) :
    size = len(sizes)
    n = len(words) - size + 1
    index = -1
    for i in range(n) :
        no_match = False
        for j in range(size) :
            if len(words[i+j]) != sizes[j] :
                no_match = True
                break
        if j == size - 1 and not no_match :
            index = i
            break
    if index == -1 :
        return "-"
    return index,words[index:index+size]

with open("1/trans", "r") as f:
    trans = f.readlines()

trans = "".join(trans)
trans = trans.replace("\n","")
trans_list = trans.split("/")
trans_list = [word.replace(" ","").lower() for word in trans_list]


print_list(trans_list)
# j = 4
# print(trans_list[j])

# print(ceaser(trans_list[j]))

real_freq = letter_freq()

(count, freq) = count_freq(trans_list)
count = sort(count)
freq = sort(freq)
real_freq = sort(real_freq)

sub = substitution(freq, real_freq)

sub = correct_sub(sub, "r", "h")
sub = correct_sub(sub, "r", "s")
sub = correct_sub(sub, "r", "a")
sub = correct_sub(sub, "n", "a")
sub = correct_sub(sub, "o", "n")
sub = correct_sub(sub, "d", "g")
sub = correct_sub(sub, "u", "l")
sub = correct_sub(sub, "d", "u")
sub = correct_sub(sub, "m", "u")
sub = correct_sub(sub, "f", "u")
sub = correct_sub(sub, "w", "p")
sub = correct_sub(sub, "p", "u")
sub = correct_sub(sub, "k", "b")
sub = correct_sub(sub, "v", "k")
sub = correct_sub(sub, "j", "q")


converted = convert(trans_list,sub)

# print(count)
# print(freq)
# print(real_freq)
print(find_sl(converted,[7,5]))
print(sub)
print_text(converted)