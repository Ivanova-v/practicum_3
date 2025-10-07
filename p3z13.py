stroki = int(input())
stolbi = int(input())
nomer = int(input())
stranica = stroki * stolbi
nom_str = (nomer - 1) // stranica + 1
stroka_i = (nomer - 1) % stranica + 1
stolb = (stroka_i - 1) // stroki + 1
position = (stroka_i - 1) % stroki + 1
print(f'страница {nom_str} столбец {stolb} строка {position}')