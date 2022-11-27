money = int(input("Введите сумму которую инвестируете:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
procent = list(per_cent.values())
bankTKB = round(procent[0]/100*money)
bankCKB = round(procent[1]/100*money)
bankVTB = round(procent[2]/100*money)
bankSBER = round(procent[3]/100*money)
deposit = [bankTKB, bankCKB, bankVTB, bankSBER]
print("Возможный доход:", deposit)
deposit.sort()
print("Максимальная сумма, которую вы можете заработать - ", deposit[-1])