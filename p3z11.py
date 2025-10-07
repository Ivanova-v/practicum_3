n = float(input())
if 0 <= n < 360:
    seconds = 43200
    gradus_1 = seconds // 360
    vse_dannie_sec = gradus_1 * n
    minutes = vse_dannie_sec // 60
    hours = minutes // 60
    minutes_ost = minutes - hours * 60
    print(int(hours), int(minutes_ost))