# RPS Component 3 - generate user choice and computer choice
rps_list = ["rock", "paper", "scissors"]
comp_index = 0

for item in rps_list:
    user_index = 0
    for item in rps_list:
            user_choice = rps_list[user_index]
            comp_choice = rps_list[comp_index]
            user_index += 1

            # Compare options..
            print("user:{}  vs computer:{} ".format(user_choice, comp_choice))

            if user_choice == comp_choice:
                result = "tie"
            elif user_choice == "rock" and comp_choice == "scissors":
                result = "win"
            elif user_choice == "paper" and comp_choice == "rock":
                result = "win"
            elif user_choice == "scissors" and comp_choice == "paper":
                result = "win"
            else:
                result = "lose"

            print("You chose {}, the computer chose {}."
                  "\nResults: {}".format(user_choice, comp_choice, result))

    comp_index += 1
    print()