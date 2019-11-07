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
                    work_base.append(rule_base[i].split()[-1])
                    added = False
    return " Nothing found "

def backward_pass(rule_base, s):
    """

    :param rule_base:
    :param s:
    :return:
    """
    fact = []
    work_base = deque()
    work_base.append(s)
    while work_base:
        a = work_base.popleft()
        found = False
        if a in fact:
            found = True
            continue
        for i in range(len(rule_base)):
            if a == rule_base[i].split()[-1]:
                for j in rule_base[i].split()[:-1]:
                    if j in fact:
                        found = True
                    if j not in work_base:
                        work_base.append(j)
                        fact.append(j)
                        found = True
        if not found:
            print(" Not found "+str(a))
        print(fact)




def main():
    file = open("Rule_base.txt", "r")
    rule_base = file.readlines()
    file.close()
    for x in range(len(rule_base)):
        rule_base[x] = rule_base[x].replace("-", "")
    final_state = ["CR-V", "Accord", "NSX", "Pilot", "X250", "E63", "G500", "SLS", "Vits", "S63", "Vesta", "Нива",
                   "Газель", "LC200", "Camry", "Hillux", "Rav4", "GT86", "Focus", "Raptor", "Transit", "Explorer", "Cuga",
                   "Mustang", "GT40", "i40", "Solaris", "Sonata", "H-1", "X5", "X7", "M5", "Series7", "Q5", "Q7", "A7",
                   "A8", "R8", "Cruz", "Camaro", "Capita", "NIVA", "Tahoe"]
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
