from itertools import combinations

txt_input = open('a_example','r').readlines()

"""Get challenge info and turn into int"""
challenge_info = txt_input[0].split(" ")
challenge_info.pop()
for number in range(0,len(challenge_info)):
    challenge_info[number] = int(challenge_info[number])

"""Pizza ingredients and hash table"""
pizza_info = txt_input[1:len(txt_input)]
pizza_array = []
for _pizza in pizza_info:
    pizza_array.append([_pizza.strip("\n")])
pizza_stack = []
pizza_options = []
for _array in pizza_array:
    pizza_stack.append([word for line in _array for word in line.split()])
    pizza_options.append([word for line in _array for word in line.split()])
for pizza in pizza_stack:
    del pizza[0]
for pizza in pizza_options:
    del pizza[0]


"""Information about the challenge"""
num_pizzas = challenge_info[0]
total_ppts = (challenge_info[1]*2) + (challenge_info[2]*3) + (challenge_info[3]*4)
total_teams = challenge_info[1] + challenge_info[2] + challenge_info[3]
ppts_array = [challenge_info[1]*2, challenge_info[2]*3, challenge_info[3]*4]

"""Work out how many deliveries and what combinations"""
team_deliveries = {
    '2_team': 0,
    '3_team': 0,
    '4_team': 0
}
while num_pizzas > 4:
    pointer = 0
    if pointer == 0 and ppts_array[pointer] != 0:
        num_pizzas -= 2
        team_deliveries['2_team'] += 1
        ppts_array[pointer] -= 2
        pointer += 1
    elif pointer == 1 and ppts_array[pointer] != 0:
        num_pizzas -= 3
        team_deliveries['3_team'] += 1
        ppts_array[pointer] -= 3
        pointer += 1
    elif pointer == 2 and ppts_array[pointer] != 0:
        num_pizzas -= 4
        team_deliveries['4_team'] += 1
        ppts_array[pointer] -= 4
        pointer = 0
"""Final checks"""
if num_pizzas == 4:
    if ppts_array[2] > 3:
        num_pizzas -= 4
        team_deliveries['4_team'] += 1
    elif ppts_array[1] > 2:
        num_pizzas -= 3
        team_deliveries['3_team'] += 1
    elif ppts_array[0] > 1:
        num_pizzas -= 2
        team_deliveries['2_team'] += 1
elif num_pizzas == 3:
    if ppts_array[1] > 2:
        num_pizzas -= 3
        team_deliveries['3_team'] += 1
    elif ppts_array[0] > 1:
        num_pizzas -= 2
        team_deliveries['2_team'] += 1
elif num_pizzas == 2:
    if ppts_array[0] > 1:
        num_pizzas -= 2
        team_deliveries['2_team'] += 1

"""Combination calculations"""
submission_array = []
for key, value in team_deliveries.items():
    if not pizza_stack:
        break
    else: 
        if key == '2_team' and value > 0:
            comb = combinations(pizza_stack, 2)
            best_combo = {
                'unique_ingredients': 0,
                'best_combo': None
            }
            for i in comb:
                if len(set(list(i[0]) + list(i[1]))) > best_combo['unique_ingredients']:
                    best_combo['unique_ingredients'] = len(set(list(i[0]) + list(i[1])))
                    best_combo['best_combo'] = list(i)
            submission_array.append(best_combo)
            team_deliveries['2_team'] -= 1
            for i in best_combo['best_combo']:
                if i in pizza_stack:
                    pizza_stack.remove(i)
        elif key == '3_team' and value > 0:
            comb = combinations(pizza_stack, 3)
            best_combo = {
                'unique_ingredients': 0,
                'best_combo': None
            }
            for i in comb:
                if len(set(list(i[0]) + list(i[1]) + list(i[2]))) > best_combo['unique_ingredients']:
                    best_combo['unique_ingredients'] = len(set(list(i[0]) + list(i[1]) + list(i[2])))
                    best_combo['best_combo'] = list(i)
            submission_array.append(best_combo)
            team_deliveries['3_team'] -= 1
            for i in best_combo['best_combo']:
                if i in pizza_stack:
                    pizza_stack.remove(i)
        elif key == '4_team' and value > 0:
            comb = combinations(pizza_stack, 3)
            best_combo = {
                'unique_ingredients': 0,
                'best_combo': None
            }
            for i in comb:
                if len(set(list(i[0]) + list(i[1]) + list(i[2]) + list(i[3]))) > best_combo['unique_ingredients']:
                    best_combo['unique_ingredients'] = len(set(list(i[0]) + list(i[1]) + list(i[2]) + list(i[3])))
                    best_combo['best_combo'] = list(i)
            submission_array.append(best_combo)
            team_deliveries['4_team'] -= 1
            for i in best_combo['best_combo']:
                if i in pizza_stack:
                    pizza_stack.remove(i)

"""Submission"""
print(len(submission_array))
for pizza_object in submission_array:
    team_number = 0
    if len(pizza_object['best_combo']) == 2:
        team_number = str(2)
    elif len(pizza_object['best_combo']) == 3:
        team_number = str(3)
    elif len(pizza_object['best_combo']) == 4:
        team_number = str(4)
    final_pizzas = []
    for pizza in pizza_object['best_combo']:
        final_pizzas.append(str(pizza_options.index(pizza)))
    print(' '.join(final_pizzas))

"""Scoring"""
final_score = 0
for j in submission_array:
    final_score += (j['unique_ingredients']**2)
print('Final Score:', final_score)



        
