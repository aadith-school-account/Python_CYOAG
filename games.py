import time, random
from text_custom import typewriter

def button_mash_game(strength, luck):
    """Adjusts difficulty based on strength, use dictionary in main code."""
    if strength >= 10:
        target_presses = 5   # Very strong, doesn't need to mash much
        time_limit = 3       # More time since they're confident
    elif strength >= 5:
        target_presses = 10  # Balanced difficulty
        time_limit = 3
    else:
        target_presses = 15  # Weaklings suffer muahahahaah
        time_limit = 3       # Less time to make it stressful

    if luck >= 7:  # Lucky = easier!
        target_presses -= 2
        time_limit += 1
    elif luck <= 3:  # Unlucky = harder!
        target_presses += 2
        time_limit -= 1

    print(f"Your luck and strength stats will help you out, or hurt you...")
    print(f"Your luck is: {luck} and your strength is: {strength}")
    print(f"Quick! Press ENTER {target_presses} times in {time_limit} seconds!")

    input("Press ENTER to start...")

    start_time = time.time()
    presses = 0

    while time.time() - start_time < time_limit:
        input()  # Wait for the player to press ENTER
        presses += 1
        print(f"Presses: {presses}/{target_presses}")

        if presses >= target_presses:
            print("Congrats! You won!!")
            return True  # Victory

    print("You were too slow! You lost....")
    return False  # Failure

def riddle_game():
    riddle = "I have a head and a tail but no body... What am I??"
    correct_answer = "COIN"

    typewriter("Answer this riddle correctly... and you may pass!", 0.03)
    typewriter(riddle, 0.03)
    print('\n')

    player_answer = input("Your answer: ")
    player_answer = player_answer.strip()
    player_answer = player_answer.upper()

    if player_answer == correct_answer:
        typewriter("Wow.... that's the correct answer!")
        return True
    else:
        typewriter("Bum bum buuuuum, incorrect answer.... suckss to suck!")
        return False

def coin_game(luck):

    typewriter("Now you may flip the coin.... of DOOM!", 0.03)


    if luck >= 5:
        coin = 2
    else:
        coin = random.randint(1,2)

    if coin == 1:
        typewriter("It's your unlucky day...")
        typewriter("You rolled the DOOOM", 0.03)
        return False
    elif coin == 2:
        typewriter("Wow! Congrats!!! YOU WON!!!!")
        typewriter("You rolled the lucky head!", 0.03)
        return True
