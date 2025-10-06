cost_rubles, cost_pennies, purchases = map(int, input().split())
rubles = (cost_rubles * 100 + cost_pennies) * purchases // 100
pennies = (cost_rubles * 100 + cost_pennies) * purchases - rubles * 100
print(f'{rubles} руб. {pennies} коп.')
print("Первая строка\nВторая строка")