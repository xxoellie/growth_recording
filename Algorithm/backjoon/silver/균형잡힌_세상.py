while True :
    corpus = input()
    if corpus == "." :
        break
    bracket_list = []
    answer = True

    for i in corpus :
        if i == "(" or i == "[" :
            bracket_list.append(i)

        elif i == ")" :
            if len(bracket_list) == 0 :
                answer = False
                break
            if bracket_list[-1] == "(":
                bracket_list.pop()
            else :
                answer = False
                break

        elif i == "]" :
            if len(bracket_list) == 0 :
                answer = False
                break
            if bracket_list[-1] == "[":
                bracket_list.pop()
            else :
                answer = False
                break
    if answer and not bracket_list :
        print("yes")
    else :
        print("no")