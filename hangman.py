#hangman

import random

words = ["abruptly", "absurd", "abyss", "affix", "askew", "avenue", "awkward", "axiom", "azure", "bagpipes", "banjo", "bayou", "beekeeper", "blitz", "blizzard", "boggle", "boxcar", "boxful", "buffalo", "buffoon", "buzzard", "buzzing", "buzzwords", "caliph", "cobweb", "cockiness", "croquet", "crypt", "curacao", "cycle", "daiquiri", "dirndl", "disavow", "dizzying", "duplex", "dwarves", "embezzle", "equip", "espionage", "euouae", "exodus", "faking", "fishhook", "fixable", "fjord", "flapjack", "flopping", "fluffiness", "flyby", "foxglove", "frazzled", "frizzled", "fuchsia", "funny", "gabby", "galaxy", "galvanize", "gazebo", "giaour", "gizmo", "glowworm", "glyph", "gnarly", "gnostic", "gossip", "grogginess", "haiku", "haphazard", "hyphen", "iatrogenic", "icebox", "injury", "ivory", "ivy", "jackpot", "jaundice", "jawbreaker", "jaywalk", "jazziest", "jazzy", "jelly", "jigsaw", "jinx", "jiujitsu", "jockey", "jogging", "joking", "jovial", "joyful", "juicy", "jukebox", "jumbo", "kayak", "kazoo", "keyhole", "khaki", "kilobyte", "kiosk", "kitsch", "kiwifruit", "klutz", "knapsack", "larynx", "lengths", "lucky", "luxury", "lymph", "marquis", "matrix", "megahertz", "microwave", "mnemonic", "mystify", "naphtha", "nightclub", "nowadays", "numbskull", "nymph", "onyx", "oxidize", "oxygen", "pajama", "peekaboo", "phlegm", "pixel", "pizazz", "pneumonia", "polka", "pshaw", "psyche", "puppy", "puzzling", "quartz", "queue", "quips", "quixotic", "quiz", "quizzes", "quorum", "razzmatazz", "rhubarb", "rhythm", "rickshaw", "schnapps", "scratch", "shiv", "snazzy", "sphinx", "spritz", "squawk", "staff", "strength", "strengths", "stretch", "stronghold", "stymied", "subway", "swivel", "syndrome", "thriftless", "thumbscrew", "topaz", "transcript", "transgress", "transplant", "twelfth", "twelfths", "unknown", "unworthy", "unzip", "uptown", "vaporize", "vixen", "vodka", "voodoo", "vortex", "voyeurism", "walkway", "waltz", "wave", "wavy", "waxy", "wellspring", "wheezy", "whiskey", "whizzing", "whomever", "wimpy", "witchcraft", "wizard", "woozy", "wristwatch", "wyvern", "xylophone", "yachtsman", "yippee", "yoked", "youthful", "yummy", "zephyr", "zigzag", "zigzagging", "zilch", "zipper", "zodiac", "zombie"]

running = True

while running:
    randomWord = words[random.randint(0, len(words))]
    guessesMade = []
    correctGuesses = []

    initialState = ["_"*len(randomWord)]
    currentState = "".join(str(x) for x in initialState)

    incorrectGuesses = []

    hangmanFrame = 10

    play = input("Play hangman (yes/no)? ")
    play = play.lower()
    while play == "yes":
        print(currentState)
        while hangmanFrame != 0 and running == True:
            guess = input("Guess a letter or type quit to quit: ").lower()
            currentState = ""
            if guess == "quit":
                play = "no"
                running = False 
            elif guess in guessesMade:
                print("Invalid guess - Try again")
            else:
                if len(guess) != 1:
                    print("Invalid guess - Try again")
                if guess in randomWord:
                    correctGuesses.append(guess)
                    guessesMade.append(guess)
                   
                else:
                    incorrectGuesses.append(guess)
                    hangmanFrame -= 1
                    guessesMade.append(guess)
            
            for i in randomWord:
                if i in correctGuesses:
                    currentState += i

                else:
                    currentState += "_"
                
                if currentState == randomWord:
                        print("You win")
                else:
                        print("Keep going")
 
            print(guessesMade)
            print(currentState)
            print("You have", hangmanFrame, "guesses left")
        
        if hangmanFrame == 0:
            print("You lose")

        print(randomWord)
        play = "no"

    running = False