# You now the game

import random
s = 0
co = 13
ro = 5
m = 3

range_ = co*ro
max_ = range_*m

def print_list(list_, c, s, l):
    p_list = []
    for e in list_:
        se = str(e)
        for i in range(l-len(se)):
            se += " "
        if len(p_list) < c:
            p_list.append(se)
        else:
            print(s.join(p_list))
            p_list = [se]
    print(s.join(p_list))


while True:
    print(f"\nGuess game.\nChoose number between {s} and {max_}\nType \"start\" to start the game or \"config\" to configure the game or \"setup\" to show the current configuration")
    while True:
        start_ = input()
        if start_ in ["start", "config", "setup"]: break
        else: print("Invalid input!")
    if start_ == "config":
        print(f"\nEnter the number of columns (default {co}):")
        input_ = input()
        co = int(input_) if input_ else co
        print(f"columns set to {co}\n")
        print(f"Enter the number of rows (default {ro}):")
        input_ = input()
        ro = int(input_) if input_ else ro
        print(f"rows set to {ro}\n")
        print(f"Enter the number range multiplier (default {m}, must be more then 1):")
        input_ = input()
        m = int(input_) if input_ and int(input_) > 1 else m
        print(f"range multiplier set to {m}\n")
        range_ = co*ro
        max_ = range_*m
        print(f"Enter the minimum number for the list (default {s}, must be less then the max {max_}):")
        input_ = input()
        s = int(input_) if input_ and int(input_) < max_ else s
        print(f"Minimum number set to {s}\n")
    if start_ == "setup":
        print(f"\ncolumns: {co}")
        print(f"rows: {ro}")
        print(f"range multiplier: {m}")
        print(f"minimum number: {s}\n")
    eliminate_num = set()
    guess = set()
    g_range = range(s, max_)
    while start_ == "start":
        list_num = set(random.sample(g_range, range_))
        print_list(list_num, co, " | ", len(str(max_)))
        print("Is your number in the list? yes/no")
        guess = set(guess)-eliminate_num
        if len(guess) == 1:
                print(f"Is this your number? {list(guess)[0]} yes/no")
                exit_ = False
                while True:
                    ans_ = input()
                    if ans_ == "yes":
                        exit_ = True
                        break
                    elif ans_ == "no":
                        break
                    else: print("Invalid input!")
                if exit_: break
        b = False
        while True:
            ans = input()
            if ans == "yes":
                guess = list_num.intersection(guess) if guess else list_num
                break
            elif ans == "no":
                eliminate_num |= set(list_num) - eliminate_num
                if len(eliminate_num) >= len(g_range):
                    print("All numbers are eliminated!")
                    b = True
                break
            else: print("Invalid Input!")
        if b: break