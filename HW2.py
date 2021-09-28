
def menu(file):
    '''Для конкретного csv файла предлагает выбрать необходимую команду для работы с ним
    '''
    print('''Выберите необходимую команду: 
    1. Вывести иерархию команд, т.е. департамент и все команды, которые входят в него
    2. Вывести сводный отчёт по департаментам
    3. Сохранить сводный отчёт из предыдущего пункта в виде csv-файла''')
    command = input()
    if int(command) == 1:
        return hierarchy(file)
    elif int(command) == 2:
        return print(report(file))
    elif int(command) == 3:
        return report_csv(file)

def hierarchy(f_csv):
    '''Возвращает информацию о Департаментах, отделах, находящихся в них,
       а также о составе команд, которые работают в данных отделах.
    '''
    import csv
    departmants = dict()
    dep_final = dict()
    positions = dict()
    team_dict = dict()
    with open(f_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter= ';')
        for row in reader:
            departmants[row['Департамент']] = departmants.get(row['Департамент'],[])+ [row['Отдел']]
            positions[row['Отдел']] = positions.get(row['Отдел'],[])+ [row['Должность']]
        teams_uniq = [set(i) for i  in departmants.values()]
        teams_uniq = [list(i) for i in teams_uniq]
        pos_uniq = [set(i) for i  in positions.values()]
        pos_uniq = [list(i) for i in pos_uniq]

        for i in teams_uniq:
            for j in range(len(i)):
                dep_final[i[j]] = pos_uniq.pop(0)
        for dep in range(len(departmants)):
            print("В департаменте " + "'"+f'{list(departmants.keys())[dep]}'+ "'" + ' находятся отделы '+ ", ".join(teams_uniq[dep]))
        print('В свою очередь, в каждом из отделов работают следующие специалисты:')
        for team in dep_final:
            print(team + ' - ' +', '.join(dep_final[team]))
    return

def report(f_csv):
    ''' Выводит сводный отчет по департаментам: название, численность,
        "вилка" зарплат в виде мин – макс, среднюю зарплату. Формат вывода - список с
        вложенными словарями, в которых ключами являются необходимые пункты отчета, а значениями -
        показатели для конкретных департаментов.
    '''
    labor = []
    wage = []
    min_wage = []
    max_wage = []
    aver_wage = []
    forks = []
    departmants = {}
    result = []
    import csv
    with open(f_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter= ';')
        for row in reader:
            departmants[row['Департамент']] = departmants.get(row['Департамент'],[])+ [row]
        for i in departmants:
            labor.append(len(departmants[i]))
            for j in departmants[i]:
                wage.append(j['Оклад'])
        wage = [int(i) for i in wage]
        k = 0
        for l in labor:
            max_wage.append(max(wage[k:l+k]))
            min_wage.append(min(wage[k:l+k]))
            aver_wage.append(round(sum(wage[k:l+k])/l),)
            k += l
        forks = [str(min_wage[i])+'-'+str(max_wage[i]) for i in range(len(min_wage))]
        for i in range(len(departmants.keys())):
            result.append({'Название Департамента': list(departmants.keys())[i] ,'Число сотрудников': labor[i], 'Вилка':forks[i] ,'Средняя зарплата':aver_wage[i]})
    return result

def report_csv(file):
    ''' Возвращает csv файл "Отчет", в котором выполнен сводный отчет по департаментам'''
    import csv
    with open("Отчет.csv", mode="w", encoding='utf-8') as w_file:
        header = ["Название Департамента", 'Число сотрудников', 'Вилка','Средняя зарплата']
        file_writer = csv.DictWriter(w_file, delimiter = ",",
                                     lineterminator="\r", fieldnames=header)
        file_writer.writeheader()
        file_writer.writerows(report(file))
    return print('Откройте файл "Отчет.csv"')
print('Введите название csv файла')
menu(input())


