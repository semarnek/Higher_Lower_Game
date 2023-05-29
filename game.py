import random
import art
import game_data


def compare(f_comp, s_comp):
    if f_comp["follower_count"] > s_comp["follower_count"]:
        return f_comp
    else:
        return s_comp

score = 0
end_of_game = False

comp_a = {}
comp_b = {}

while end_of_game == False:

    user_choose = ""
    if score == 0:
        comp_a = random.choice(game_data.data)

    comp_b = random.choice(game_data.data)
    while comp_b == comp_a:
        comp_b = random.choice(game_data.data)
    print(art.logo)

    if score != 0:
        print(f"You're right! Current score: {score}")
    print(f"Compare A: {comp_a['name']}, a/an {comp_a['description']}, from {comp_a['country']}.")
    print(art.vs)
    print(f"Against B: {comp_b['name']}, a/an {comp_b['description']}, from {comp_b['country']}.")
    user_choose = input("Who has more followers? Type 'A' or 'B': ")

    result = compare(comp_a, comp_b)

    if user_choose == "a" or user_choose == "A":
        user_choose = comp_a
    elif user_choose == "b" or user_choose == "B":
        user_choose = comp_b


    if result == user_choose:
        score +=1
        comp_a = result
    else:
        end_of_game = True
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}.")
