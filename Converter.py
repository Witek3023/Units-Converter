from lengthmodule import *
from timemodule import *
from terminaltables import AsciiTable
import os
import platform

# test

table_data = [
    ['1.Czas'],
    ['2.Długość'],
    ]
table = AsciiTable(table_data)
print(table.table)
mode = input('Wybierz co chcesz przekonwertować: ')

if platform.system() == 'Linux':
    os.system('clear')
    print('linux')
elif platform.system() == 'Windows':
    print('windows')
    os.system('cls')

match mode:
    case '1':
        mode_options = [
            ['1.Sekundy na minuty'],
            ['2.Minuty na Sekundy'],
            ['3.Sekundy na godziny'],
            ['4.Godziny na sekundy'],
            ['5.Godziny na minuty'],
            ['6.Minuty na godziny'],
        ]
        table = AsciiTable(mode_options)
        table.inner_heading_row_border = False
        print(table.table)
        option = input('Wybierz co chcesz przekonwertować: ')
        match option:
            case '1':
                number = float(input('Podaj ile sekund: '))
                result = sekmin(number)
                print(f'{number} sekund to {result} minut')
            case '2':
                number = float(input('Podaj ile minut: '))
                result = minsek(number)
                print(f'{number} minut to {result} sekund')
            case '3':
                number = float(input('Podaj ile sekund: '))
                result = sekhour(number)
                print(f'{number} sekund to {result} godzin')
            case '4':
                number = float(input('Podaj ile godzin: '))
                result = hoursek(number)
                print(f'{number} godzin to {result} sekund')
            case '5':
                number = float(input('Podaj ile godzin: '))
                result = hourmin(number)
                print(f'{number} godzin to {result} minut')
            case '6':
                number = float(input('Podaj ile minut: '))
                result = minhour(number)
                print(f'{number} minut to {result} godzin')
            case _:
                print('\nZła liczba')
    case '2':
        mode_options = [
            ['1.Centymetry na metry'],
            ['2.Metry na centymetry'],
            ['3.Centymetry na kilometry'],
            ['4.Kilometry na centymetry'],
            ['5.Kilometry na metry'],
            ['6.Metry na kilometry'],
        ]
        table = AsciiTable(mode_options)
        table.inner_heading_row_border = False
        print(table.table)
        option = input('Wybierz co chcesz przekonwertować: ')
        match option:
            case '1':
                number = float(input('Podaj ile centymetrów: '))
                result = cm_m(number)
                print(f'{number} centymetrów to {result} metrów')
            case '2':
                number = float(input('Podaj ile metrów: '))
                result = m_cm(number)
                print(f'{number} metrów to {result} centymetrów')
            case '3':
                number = float(input('Podaj ile centymetrów: '))
                result = cm_km(number)
                print(f'{number} centymetrów to {result} kilometrów')
            case '4':
                number = float(input('Podaj ile kilometrów: '))
                result = km_cm(number)
                print(f'{number} kilometrów to {result} centymetrów')
            case '5':
                number = float(input('Podaj ile kilometrów: '))
                result = km_m(number)
                print(f'{number} kilometrów to {result} metrów')
            case '6':
                number = float(input('Podaj ile metrów: '))
                result = m_km(number)
                print(f'{number} metrów to {result} kilometrów')
            case _:
                print('\nZła liczba')
    case _:
        print('\nZła liczba')

end = input('\nnaciśnij ENTER aby zakończyć')
