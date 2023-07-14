ano = int(input("Que ano quer analizar? "))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("o ano {} é BISSEXTO".format(ano))
else:
    print("O ano {} NÂO é BISSEXTO".format(ano))
