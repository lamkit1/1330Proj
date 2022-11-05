import random

word_list = []
word_file = open('5letterwords.txt')
for words in word_file:
  word_list.append(words.strip())

correct_word = random.choice(word_list)

print("""This is the final test of CAES1234 course 
You have to guess a five letter hidden word for 3 times
Each time,you have six chances to guess this word
For the guide shown 
"G" Indicates that the letter is in the word and in the correct spot 
"Y" indicates that the letter is in the word but not in the correct spot 
"X" indicates that the letter is not in the word   
If you can guess it correctly within 6 attempts for 3 times.You get an A in this course.For 2 times,You get a B.for 1 time, you get a D.Otherwise,you fail this course.""")

count = 0
for i in range(0,3):
  attempt = 6
  is_correct = False
  guide = ''
  print(i+1,'time(s)')
  while attempt > 0 and not is_correct:
    guess = str(input('Enter a 5-letter word: ')).lower()
    if len(guess) != 5:
      print('Invalid input.')
    else:
      for j in range(0,5):
        if guess[j] == correct_word[j]:
          guide += 'G'
        elif guess[j] in correct_word:
          guide += 'Y'
        else:
          guide += 'X'
    print(guide)
    attempt -= 1
    if guide != 'GGGGG':
      print(f"you have {attempt} attempt(s) left.")
    if guide == 'GGGGG':
      break
    guide = ''
  if guide == 'GGGGG':
    is_correct = True
    count += 1
    print('You guess the word correctly.')
  else:
    print('You guess the word wrongly.')

if count == 0:
  print('You guess',count,'word(s) right.You fail this course.')
elif count == 1:
  print('You guess',count,'word(s) right.You get a D in this course.')
elif count == 2:
  print('You guess',count,'word(s) right.You get a B in this course.')
elif count == 3:
  print('You guess',count,'word(s) right.You get an A in this course.')
