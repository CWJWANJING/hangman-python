import random
import pdb
# |------------
# |        |
# |        |
# |      //O\\
# |       /|\/
# |      / |
# |       / \
# |      /   \
# |
# |------------

# 上支架，中支架, 下支架, 吊绳，脑袋，头发，左手，右手，身体，左腿，右腿 11


def choose_word():
    with open("1-1000.txt") as wordsf:
        words = wordsf.readlines()
        return random.choice(words)


def user_guessed_word(guess, word):
    if guess == word:
        return True
    return False


def win():
    print("(^o^)~≪☆*CONGRATULATIONS*☆≫~(^o^)／ You Win! ")


def lose(word):
    print("Sorry, game over ¯\\_(ツ)_/¯.")
    print(f"The word is: {word}")


def load_stages(fname):
    # create a dict of num mistakes to thing to print
    mistakes_dict = {}
    with open(fname, 'r') as stages:
        for i in range(1, 12):
            # read 10 lines from file
            mistakes_dict[i] = "".join([next(stages) for _ in range(10)])
    return mistakes_dict


def draw(mistakes, mistakes_dict):
    print(mistakes_dict[mistakes])


if __name__ == "__main__":
    mistakes_dict = load_stages("hanging_stages.txt")
    # number of mistakes
    mistakes = 0
    # number of guessed letters
    corrects = 0
    # generate a random English word, present the number of letters
    # strip the "\n"
    guessword = choose_word().rstrip()
    print(f"This word has {len(guessword)} letters.\nYou have 11 chances.")
    display = []
    for i in range(len(guessword)):
        display.append("_ ")
    print(" ".join(display))
    charOrdering = list(guessword)
    # count the numbers of correct letters
    count = 0
    # record the letters that have been guessed
    guessed = []
    # pdb.set_trace()
    while True:
        # when the chances are used up
        if mistakes == 11:
            lose(guessword)
            break
        # take input letter
        inp = input()
        # check input size, can only allow 1 letter or the exact word
        if user_guessed_word(inp, guessword):
            win()
            break
        elif len(inp) == 1:
            if inp in guessed:
                print("You have guessed this letter before!")
            elif inp in guessword:
                # display the letters
                indexes = [i for i, x in enumerate(charOrdering) if x == inp]
                for i in indexes:
                    display[i] = inp
                print(" ".join(display))
                count += len(indexes)
                guessed.append(inp)
                if count == len(guessword):
                    win()
                    break
            else:
                guessed.append(inp)
                mistakes += 1
                draw(mistakes, mistakes_dict)
        elif len(inp) == 0:
            print("Please guess a letter.")
        else:
            print("Please enter either one letter or guess a word!")
