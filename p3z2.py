seconds = 24*60*60
particular_second = int(input())
if 1 <= particular_second <= seconds:
    hours = particular_second // 3600
    minutes = particular_second // 60 - hours * 60
    second = particular_second - minutes * 60 - hours * 3600
    print(f'{hours} часов {minutes} минут {second} секунд')
