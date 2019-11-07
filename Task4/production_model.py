import re
import sys
from collections import deque


def check_string(value):
    """
    Проверка строки для применения Forward и Backward
    :param value: строка считываемая с клавиатуры
    :return: True - строка подходит для применения Forward и Backward,
    False - строка не подходит для применения Forward и Backward
    """
    match = re.match("""^[а-яё \-_a-zA-Z]+$""", value)
    return bool(match)


def check_string_for_fact(value):
    """
    Проверка строки для применения Forward и Backward
    :param value: строка считываемая с клавиатуры
    :return: True - строка подходит для применения Forward и Backward,
    False - строка не подходит для применения Forward и Backward
    """
    match = re.match("""^[а-яё \-_a-zA-ZА-Я0-9]+$""", value)
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

    rule_base = list(reversed(rule_base))
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
                if rule_base[i].split() != []:
                    if rule_base[i].split()[-1] in final_state:
                        return rule_base[i].split()[-1]
                    if rule_base[i].split()[-1] not in work_base:
                        work_base.append(rule_base[i].split()[-1])
                        added = False
    return " Nothing found "


def backward_pass(rule_base, s, ax):
    """

    :param ax:
    :param rule_base:
    :param s:
    :return:
    """
    rule_base = list(reversed(rule_base))
    need_to_confirm = deque()
    facts = ax.split()
    basic_fact = []
    need_to_confirm.append(s)
    while need_to_confirm:
        if basic_fact:
            done = True
            for x in basic_fact:
                if x not in facts:
                    done = False
            if done:
                return True
        current = need_to_confirm.popleft()
        added = True
        for i in range(len(rule_base)):
            flag = True
            if rule_base[i].split():
                for x in rule_base[i].split()[:-1]:
                    if x not in facts:
                        flag = False
                if rule_base[i].split()[-1] == current:
                    for x in rule_base[i].split()[:-1]:
                        if x not in facts and x not in need_to_confirm:
                            need_to_confirm.append(x)
                if rule_base[i].split()[-1] == s:
                    for x in rule_base[i].split()[:-1]:
                        basic_fact.append(x)
                if flag:
                    if rule_base[i].split()[-1] not in facts:
                        facts.append(rule_base[i].split()[-1])

    return False


def main():
    file = open("Rule_base.txt", "r")
    rule_base = file.readlines()
    file.close()
    for x in range(len(rule_base)):
        rule_base[x] = rule_base[x].replace("-", "")
    final_state = ["CR-V", "Accord", "NSX", "Pilot", "X250", "E63", "G500", "SLS", "Vits", "S63", "Vesta", "Нива",
                   "Газель", "LC200", "Camry", "Hillux", "Rav4", "GT86", "Focus", "Raptor", "Transit", "Explorer",
                   "Cuga",
                   "Mustang", "GT40", "i40", "Solaris", "Sonata", "H-1", "X5", "X7", "M5", "Series7", "Q5", "Q7", "A7",
                   "A8", "R8", "Cruz", "Camaro", "Capita", "NIVA", "Tahoe"]
    print(" Hello, enter qualities of the car and program will predict the brand of the car")
    type = input(" Choose Forward(1) or Backward(2) ")
    if type == "1":
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
            print("Result : " + str(forward_pass(rule_base, s, final_state)))

    if type == "2":
        print(" For exit from input \" exit \" or \" break \"")
        print(" Example:купе мощная экономная")
        while True:
            correct_string = False
            s = ""
            print(" ==================================================== ")
            while not correct_string:
                s = input(" Enter not a confirmed fact: ")
                if s in ["exit", "break", "выход", "Exit", "Break", "Выход"]:
                    sys.exit()
                correct_string = check_string_for_fact(s)
                if not correct_string:
                    print("Error!")
            correct_string = False
            while not correct_string:
                ax = input(" Enter axioms: ")
                if ax in ["exit", "break", "выход", "Exit", "Break", "Выход"]:
                    sys.exit()
                correct_string = check_string(ax)
                if not correct_string:
                    print("Error!")
            print("Result : " + str(backward_pass(rule_base, s, ax)))


if __name__ == "__main__":
    main()
