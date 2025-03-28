##########-imports-##########
import random, time, sys, os, threading
from time_functions import pause, countdown_timer
from text_custom import typewriter, to_color, load_animation
from games import button_mash_game, riddle_game, coin_game
from stats import character, battle, create_character
from ascii import *
import pygame

fancy_name = "Baron Maximilian Von Schnitzelworth, Keeper of the Velvet Cravat"

speed = 0
##########-MUSIC-##########
#music links
#https://www.youtube.com/watch?v=aAkMkVFwAoo - ALL I WANT FOR CHRISTMAS IS YOU
#https://www.youtube.com/watch?v=CQeezCdF4mk

def play_music_elevator():
    pygame.mixer.init()
    try:
        pygame.mixer.music.load("elevator_music.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)  # loop de loop
    except pygame.error:
        print(
            "Could not play music file. Make sure elevator_music.mp3 exists in the project directory."
        )

def play_music_christmas():
    pygame.mixer.init()
    try:
        pygame.mixer.music.load("all_i_want_for_christmas_is_you.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)  # loop de loop
    except pygame.error:
        print(
            "Could not play music file. Make sure elevator_music.mp3 exists in the project directory."
        )

def sad_trombone():
    #
    pygame.mixer.init()
    skibidi_sound = pygame.mixer.Sound(os.path.join('trombone_sad.mp3'))
    skibidi_sound.play()

##########-DEFINITIONS OF FUNCTIONS FOR CHOICE, CLEAR, AND MUSIC START-###########


def choose_option(num_options):
    while True:
        choice = input(f"Please choose a number from 1 - {num_options}: ")
        if choice.isdigit():
            # convert to integer
            choice = int(choice)
            # check to make sure its between 1 and num_options
            if 1 <= choice <= num_options:
                return choice
        else:
            print("Please write a digit")
        print("Invalid Choice, please enter a number between 1 and " +
              str(num_options))


def clear_screen():

    if os.name == 'nt':  # Checks to see if you're on windows
        os.system('cls')  # windows command to clear screen
    else:  # For Linux and macOS
        os.system('clear')  # linux/macOS command to clear screen

############-DEFINITIONS OF STORY FUNCTIONS-##########
music = input("Would you like to play music? (Y/N):")
music = music.upper()

if music.upper() == 'Y':

    print("Do you want to listen to... ")
    print("1: Christmas Music")
    print('2: Elevator Music')
    choice = choose_option(2)

    if choice == 2:
        play_music_elevator()

        music_thread = threading.Thread(target=play_music_elevator)
        music_thread.daemon = True  # Thread will stop when main program exits
        music_thread.start()

    elif choice == 1:
        play_music_christmas()

        music_thread = threading.Thread(target=play_music_christmas)
        music_thread.daemon = True  # Thread will stop when main program exits
        music_thread.start()
else:
    print("your loss :(")
    sad_trombone()

player = create_character(health=10, stamina=15)


# introduction, explain the rules
def game_explanation():
    global speed, player
    clear_screen()
    print("EXPAND YOUR CONSOLE!!!!!")
    try:
        speed = float(input("How fast would you like to type? \n(0.01 is super fast, 0.03 is moderate, and 0.05 is slow): "))
    except ValueError:
        speed = 0.01
        print('bruh moment')

    skip_intro = input("Would you like to skip the intro? Y/N: ")
    skip_intro = skip_intro.upper()


    if skip_intro == "Y":
        typewriter("If you say so...", 0.1)
        game_start()

    elif skip_intro == "N":
        typewriter("You have woken up in the body of a handsome stranger!!",
                   speed)
        typewriter(
            "At various points, you will have to make decisions that will impact your future!",
            speed)
        typewriter("Choose wisely!!!! ", speed)
        print('\n')
        # ANSI red, clear line?
        typewriter("\u001b[31mbeware of the sneaky goblins...\u001b[0m", 0.1)
        clear_screen()
        typewriter("Venture forward hero, and attempt to survive!", speed)
        pause()
        game_start()
    else:
        print('Bro, type "Y" or "N" smh, now you gotta restart')


# set the location start the game
def game_start():
    global speed, player
    pause()
    clear_screen()
    typewriter("You wake up in a forest and hear gobbys snarling around you",
               speed)
    print(to_color(ASCII_GOBLIN, 'red'))
    typewriter("Now you may choose. Would you like to...", speed)
    typewriter("1: Run away from the goblins (scaredy cat) ", speed)
    typewriter(ASCII_CAT, 0.01)
    time.sleep(0.2)
    typewriter("2: Fight the goblins, like the big buff macho person you are",
               speed)
    typewriter("3: Try to.. fall back asleep? I don't see how this would work",
               speed)

    choice_start = choose_option(3)

    clear_screen()

    if choice_start == 1:
        typewriter("You coward! I can't believe this...", speed)
        pause()
        choice_run_away_from_goblins()
    elif choice_start == 2:
        typewriter("Good choice! You stand tall and FIGHT", speed)
        choice_fight_the_goblin()
    elif choice_start == 3:
        choice_fall_asleep()


def choice_run_away_from_goblins():
    global speed, player
    clear_screen()
    time.sleep(2)
    typewriter("I can't believe you've been chosen to be the hero...", speed)
    typewriter("Well, you have what's coming for you!", speed)
    typewriter("Well, theres no point prolonging the inevitable.", speed)
    countdown_timer(5, 1)
    time.sleep(1)
    print(to_color("DRAGON FIGHT TIME", 'red'))
    dragon_fight()


def choice_fight_the_goblin():
    global speed, player
    typewriter(
        "Ah, a strong, buff, muscular person like you must \nneed more stats...",
        speed)
    player.allocate_stats(2)
    player.print_stats()
    pause()
    typewriter("That was well worthy of a glorious person like you", speed)
    load_animation("Well... fighting time", 0.1, 50)
    typewriter("You see yourself surrounded by goblins...", speed)
    typewriter("\nYou even see one with a spoon???", speed)
    time.sleep(0.5)
    if player.charm <= 5:
        print(
            to_color(
                f"{player.name}: Measly goblin, what hath you do with a spoon?",
                'red'))
        time.sleep(1.5)
        print(
            to_color("Goblin: Ummmmm sword home? lost? you sword mine",
                     'yellow'))
        time.sleep(1.5)
        print(
            to_color(f"{player.name}: I think not goblin, now we shall fight!",
                     'red'))
        time.sleep(1.5)
        result_goblin_fight = button_mash_game(player.strength, player.luck)
        time.sleep(1)
        clear_screen()
        if result_goblin_fight == True:
            typewriter("Wow, gloriously played hero! As expected!!!")
            typewriter(
                "Because you have overcame that fight, your rewards are expected"
            )
            player.allocate_stats(3)
            player.print_stats()
            end_of_goblin_encounter_win()
        else:
            typewriter("How....... how did you lose", speed)
            typewriter("You...... have brought shame to me", speed)
            typewriter("You have two choices now", speed)
            typewriter("1.Continue on with the shame, and lose your stats")
            typewriter("2. Risk exploding for a chance to keep them!")

            choice_goblin_fight_lose = choose_option(2)

            if choice_goblin_fight_lose == 1:
                player.remove_stat("health", 3)
                player.remove_stat("strength", 2)
                player.remove_stat("charm", 1)
                player.remove_stat("luck", 1)
                time.sleep(1)
                player.print_stats()
                typewriter(f"Now continue forward... {player.name}", speed)
                typewriter(f"And try to bring back the shame you lost", speed)
                pause()
                end_of_goblin_encounter_lose()
            else:
                print('wow')
                typewriter("Well, good luck!")
                win_or_lose = riddle_game()

                if win_or_lose == True:
                    clear_screen()
                    typewriter("Congrats!! well played", speed)
                    end_of_goblin_encounter_lose()
                else:
                    typewriter(
                        "You spontaneously combust from sucking at riddles",
                        speed)
                    typewriter("RIP")

    elif player.charm >= 6:
        typewriter("You lucky guy... ", 0.03)
        print(to_color(f"{player.name}: Yello, I come in peace ", 'red'))
        time.sleep(2)
        print(
            to_color("Goblin: Ummmmm ok we trust nice you. ogoaob bogg",
                     'yellow'))
        time.sleep(2)
        print(to_color(f"{player.name}: Well thats gnarly! Thanks!", 'red'))
        time.sleep(2)
        typewriter("Looks like you got away without fighting!", speed)
        pause()
        charmed_goblins()
    else:
        print("better fix dat cuz why are you here. DEBUG")


def choice_fall_asleep():
    global speed, player
    clear_screen()
    typewriter("I don't see how that would work... ", speed)
    typewriter("Well... you try to fall asleep!", speed)
    countdown_timer(5, 1)
    time.sleep(1)
    load_animation("ready to wake up?", 0.1, 50)
    typewriter("Whoa! You're surrounded by a bunch of small men???", speed)
    if player.charm >= 6:
        typewriter("They want to be your friend!", speed)
        print(to_color(f"{player.name}: What are you???????? HUH????", 'red'))
        time.sleep(2)
        print(
            to_color("Small Man: Whoa you're so cool, let's be friends! ",
                     'yellow'))
        time.sleep(2)
        print(to_color(f"{player.name}: Cool " + "\U0001F44D", 'red'))
        time.sleep(2)
        clear_screen()
        typewriter(
            "Over the next 10 years you slowly assimilate with their culture")
        typewriter("You learn more and more, and slowly become small yourself")
        typewriter("And you enjoy the finer things in life")
        print(ASCII_STICKMAN_FRISBEE)
        print('\n')
        typewriter("Like mini frisbee!", speed)
        time.sleep(2)
        clear_screen()
        time.sleep(1)
        typewriter("The end!")
    elif player.charm <= 5:
        typewriter("Oooooof.... looks like they're trying to rob you...", speed)
        typewriter("Of your stats! oh nose!!!!", speed)
        typewriter(
            "You may either take the L, or risk it all to keep your stats!",
            0.03)
        typewriter("1: Take the L ", speed)
        typewriter("2: Risk it all!", speed)
        choice_small_men = choose_option(2)

        if choice_small_men == 1:
            player.remove_stat("health", 3)
            player.remove_stat("strength", 2)
            player.remove_stat("charm", 1)
            player.remove_stat("luck", 1)
            time.sleep(1)
            player.print_stats()
            typewriter(f"Now continue forward... {player.name}", speed)
            typewriter(f"And try to bring back the shame you lost", speed)
            pause()
            robbed_small_men()
        elif choice_small_men == 2:
            clear_screen()
            small_men = coin_game(player.luck)
            if small_men == True:
                typewriter(
                    "Hell yeah!!! Now you may go back to adventuring!",
                    speed)
                coin_small_men()
            elif small_men == False:
                typewriter(".....", 0.03)
                typewriter("You spontaneously combust lol", speed)
                typewriter("RIP")


# NOW ONTO SECONDARY STORY FUNCTIONS, AFTER FIRST ROUND!
# MUST ADD: DRAGON FIGHT FOR RUNAWAY(END)


def end_of_goblin_encounter_win():
    global speed, player
    clear_screen()
    typewriter("Wow.... good job fighting against the goblins", speed)
    typewriter(
        "You see someone approaching you from far away, with a long cape and a fancy sword",
        speed)
    print(
        to_color(f"{player.name}: Who are you and what do you want from me?",
                 'red'))
    time.sleep(2)
    print(
        to_color(
            "Stranger: Hello hero! I have come to request thee for thy help!",
            'yellow'))
    time.sleep(2)
    print(
        to_color(
            f"{player.name}: Well what's in it for me... no way I'm doing that for free",
            'red'))
    time.sleep(2)
    print(to_color("Stranger: Oh fudge.. didn't see that coming", 'yellow'))
    time.sleep(2)
    print(
        to_color("Stranger: Well I got this nice sword here " + "\U0001F44D",
                 'yellow'))
    time.sleep(2)
    print(to_color(ASCII_SWORD_COOL, 'blue'))
    time.sleep(1)
    print(to_color(f"{player.name}: OOOOOH ME WANT", 'red'))
    time.sleep(2)
    print(to_color("Stranger: Well it looks like we have a deal!", 'yellow'))
    time.sleep(2)
    clear_screen()
    print(
        to_color("Stranger: Now you just have to... fight a dragon", 'yellow'))
    time.sleep(2)
    print(to_color(f"{player.name}: fudge", 'red'))
    time.sleep(2)
    player.strength += 10
    typewriter("You gained 10 strength for picking up the cool sword", 0.03)
    player.print_stats()
    print(to_color("Stranger: Let's go to the village now!", 'yellow'))
    time.sleep(2)

    village_no_allies()


def end_of_goblin_encounter_lose():
    global speed, player
    clear_screen()
    typewriter("losing is crazy " + "\U0001F926")
    typewriter("As you look off into the distance, wondering about your loss",
               speed)
    typewriter(
        "You see a strange man approaching from far away, with a spicky spanny sword",
        speed)
    print(
        to_color(f"{player.name}: Who are you and what do you want from me?",
                 'red'))
    time.sleep(2)
    print(
        to_color(
            "Stranger: Hello hero! I have come to request thee for thy help!",
            'yellow'))
    time.sleep(2)
    print(
        to_color(
            "Stranger: Although I am unsure if I need your help considering the fact that you lost",
            'yellow'))
    time.sleep(2)
    print(
        to_color(
            f"{player.name}: Well what's in it for me... no way I'm doing that for free",
            'red'))
    time.sleep(2)
    print(
        to_color(
            "Stranger: Oh fudge.. didn't see that coming from a loser like you",
            'yellow'))
    time.sleep(2)
    print(
        to_color(
            "Stranger: Well I got this nice sword here, not sure if you're worthy of it "
            + "\U0001F44D", 'yellow'))
    time.sleep(2)
    print(to_color(ASCII_SWORD_UNCOOL, 'blue'))
    time.sleep(1)
    print(to_color(f"{player.name}: It's so... small?", 'red'))
    time.sleep(2)
    print(
        to_color(
            "Stranger: Well I think it's average personally, but do we have a deal?",
            'yellow'))
    time.sleep(2)
    print(to_color(f"{player.name}: I geuss...?", 'red'))
    clear_screen()
    print(
        to_color("Stranger: Now you just have to... fight a dragon", 'yellow'))
    time.sleep(2)
    print(to_color(f"{player.name}: fudge", 'red'))
    player.strength += 5
    typewriter("You gained 5 strength for picking up the sword!", 0.03)
    player.print_stats()
    print(to_color("Stranger: Let's go to the village now!", 'yellow'))
    time.sleep(2)

    village_no_allies()


def charmed_goblins():
    global speed, player
    clear_screen()
    typewriter(
        "You may have gotten away without fighting, but as you walk away you look behind you",
        speed)
    typewriter("AND YOU SEE 20 GOBLINS FOLLOWING YOU????", speed)
    typewriter("You were far too charming, and now you have some allies!",
               speed)
    print('\n')
    typewriter("You gained.... friendship!")
    pause()
    clear_screen()
    typewriter("As you continue onwards, you near a village", speed)
    typewriter("But from afar, the guards saw you and start chasing you!",
               speed)
    pause()
    clear_screen()
    typewriter("You sprint away, but the guards are hot on your tail", speed)
    typewriter("As you look to your left, you see a goblin village", speed)
    typewriter("And as you look to your right, you see a CREEPY mansion", speed)
    typewriter("Do you go?", speed)
    typewriter("1: Left towards the goblin village", speed)
    typewriter("2: Right towards the creepy mansion", speed)
    charmed_goblins_option = choose_option(2)
    pause()

    if charmed_goblins_option == 1:
        clear_screen()
        typewriter("As you sprint towards the village", speed)
        typewriter("THE SCARY GOBLIN GIANT STARTS CHASING YOU!")
        typewriter(
            "you get sandwhiched between the two, and get eaten by the goblin giant",
            speed)
        typewriter("RIP")
    elif charmed_goblins_option == 2:
        clear_screen()
        typewriter(
            "You enter the scary mansion, your goblin friends following you",
            speed)
        scary_mansion()


def coin_small_men():
    global speed, player
    clear_screen()
    typewriter("That was lucky", speed)
    typewriter(
        "You see someone approaching from far away, but it looks like he got scared of you",
        speed)
    typewriter("Probably because the small men are so smelly", speed)
    typewriter("Well... you approach a village!")

    smelly_village()


def robbed_small_men():
    global speed, player
    clear_screen()
    typewriter("Can't believe you got robbed", speed)
    typewriter(
        "You see someone approaching from far away, but it looks like he got scared of you",
        speed)
    typewriter("Probably because the small men are so smelly", speed)
    typewriter("You realise you need help, cuz now you suck", speed)
    typewriter("You go to the village with a purpose, to find some allies!",
               speed)

    village_with_allies()


##TERIARAY FUNCTIONS
# POTENTIAL DRAGON FIGHT? CONT FROM SECONDARY oh my goodness


def village_no_allies():
    global speed, player
    global fancy_name
    clear_screen()
    typewriter("You enter the village, with the stranger besides you", speed)
    print(to_color(f"{player.name}: Who even are you? You got a name?", 'red'))
    time.sleep(2)
    print(
        to_color(
            "Stranger: Baron Maximilian Von Schnitzelworth, Keeper of the Velvet Cravat",
            'yellow'))
    time.sleep(2)
    print(to_color(f"{player.name}: Bless you", 'red'))
    time.sleep(2)
    print(
        to_color(
            f"{fancy_name}: I am well known around this village, for I have preserved peace for generations!",
            'yellow'))
    time.sleep(2)
    print(
        to_color(
            f"{player.name}: Well that's nice, now can we get some resources?",
            'red'))
    time.sleep(2)
    clear_screen()
    typewriter("You gained...")
    typewriter(
        "A monocle polishing kit? Because a cloudy monocle is simply unacceptable??",
        speed)
    typewriter(
        "A pocket sized emotional support ferret, in case you're feeling down",
        speed)
    typewriter("And a mystery key? It unlocks... something???", speed)
    pause()
    clear_screen()
    typewriter("You see some gnarly peasants approaching from a bit away",
               speed)
    typewriter("It looks like they're trying to rob you!", speed)
    time.sleep(1)
    print(
        to_color(
            f"{fancy_name}: NOO NOT THE EMOTIONAL SUPPORT FERRET!!! RUNNNNNN",
            'yellow'))
    typewriter("Do you...")
    typewriter("1: Run away, for the sake of the ferret", speed)
    typewriter("2: Fight the peasents, and defend the honor of said ferret",
               speed)

    run_or_fight_ferret = choose_option(2)

    if run_or_fight_ferret == 1:
        typewriter("You sprint in the opposite direction...", speed)

        run_for_ferret()
    elif run_or_fight_ferret == 2:
        typewriter("You turn around and stand strong, ready to fight!", speed)

        fight_bandits()


def village_with_allies():
    global speed, player
    clear_screen()
    typewriter("As you enter the village, everyone backs away from you", speed)
    typewriter("You stink...", speed)
    typewriter(ASCII_STINKY, speed)
    pause()
    typewriter("As you stumble around, you see an ultra handsome man", speed)
    typewriter("He takes one good look at you, and suddenly falls on one knee",
               speed)
    print(
        to_color(
            f"{player.name}: Who even are you? Why are you proposing to me???",
            'red'))
    time.sleep(2)
    print(
        to_color(
            "Stranger: Baron Maximilian Von Schnitzelworth is my name, and you are them most handsom, beautiful being i have ever seen!",
            'yellow'))
    time.sleep(2)
    print(
        to_color(
            f"{player.name}: Oh my goodness.... I did not expect that today ",
            'red'))
    time.sleep(2)
    pause()
    typewriter("do you....", speed)
    typewriter("1: Accept his proposal")
    typewriter("2: Deny it, and run away")
    choice_proposal = choose_option(2)

    if choice_proposal == 1:
        typewriter("Well I didn't see that coming...")
        typewriter("I geuss you gained an ally!", speed)
        proposal()

    elif choice_proposal == 2:
        typewriter("Your loss...", speed)
        rejection()


def smelly_village():
    global speed, player
    clear_screen()
    typewriter(
        "As you enter the village, you're so smelly everyone get's scared",
        speed)
    typewriter(
        "People are running left and right, trying to get away from you", speed)
    typewriter(ASCII_STINKY, 0.01)
    pause()
    clear_screen()
    typewriter(
        "You spend the whole day being chased, and eventually find a nice small area to hide..",
        speed)
    typewriter("But you have a foreboding feeling approaching")
    pause()
    typewriter("Someone approaches from far away", speed)
    typewriter("He's floating?? Seems like he smells something reaaaaaal good",
               speed)
    time.sleep(1)
    print(
        to_color(f"{player.name}: Who are you and what do you want from me?",
                 'red'))
    time.sleep(2)
    print(to_color("Stranger: Yo you smell good as hell dawg!", 'yellow'))
    time.sleep(2)
    print(to_color("Stranger: So good.... ima rob you MUAHAHAHA", 'yellow'))
    time.sleep(2)
    pause()
    clear_screen()
    typewriter("You get robbed and fail to survive in this miserable world")
    typewriter("What a sad way to go...")
    # END


def scary_mansion():
    global speed, player
    typewriter(
        "You enter a spoooooooooooooooooooooooooooooooooooky mansion...", speed)
    time.sleep(2)
    skib = random.randint(1, 9)
    skib += player.luck()

    if skib >= 11:
        print(ASCII_SKIBIDI_TOILET)
        typewriter("crazy lucky pull dawg")
        typewriter("heres ur reward buddy boy")
        typewriter("you gained a skibidi toilet")
        player.allocate_stats(15)
    else:
        print(ASCII_SPOOKY)

    time.sleep(0.3)
    clear_screen()
    typewriter(
        "You venture forwards... but you feel someone's gaze behind you")
    typewriter("You look back, but you only see your goblin friends")
    typewriter("Blissfully unaware of what is coming...")
    pause()
    clear_screen()
    typewriter("You walk up the stairs and enter the master bedroom", speed)
    typewriter(
        "The stairs break behind you, your goblin friends falling through! OH NOSE",
        speed)
    typewriter("You're all alone now... no more friends to hide behind", speed)
    typewriter(
        "I mean.. in front of? Wait does that work? I don't even know at this point I need a nap",
        speed)
    typewriter("Well you enter the spooky bedroom!", speed)
    pause()
    clear_screen()
    typewriter("A spoooooooky ghossstt aaappears iiin ffront offf yooou")
    print(
        to_color(
            f"{player.name}: Oh my goodness gracious, a Scary Spooky Ghost!!!!!",
            'red'))
    time.sleep(2)
    print(
        to_color(
            "Ghost: Yo Yo brother/sister/sibling O, wassup my zawg. How's life chillin' here?",
            'yellow'))
    time.sleep(2)
    print(
        to_color(f"{player.name}: Huh? You spooky as hell oh my goodness",
                 'red'))
    time.sleep(2)
    print(
        to_color(
            "Ghost: My bad dawg, didn't realize I was that spooky. Here's a little gift as a suprise",
            'yellow'))
    time.sleep(2)
    pause()
    clear_screen()
    typewriter("You gained.... enlightenment", speed)
    typewriter("Don't ask me what you're gonna do with that")
    enlightenment()


# QUATERNARY FUNCTIONS
# MUST ADD.................................


def run_for_ferret():
    global speed, player
    pause()
    clear_screen()
    typewriter(
        "You hold your pocket sized emotional support ferret near your heart, and sprint in the opposite direction",
        speed)
    typewriter(
        "As you run, you find a shady, creepy motel, and you enter it like the dumb individual you are",
        speed)
    print('\n\n')
    typewriter(
        "You enter the hotel, looking around and seeing a bunch of scary men",
        speed)
    typewriter("All of a sudden, they all get up and slowly approach you",
               speed)
    countdown_timer(3, 1)
    pause()
    clear_screen()
    typewriter("Then they burst out into song!")
    typewriter("Turns out you met the amazing and fabulous town band", speed)
    typewriter("You and your ferret stand in awe of their skill", speed)
    typewriter("But all of a sudden... they ask for a singing battle!", speed)
    if player.charm >= 7:
        typewriter("You awed them with your amazing singing skills...", speed)
        typewriter(
            "They ask you to join their band, and you just can't deny them",
            speed)
        typewriter(
            "You become a professional singer, and live your life with your emotional support ferret!",
            speed)
        typewriter("THE END")
    elif player.charm <= 6:
        typewriter(
            "You suck at singing, and they remove your existence priviliges")
        typewriter("What a sad way to go...")


def fight_bandits():
    global speed, player
    pause()
    clear_screen()

    enemy = character('Bandits', 10, 5, 2, 2, 10)

    bandit_fight = battle(player, enemy)
    if bandit_fight == True:
        typewriter("You won against the bandits! ", speed)
        typewriter("Here are some stats!")
        player.allocate_stats(5)
        typewriter(
            "You continue onwards with your journey, and start approaching the dragon!",
            speed)
        dragon_fight()
    else:
        typewriter("You lost and your soul left you for the spirit realm")
        typewriter("You kinda suck lol")


def proposal():
    global speed, player
    typewriter("Wow... what a romantic")
    pause()
    clear_screen()
    typewriter("You accept the weirdo's proposal and start dating", speed)
    typewriter("You learn more about him, and come to love him for who he is",
               speed)
    typewriter("You fall madly in love, and eventually decide to propose!",
               speed)
    print(ASCII_RING)
    typewriter("Wow congratulations on your proposal!", speed)
    typewriter("You guys get engaged, and live together", speed)
    typewriter("Eventually.... you guys get married!")
    print(ASCII_MARRY)
    typewriter("Wow congratulations!")
    typewriter(
        "You learn more about him, and you guys live to the ripe age of 68",
        0.03)
    print('\n')
    typewriter("The end! I'm so proud of you \u2764")


def rejection():
    global speed, player
    pause()
    clear_screen()
    typewriter("You reject the poor man, and he runs off with sadness", speed)
    typewriter("You ruined his day you horrible person " + "\U0001F620", speed)
    typewriter(
        "Well... now you're being chased by twenty bystanders who are mad at you",
        speed)
    typewriter("You know what time it is!!!", speed)
    # POTENTIALLY INSERT ACTUAL GAME WITH PYGMAE
    result_rejection_fight = button_mash_game(player.strength, player.luck)

    if result_rejection_fight == False:
        typewriter("wow... can't beleive you lost lol", speed)
        typewriter(
            "You got chased out of the village, and lived the rest of your life",
            speed)
        typewriter("In dismal sadness, regretting your decisions", speed)
        typewriter("What a sad way to go :(")
        typewriter("The end :(((((((((((((")

    elif result_rejection_fight == True:
        pause()
        clear_screen()
        typewriter("Wow congrats! You successfully escaped!", speed)
        typewriter("You skeddadle out of the village, and recuperate outside",
                   speed)
        typewriter("Your future is now uncertain, as you have", speed)
        print("NO FRIENDS")
        time.sleep(1)
        print("NO LIFE")
        time.sleep(1)
        print("AND NO FUTURE")
        time.sleep(1)
        # INSERT NEXT FUNCTION
    else:
        print("debug")


def enlightenment():
    global speed, player
    pause()
    clear_screen()
    typewriter("As you walk out of the mansion you feel enlightened", speed)
    typewriter("As if the very fabric of your existence has been changed",
               speed)
    typewriter("You now understand the true meaning of life", speed)
    typewriter("MONEY")
    print('\n')
    typewriter("You think to yourself,", speed)
    typewriter("Whats the best way to make money in this harsh economy???",
               speed)
    typewriter("You may....")
    typewriter(
        "1: Fight a dragon, and sell it's loot! Hope you invested in strength",
        speed)
    typewriter("2: Go back to the village and become a famous business man!",
               speed)
    choice_business = choose_option(2)

    if choice_business == 1:
        typewriter("Well... just know that it was your decision not mine")
        dragon_fight()
    elif choice_business == 2:
        typewriter("Smart decision!")
        if player.luck >= 7:
            typewriter(
                "You go back to the village and become a succesful business man!",
                speed)
            typewriter(
                "You invest heavily into botcoin, and made over 2 million dollars",
                speed)
            typewriter("You live out the rest of your life in luxury :)")
        else:
            typewriter("You go back to the village...", speed)
            typewriter("And decide to invest in bitcoin", 0.03)
            typewriter("But you invested when it was 103k", 0.03)
            typewriter(
                "You lose all your money, and regret every decision you've ever made",
                0.03)
    else:
        print("debug")


# FINAL FUnCTIONS
# WIN REJECTION FIGHT (no friends no life)


def dragon_fight():
    global speed, player
    pause()
    clear_screen()
    typewriter("You now begin to approach the dragon...", speed)
    typewriter("You see a big castle, but as you enter through the front door",
               speed)
    typewriter("A ROARING FLAME GOES RIGHT PAST YOUR HEAD!!", speed)
    print(ASCII_DRAGON)
    typewriter("ARE YOU READY FOR THIS FIGHT???", speed)
    typewriter("1: I'm too scared, I need to run!", speed)
    typewriter("2: LET'S FIGHT!!!!!")

    dragon_run = choose_option(2)

    if dragon_run == 1:
        print("Oh you little scaredy cat")
        time.sleep(1)
        typewriter("As you try to run... the dragon eats you in one big bite")
        typewriter("That was all your fault")
        typewriter("You deserved that")
    elif dragon_run == 2:
        typewriter("YES YOU BUFF LITTLE PERSON")
        typewriter("Hope you payed attention where you put your stats...")

        if player.charm >= 10:
            typewriter("You charming lil guy")
            typewriter("You charmed the dragon out of eating you!!!!")
            typewriter("You and the dragon are now besties forever <3")
        else:
            enemy = character("Dragon", 35, 3, 2, 2, 50)
            win_or_lose = battle(player, enemy)
            if win_or_lose == True:
                pause()
                clear_screen()
                typewriter(
                    "Yes! You've succeeded and brought peace to this land!")
                typewriter("Congratulations! I'm so proud of you")
                typewriter("You're like super cool and epic")
                typewriter(
                    "And your name will forever be passed down in history")
            elif win_or_lose == False:
                pause()
                clear_screen()
                typewriter("oooooof that must hurt")
                typewriter(
                    "You lost and your soul left to the spirit realm :(")


def rejection_fight():
    global speed, player
    pause()
    clear_screen()
    typewriter("As you stumble out of the village, you look left and right",
               speed)
    typewriter(
        "You see yourself, standing alone, regretting your life decisions",
        speed)
    typewriter("Do you... ")
    typewriter("1: Run to the forest, and live in sadness", speed)
    typewriter("2: Redeem yourself by fighting the dragon!", speed)
    choice_redeem = choose_option(2)
    if choice_redeem == 1:
        typewriter("You run to the forest, and live in sadness", speed)
        typewriter(
            "You never get to see your friends, and live as a hermit for the rest of your life",
            speed)
    elif choice_redeem == 2:
        typewriter("I'm proud of you :", speed)
        dragon_fight()


##########-GAME LOOP-##########
while True:
    clear_screen()
    game_explanation()

    restart = input("Do you want to play again? (Y/N): ")
    if restart.upper() != 'Y':
        sad_trombone()
        time.sleep(1)
        print("Thanks for playing! Goodbye!")
        break

