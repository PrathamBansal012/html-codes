def find_prob(a,b):

    if a==1:
        prob_a = 0.2
        if b==1:
            prob_bga = 0.85
        elif b==2:
            prob_bga = 0.15
        else:
            print("Invalid Choice")
        prob_a_and_b = prob_a * prob_bga
        print("Probability of b given a:", prob_bga)
        print("Probability of both the events occuring:", prob_a_and_b)

    elif a==2:
        prob_a = 0.8
        if b==1:
            prob_bga = 0.02
        elif b==2:
            prob_bga = 0.98
        else:
            print("Invalid Choice")
        prob_a_and_b = prob_a * prob_bga
        print("Probability of b given a:", prob_bga)
        print("Probability of both the events occuring:", prob_a_and_b)
    else:
        print("invalid")
print("lets calculate")
print("person has \n1. yes \n2. no")
a=int(input("enter"))
print("person has \n1. yes \n2.1" \
" no")
b=int(input("enter"))
print("Probability of both the events occuring:")
find_prob(a,b)