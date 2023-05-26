import random
user_score = 0
computer_score=0
choices = ['rock','paper','scissor']

while True:
    user_pick = input('Enter your choice(rock/paper/scissor/q to quit): ').lower()
    random_number=random.randint(0,2)
    computer_pick = choices[random_number]
    if user_pick == 'q':
        break
    print(computer_pick)
    if user_pick == computer_pick:
        print('you got the same')
    elif user_pick == 'rock' and computer_pick == 'scissor':
        user_score+=1
        print('you won')
    elif user_pick == 'paper' and computer_pick == 'rock':
        user_score+=1
        print('you won')
    elif user_pick == 'scissor' and computer_pick == 'paper':
        user_score+=1
        print('you won')
    else:
        print('you lose')
        computer_score+=1
print ('you quit')
print(f'you won {user_score} times')
print(f'computer won {computer_score} times')