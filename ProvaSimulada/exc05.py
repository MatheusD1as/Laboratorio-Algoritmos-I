diaNasc = int(input(""))
mesNasc = int(input(""))
anoNasc = int(input(""))

diaAtual = int(input(""))
mesAtual = int(input(""))
anoAtual = int(input(""))

diaResult = diaAtual - diaNasc
mesResult = mesAtual - mesNasc
anoResult  = anoAtual - anoNasc

if diaResult < 0 and mesResult < 0:
    print(anoResult -1,"anos", mesResult + 11,"meseses",diaResult +29,"dias")
elif diaResult > 0 and mesResult < 0:
    print(anoResult -1,"anos", mesResult + 12,"meseses",diaResult,"dias")
elif diaResult < 0 and mesResult > 0:
    print(anoResult,"anos", mesResult -1,"meseses",diaResult +29,"dias")
elif diaResult == 0 and mesResult < 0:
    print(anoResult -1,"anos", mesResult +12,"meseses",diaResult,"dias")
elif diaResult < 0 and mesResult == 0:
    print(anoResult-1,"anos", mesResult +11,"meseses",diaResult +29,"dias")
else:
    print(anoResult,"anos", mesResult,"meseses",diaResult,"dias")
