lista = []
lista.append([1, "kom in","Axel Bergenfeldt", "Ester Hagberg Kuylenstierna", "August Melin Skogum", "Pontus Thuresson", "Malte Callsen", "Anton Sundström", "Vilma Blidner", "Elina Kazemi", "Samin Ahmed Chowdhury", "Alva Rosberg", "Torild Källqvist Lidman", "Samuel Eriksson", "Edvin Ahlström", "Alicia Ahlgren", "Pontus Lindberg", "Magdalenda Ohlsson", "Erik Mällroth Franzén", "Isabella Brearwaldt", "Jonathan Malmquist", "Theodor Käll", "Hanna Lindström", "Lukas Andersson 7559", "Ellen Boström", "Ada Parén", "Erik Nord", "Sixten Georgsson", "Erik Fredriksson", "Hannes Lövholm", "Vic Kowalik", "Alma Holmgren", "Mattis Mattsson", "Lovisa Verselius", "Victor Rasmussen"])
lista.append([7, "kom in", "Hilding Andersson"])
lista.append([8, "kom in", "Wilhelm Branzell"])
lista.append([12, "kom in", "Ludvig Wadenbäck"])
lista.append([15, "kom in", "Jacob Hoas"])
lista.append([17, "kom in", "Wilhelm Branzell"])
lista.append([18, "kom in", "Emil Fredriksson"])
lista.append([18.1, "kom in", "Wilhelm Branzell"])
lista.append([19, "kom in", "Rebecka Eldh"])
lista.append([13, "gick ut", "Sixten Georgsson"])
lista.append([16, "gick ut", "Wilhelm Branzell"])
lista.append([18, "gick ut", "Ellen Boström", "Wilhelm Branzell"])
lista.append([19.2, "gick ut", "Hilding Andersson", "Edvin Ahlström", "Rebecka Eldh"])
lista.append([19.3, "gick ut", "Wilhelm Branzell", "Theodor Käll", "Emil Fredriksson", "Torild Källqvist Lidman"])
lista.append([19.6, "gick ut", "Jacob Hoas"])
lista.append([23, "gick ut", "RESTEN"])

# test = [["Axel","är ganska bra"]]

# for i in range(len(test)) :
#     if test[i][0] == "Axel" :
#         test[i][1] += "hej"

# print(test[0][1])

text = []
pers = []
inout = []
for l in lista :
    par = l[0]
    pref = l[1]
    for l1 in l[2:] :
        if l1 != "RESTEN" :
            try :
                ind = pers.index(l1)
            except :
                text.append([l1," §" + str(par) + " - " + pref + ","])
                pers.append(l1)
                inout.append(True)
            else :
                text[ind][1] += " §" + str(par) + " - " + pref + ","
                if pref == "gick ut" :
                    inout[ind] = False
                else :
                    inout[ind] = True
        else :
            for i in range(len(pers)) :
                if inout[i] == True :
                    text[i][1] += " §" + str(par) + " - " + pref + ","

for tex in text :
    ans = tex[0] + " &" + tex[1][:-1] + " \\\\"
    print(ans)
    print("\hline")



