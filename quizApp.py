from art import logo
from questions import quiz
from replit import clear


def check_ans(question, ans, attempts, player):
    clear()
    """
    Takes the arguments, and confirms if the answer provided by user is correct.
    Converts all answers to lower case to make sure the quiz is not case sensitive.
    """
    if quiz[question]['answer'].lower() == ans.lower():
        print(f"Correct Answer! \n{player}'s score is {player_score[player] + 1}!")
        return True
    else:
        print(f"Wrong Answer :( \nYou have {attempts - 1} left! \nTry again...")
        return False


def print_dictionary():
    for question_id, ques_answer in quiz.items():
        for key in ques_answer:
            print(key + ':', ques_answer[key])


def intro_message():
    """
    Introduces user to the quiz and rules, and takes an input from customer to start the quiz.
    Returns true regardless of any key pressed.
    """
    print(logo)
    print("There are a total of 6 questions, you can skip a question anytime by typing 'skip'")
    input("Press any key to get started...")
    return True

def switch_users(p_user):
    if p_user == 0:
        return 1
    return 0

def print_winner(player1, player2):
    if player_score[player1] > player_score[player2]:
        print(f"{player1} WON! The score is {player_score[player1]}")
    elif player_score[player1] < player_score[player2]:
        print(f"{player2} WON! The score is {player_score[player2]}")
    else:
        print("It's DRAW!")
# python project.py
intro = intro_message()
players = input("Enter 2 Players with Space: ")
player_list = players.split(" ")
player_score = dict.fromkeys(player_list, 0)
current_player = player_list[0] #start with first player
for question in quiz:
    print("------------------------------")
    print(f"It is {current_player}'s turn.")
    attempts = 2
    while attempts > 0:
        print(quiz[question]['question'])
        answer = input("Enter Answer (To move to the next question, type 'skip') : ")
        if answer == "skip":
            break
        check = check_ans(question, answer, attempts, current_player)
        if check:
            player_score[current_player] += 1
            
            break
        attempts -= 1
        
    current_player_index = player_list.index(current_player)
    current_player = player_list[switch_users(current_player_index)]



print_winner(player_list[0], player_list[1])
correct_answer = input("Want to know the correct answers? (Y/N): ")
if correct_answer == "Y":
    print_dictionary()
print("Thanks for playing!")
