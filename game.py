# -*- coding: UTF-8 -*-
'''
update histoty
--3.22:
Yeah! The fisrt beta version is published!
--3.23:
1.add customize mode
2.add op mode
3.adjust the value of easy mode and impossible mode in order
to make the game more reasonable and defiant.
4.fix a bug which may make year input goes wrong
5.fix some descriptions' problems
6.fix some bugs which will make some value goes wrong.
--3.24:
1.remove op mode
2.add some easter eggs
3.simplize the code
--3.25
1.fix some stupid bugs
2.when player chooce to quit or suicide, they will be ask again to make sure
--3.26
1.simplize the code
2.now health will decrease 2 per month
--3.27
1.now the date and month will be counted correctly
2.a new warning for player when they have low food and health
3.a easter egg for Meriwether Lewis was add
--3.28
1.now the health will decrease randomly per month
2.bug fix: when player run out of food or health, a negative value will be showed.
Now when player run out of food or health, there be no warning for food and health.
Player will receive gameover hint immediately
3.now player will meet a random event that occurs randomly once a month
4.better loading (just for fun)
5.fix a bug that the random days of accident are not counted into total days correctly

future plan:
1.simplize the code
2.the players can choose the month and the date which they want to start
3.two known bugs fixing
(because of some reasons, i cannot tell you here)
4.add background picture
5.add background music
6.improve the playing feeling
7.more hints for players
8.game can be played again after game over
9.the balance of value for each mode
10.more amazing modes will be added soon
11.tell a story?
12.more easter eggs
13.multiplayer mode
14.a shop for buging things?
15.email the data of game to author after player finish the game
This will help me to do the balance of value.
16.a function to check leap year will be added soon
17.chinese virson support?
'''

#import
import random
import time
import smtplib #send email import

#welcom player
print('Welcome to the game Oregon Trail ')

#asking name
player_name = input('What is your name:')

#easter eggs for name
if player_name == 'Meriwether Lewis':
  year_set = 1803
  mode_choice = 'impossible'
else:
  year_set = int(input('Enter a year whatever you like:'))
  print('Which mode do you want to play?')
  mode_choice = input('(easy,normal,hard,impossible,customize):')

#leap year function
'''
if (year_set % 4) == 0:
   if (year_set % 100) == 0:
       if (year_set % 400) == 0:
           print('leap year')
       else:
           print('no leap year')
   else:
       print('leap year')
else:
   print('no leap year')
'''

#easy mode:
if mode_choice == 'easy':
  food_num = 1000
  health_num = 10
#noraml mode:
if mode_choice == 'normal':
  food_num = 500
  health_num = 5
#hard mode:
if mode_choice == 'hard':
  food_num = 300
  health_num = 4
#impossible mode:
if mode_choice == 'impossible':
  food_num = 150
  health_num = 3
#customize mode:
if mode_choice == 'customize':
  food_num = int(input('How much food do you want:'))
  health_num = int(input('How much health do you want:'))

#other basic strating value setting
player_move_distance = 0
month_num = 3
days_pass = 1
total_days = 0
MONTHS_WITH_31_DAYS = [1, 3, 5, 7, 8, 10, 12]
random_result = 0
health_d1 = random.randint(1, 31)
health_d2 = random.randint(1, 31)
acident_appear = random.randint(1, 30)
travel_total_num = 0
rest_total_num = 0
hunt_total_num = 0
status_total_num = 0

#add days:
def add_days(min, max):
  global days_pass
  global month_num
  global MONTHS_WITH_31_DAYS
  global random_result
  global food_num
  global health_num
  global health_d1
  global health_d2
  global total_days
  global acident_appear

  random_result = random.randint(min, max)
  print('Now',random_result,"days passed..")
  days_pass_min = days_pass
  check_big = days_pass + random_result

  #acident
  if acident_appear >= days_pass and acident_appear <= check_big:
    a_number = random.randint(1, 3)
    a_health_num = random.randint(1, 2)
    if a_number == 1:
      print('During this time, you crossed a river.')
    if a_number == 2:
      print('During this time, you had a dysentery.')
    if a_number == 3:
      print('During this time, you saw a beautiful girl and had a good time with her.')
    random_result2_food = random.randint(1, 10)
    random_result2_day = random.randint(1, 10)
    print('As a result, you eat '+str(random_result2_food)+' lbs extra food.')
    print('It also took up eatra '+str(random_result2_day)+' days.')
    if a_health_num == 1:
      print('And you also lose 1 health')
      health_num -= 1
    food_num = food_num - random_result2_food - random_result2_day*5
    days_pass += random_result2_day
    total_days += random_result2_day
  #health decrease randomly  
  check_big = days_pass + random_result
  if health_d1 >= days_pass_min and health_d1 <= check_big:
    health_num -= 1
    print('Unfortunately, you lose 1 health during this time.')
  if health_d2 >= days_pass_min and health_d2 <= check_big:
    health_num -= 1
    print('Unfortunately, you lose 1 health during this time.')


  days_pass += random_result
  total_days += random_result
  food_num -= random_result * 5

  if days_pass >= 30:
    if month_num not in MONTHS_WITH_31_DAYS:
      if days_pass > 30:
        days_pass -= 30
        month_num += 1
        health_d1 = random.randint(1, 30)
        health_d2 = random.randint(1, 30)
        acident_appear == random.randint(1, 30)
    else:
      if days_pass > 31:
        days_pass -= 31
        month_num += 1
        health_d1 = random.randint(1, 30)
        health_d2 = random.randint(1, 30)
        acident_appear == random.randint(1, 30)

#function part
def travle1(movedistance):
  global days_pass
  global travel_total_num
  add_days(3,7)
  movedistance = movedistance + random.randint(30, 60)
  travel_total_num += 1
  return movedistance

def rest(health):
  global days_pass
  global rest_total_num
  add_days(2,5)
  health = health + 1
  rest_total_num += 1
  return health

def hunt(hunting_food):
  global days_pass
  global hunt_total_num
  add_days(2,5)
  hunting_food = hunting_food + 100
  print('Gain: 100 lbs food')
  hunt_total_num += 1
  return hunting_food


#loading part
print('--------------------------------------')
print('Now Loding...')
time.sleep(0.5)
print('Now loading the player setting...')
time.sleep(2)
print('Successfully!')
time.sleep(0.5)
print('Now loading the game setting...')
time.sleep(2)
print('Successfully!')
time.sleep(0.5)
print('Prepearing the trip for Oregon...')
time.sleep(2)
print('Successfully!')
time.sleep(0.5)
print('Now game is ready!')
print('--------------------------------------')
print('Attention:')
print('We will be recreating Oregon Trail! The goal is to travel from NYC to')
print('Oregon (2000 miles) by Dec 31st. However, the trail is arduous. Each')
print('day costs you food and health. You can huntand rest, but you have to')
print('get there before winter. GOOD LUCK!')
print('--------------------------------------')

#main
while player_move_distance < 2000 and food_num > 0 and health_num > 0 and month_num < 13:
  if food_num <= 50:
    print('Warning! You only have '+ str(food_num) + " lbs food now.")
    print('You need hunt now.')
  if health_num <= 2:
    print('Warning! You only have '+ str(health_num) + " health now.")
    print('You need a rest.')
  print(str(player_name) + ', now is '+str(month_num)+'/'+str(days_pass)+'/'+str(year_set)+", and you have travled " + str(player_move_distance) + " miles.")
  choice = input('Your choice:')
  if choice == 'travel':
    player_move_distance = travle1(player_move_distance)
  if choice == 'rest':
    if health_num < 5:
      print("You get 1 heath!")
      health_num = rest(health_num)
    if health_num >= 5:
      print("Your health is full, the maximum number for health is 5!")
  if choice == 'hunt':
    food_num = hunt(food_num)
  if choice == 'status':
    print('-Dear ' + str(player_name) + ', now is '+str(month_num)+'/'+str(days_pass)+'/'+str(year_set)+".")
    print('-Food:',food_num,"lbs")
    print('-Health:',health_num)
    print('-Distance traveled:',player_move_distance)
    distance_left = 2000 - player_move_distance
    print('-'+str(total_days) +' days have passed.')
    print('-You have travled ' + str(player_move_distance) + " miles, there is still " + str(distance_left) + ' miles left.')
    status_total_num += 1
  if choice == 'help':
    print('[travel]: moves you randomly between 30-60 miles and takes 3-7 days (random).')
    print('[rest]: increases health 1 level (up to 5 maximum) and takes 2-5 days (random).')
    print('[hunt]: adds 100 lbs of food and takes 2-5 days (random).')
    print('[status]: lists food, health, distance traveled, and day.')
    print('[quit]: will end the game.')
  if choice == 'quit':
    quit_choice = input('Are you sure that you want to quit?(y/n)')
    if quit_choice == 'y':
      print('Game over...I cannot believe that you quit...')
      break
  if choice == 'suicide':
    quit_choice2 = input('Are you sure?(y/n)')
    if quit_choice2 == 'y':
      print('Game over...You kill youslf...')
      break
  if choice == 'easter egg':
    print("　　　　　　　　　　　　　＿＿＿ r -v ､ _＿＿＿")
    print("　　　　　　　　- ﾆ 二_ ` ､_::: -‐`…‐'´- _::::::::::::::7")
    print("　　　　　　　　__ 　-―` 　　　　　　　　　　｀ヽ:::/")
    print("　　　 　 　,. ´　　,. 　´　　　　　　　　　　　　 　＼")
    print("　　 　 ／　 __ ／　　　　　/　 /　　　　　　　　ヽ　ヽ.")
    print("　　　/'´￣ ／'　　 /　　 /　 / / ∧　 |　　　　　∨ ﾊ")
    print("　　　　　　//　 　/　 　/　 ｲ　'　| 　!　ﾄ　＼　　　∨ l")
    print("　 　 　　 /ｲ 　　,′　ｨ ⌒　|　|　| 　!　l　⌒ ヽ 　|　V")
    print("　　　　 〃 |　　│ 　 |　/ 　|　|　| 　 V 　　＼|　 |　　',")
    print("　 　 　 l! 　ﾚ　　|　　 |/_＿　V 　 　 　　 _ ＿|,_　ﾄ､ 　 ,")
    print("　　　　　　 |　　 |　　/ヾi ￣`r　 　　 　彳´￣ﾊ　ﾚ ヽ　l")
    print("　　　　　　 |　/|∧ ∧ 　VU`l 　 　　 　 l'ひV　!│ l　ヽ!")
    print("　　　　　　 ﾚ'　l　 !　ﾊ 　ゝ- ' / / / // ｀　´ ∧.ﾚ′")
    print("　　　　　　　　　　 V　ゝ　　　　 　 　　 　　 ノ ´ﾚ′")
    print("　　　　　　　 　　　　 　 　＞ .. _　 ´　_ .. ィ")
    print("　 　　 　 　 　　　 　　 　　_|ノ^､l ￣ l∧　|")
    print("　　　　 　 　　 　 　ィ´　丁| i ヽヽ_ _// ﾊ￣/ ヽ")
    print("　　　 　　 　　 　 /│　　V| i　 ゝ--く / ハ′ ハ")
    print("　　　　　　　　 　l　 ヽ　　|　ゝハ:::::::ハ │|　/　 |")
    print('verson:1.12')
    print('author: Yudong Lin')
    print('Good at: Game world view disign and value balance for the game')
    print('Have three-year-experience on developing and maintaining minecraft server')
    print('Technical nerd change the world!')
    print('Any bug reports please email:yoshino1347716570@gmail.com')
    print('Thanks for playing!')
  print('--------------------------------------')
#succeed!
if player_move_distance >= 2000:
  print('Nice job! you have arrived in Oregon')

#game over
if food_num <= 0:
  print('Game over, you have no food now.')

if health_num <= 0:
  print('Game over, you have no health now.')

if month_num >= 13:
  print('Game over, you run out of time!')
  
print('During the whole game, you:')
print('Travel ' + str(travel_total_num) +' times.')
print('Rest ' + str(rest_total_num) +' times.')
print('Hunt ' + str(hunt_total_num) +' times.')
print('Status ' + str(status_total_num) +' times.')

#restart
#restart_choice = input('Do you want to restart the game?')
      