import re
import sys

def check_string(value):
    """
    Проверка строки для применения Forward и Backward
    :param value: строка считываемая с клавиатуры
    :return: True - строка подходит для применения Forward и Backward,
    False - строка не подходит для применения Forward и Backward
    """
    match = re.match("""^[а-яё ]+$""", value)
    return bool(match)


def forward_pass(rule_base, s, final_state):
    """
    Прямой порядок — от фактов к заключениям. В экспертных си­стемах с прямыми выводами
    по известным фактам отыскивается заключение, которое из этих фактов следует.
    Если такое заключение удается найти, оно заносится в рабочую память.
    :param final_state: состояния, когда алгоритм заканчивается
    :param rule_base: база правил
    :param s: факты
    :return: заключение
    """
    work_base = s.split()
    added = False
    while not added:
        added = True
        for i in range(len(rule_base)):
            flag = True
            for x in rule_base[i].split()[:-1]:
                if x not in work_base:
                    flag = False
            if flag:
                if rule_base[i].split()[-1] in final_state:
                    return rule_base[i].split()[-1]
                work_base.append(rule_base[i].split()[-1])
                added = False
    return " Nothing found "


def main():
    file = open("Cars.txt", "r")
    rule_base = file.readlines()
    file.close()
    for x in range(len(rule_base)):
        rule_base[x] = rule_base[x].replace(",", "").replace("->", "")
    final_state = ["Audi", "Skoda", "Toyota", "Volkswagen", "Hyundai", "BMW", "Chery", "Honda", "Datsun", "Opel"]
    print(" Hello, enter qualities of the car and program will predict the brand of the car")
    print(" For exit from input \" exit \" or \" break \"")
    print(" Example:купе мощная экономная")
    while True:
        correct_string = False
        s = ""
        print(" ==================================================== ")
        while not correct_string:
            s = input(" Enter: ")
            if s in ["exit", "break", "выход", "Exit", "Break", "Выход"]:
                sys.exit()
            correct_string = check_string(s)
            if not correct_string:
                print("Error!")
        print("Result : "+str(forward_pass(rule_base, s, final_state)))


if __name__ == "__main__":
    main()
