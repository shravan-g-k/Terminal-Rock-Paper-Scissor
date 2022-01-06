while True :
    import random
    ranno = random.randint(1,3)
    print("****please choose either 'r' or 'p' or 's' ****")
    user = str(input('Your Turn choose :- \n🧱ROCK[r]\n📃PAPER[p]\n✂ SCISSOR[s]\n - '))

    comp = ranno
    if comp==1:
        comp = "r"
    elif comp == 2:
        comp = "p"
    elif comp == 3 :
        comp = "s"
    if user == comp:
        result = '🤝TIE'
    elif comp == "r" and user == "p" or comp == "p" and user == "s" or comp == "s" and user == "r" :
        result = 'YOU WIN 🥇'
    else :
        result = 'YOU LOST👎'
    print(f'{result}, As computer choose - {comp} ')
