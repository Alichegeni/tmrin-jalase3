import random

score = 10
true_chars = []

words = ['book', 'tree', 'python', 'bag', 'umbrella', 'dog', 'clock', 'engineer', 'toothpaste', 'shirmoz']
word = random.choice(words)
word = word.lower()

while True:
    len_word = len(word)
    print("len_word=", len_word)
    for i in range(len(word)):

        if word[i] in true_chars:
            print(word[i], end='')
        else:
            print('-', end='')
    print("\n~~~~~~~~~~~~~~~~~~~~~")
    char = input("\nenter a character: ")
    char = char.lower()

    if char in word:
        true_chars.append(char)
    else:
        score -= 1

    print("score=",score)

    if len(true_chars) == len(word):
        print("oh you wins")
        break


    if score == 0:
        print("Game Over!")