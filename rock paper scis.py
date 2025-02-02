import random
iter=1
comp_score=0
user_score=0
while(iter):
    user_input=(input("Rock\nScissor\nPaper"))
    comp_input=random.choice(["Rock","Paper","Scissor"])
    
    if(user_input==comp_input):
        print("Tie")
    elif((comp_input=='Rock' and user_input=='Scissor')or(comp_input=='Scissor' and user_input=='Paper')or(comp_input=='Paper' and user_input=='Rock')):
        comp_score+=1
        print("Computer win!")
    else:
        print("User Win")
        user_score+=1
    print("Do you wanr to continue if yes enter 1 else 0")
    iter=int(input())
print(f"user score: {user_score}\ncomputer score: {comp_score}")
