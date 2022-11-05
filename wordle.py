import random

word_list = []
word_file = open('5letterwords.txt')
for words in word_file:
  word_list.append(words.strip())

print("""This is the final test of ENGL1024 course. 
Player 1 and player 2 have to compete to guess a five letter hidden word for 3 times.
Each game, you have six attempts to guess the word.
For the guide shown, 
"G" indicates that the letter is in the word and in the correct spot. 
"Y" indicates that the letter is in the word but not in the correct spot. 
"X" indicates that the letter is not in the word.   
Player who guess more words correctly get an A in this course.
Player who guess less words correctly fail in this course.
If both players can't guess any words.Both of you fail this course. ><
Let's start the game.\n""")
a1 = 0
p1 = 0
p2 = 0
for i in range(0,3):
  w1 = random.choice(word_list)
  correct_word = list(w1)
  tem = correct_word.copy()
  attempt = 6
  is_correct = False
  guide = ['X', 'X', 'X', 'X', 'X']
  print('Game', i + 1)
  while attempt > 0 and not is_correct:
    if a1 % 2 == 0:
      v2 = str(input('Player 1, enter a 5-letter word: ')).lower()
    elif a1 % 2 == 1:
      v2 = str(input('Player 2, enter a 5-letter word: ')).lower()
    guess = list(v2)
    v3 = 0
    v4 = 1
    if len(v2) != 5 or v2 not in word_list:
      print('Invalid input.')
      if attempt == 1:
        print(f"you have {attempt} attempt left.")
      elif attempt > 1:
        print(f"you have {attempt} attempts left.")
    else:
      for i in range(0,5):
        if guess[i] == correct_word[i]:
          guide[i] = 'G'
          correct_word[i] = str(v3)
          guess[i] = str(v4)
      for j in range(0,5):
        if guess[j] in correct_word:
          guide[j] = 'Y'
        for k in range(0,5):
          if correct_word[k] == guess[j]:
            guess[j] = str(v4)
            correct_word[k] = str(v3)
            break
      correct_word = tem.copy()
      attempt -= 1
      a1 += 1
      print(guide)
      if guide != ['G', 'G', 'G', 'G', 'G']:
        if attempt == 1:
          print(f"you have {attempt} attempt left.")
        elif attempt > 1:
          print(f"you have {attempt} attempts left.")
      else:
        break
      guide = ['X', 'X', 'X', 'X', 'X']
  if guide == ['G', 'G', 'G', 'G', 'G']:
    is_correct = True
    if a1 % 2 == 0:
      a1 = 0
      print('Player 2 wins!!!\n')
      p2 += 1
    else:
      a1 = 1
      print('Player 1 wins!!!\n')
      p1 += 1
  else:
    print('NOOOOOO!!! Both of you cannot guess the word correctly.\n')
    if a1 % 2 == 0:
      a1 = 0
    else:
      a1 = 1

if p1 == 0 and p2 == 0:
  print('Both of you guess 0 word right. You guys fail this course.')
elif p1 > p2:
  print('Player 1 guess more words right. Player 1 get an A and player 2 fail this course.')
else:
  print('Player 2 guess more words right. Player 2 get an A and player 1 fail this course.')
