import numpy as np


matrice = np.array([[(3, 2), (7, 4), (4, 0)],
                    [(12, 1), (11, 3), (12, 1)],
                    [(1, 4), (0, 5), (0, 2)]])


gain_a = matrice[:, :, 0]
print(gain_a)

# Player A
def find_dominant_strategy_for_player_a(matrice):
    dominant_strategie = []
    for i in range(gain_a.shape[0]):
        is_dominant = True
        for j in range(gain_a.shape[0]):
            if i != j and not all(gain_a[i] > gain_a[j]):
                is_dominant = False
                break
        if is_dominant:
            dominant_strategie.append(i)
    return dominant_strategie


dominant_strategie_a = find_dominant_strategy_for_player_a(matrice)


if dominant_strategie_a is not None :
    print(f"Player A has a dominant strategy at row: {['A' + str(i+1) for i in dominant_strategie_a]}")
    Player_a = True
else:
    print("Player A does not have a dominant strategy.")



# Player B
gain_b = matrice[:, :, 1]


def find_dominant_strategy_for_player_b(matrice):

    dominant_strategie = []
    for i in range(matrice.shape[1]):  
        is_dominant = True
        for j in range(matrice.shape[1]):  
            if i != j and not all(matrice[:, i] > matrice[:, j]):
                is_dominant = False
                break
        if is_dominant:
            dominant_strategie.append(i)
    return dominant_strategie


dominant_strategie_b = find_dominant_strategy_for_player_b(gain_b)


if dominant_strategie_b:
    print(f"Player B has a dominant strategy at column: {['B' + str(i+1) for i in dominant_strategie_b]}")
    Player_b = True
else:
    print("Player B does not have a dominant strategy.")

if Player_a & Player_b : 
    print("Il y a un equilibre.")