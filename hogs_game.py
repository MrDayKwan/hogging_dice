import re


class HogPlayer:		
	def __init__ (self, player_name_spawn):
		self.player_score = 0
		self.player_number = 0
		self.player_name = player_name_spawn
		print (f'Player {self.player_number} has entered the game.')

	def get_player_number(self):
		return self.player_number

	def get_player_name(self):
		return self.player_name
	
	def get_player_score(self):
		return self.player_score

	def set_player_name(self):
		assigned_name = enter_user_string('name')
		self.player_name = assigned_name

	def set_player_number(self):
		self.player_number += 1
		
import re

def enter_user_string(inputValue):
	inputStatement = f'Enter your {inputValue}'
	(inputPattern, errorCode) = ('^[A-Z][a-z]*$', 'a capitalized string of text')
	validated_user_unsubmitted= True
	while validated_user_unsubmitted:
		userInput = input(f'\n{inputStatement}:')	
		if userInput == '':
			print ('No value entered.')
		elif re.search(inputPattern, userInput):		
			print (f'Your {inputValue} must be {errorCode}.')
		else:
			validated_user_unsubmitted = False
		print (f'\nYou entered {userInput}. Thank you.\n\n')
		return userInput

def get_current_player():
	return

def get_opponent_score(current_player):
	if current_player == player1:
		return get_player_score(player2)
	elif current_player == player2:
		return get_player_score(player1)
	else:
		return 'error'
		
dice_size = 5

# I know! I'll use my Higher-order functions to Order higher rolls.
#need to use control statements and higher-order functions together

rule_enabled_pig_out = False
#To spice up the game, we will play with some special rules:

while rule_enabled_pig_out:
    PigOutOccur = False
	for dice in number_of_dice_rolled:
        if dice == 1:
    		PigOutOccur = True
    if PigOutOccur:
    	current_turn_score = 1
    statement = 'Pig Out! You rolled a 1, and now your score for this turn is 1!'

rule_enabled_free_bacon = False



while rule_enabled_free_bacon:
	if NUMBER_OF_DICE == 0:
		opponent_score = get_oppenent_score (get_current_player())				
		if len(opponent_score) = 1:
			free_bacon_subtraction = 0
		elif len(opponent_score) = 2:
			if opponent_score[0] >= opponent_score[1]:
				free_bacon_subtraction = opponent_score[1]
			elif opponent_score[1] > opponent_score[0]:
				free_bacon_subtraction = opponent_score[0]
			else:
				free_bacon_subtraction = 0
		free_bacon_score = 10 - free_bacon_subtraction
		statement = 'Free Bacon! {current_player} chose to roll zero dice. They score {free_bacon_score} points!'
	return statement
	return free_bacon_score

rule_enabled_feral_hogs = False
while rule_enabled_feral_hogs:
	CURRENT_DICE_ROLLED = 0
	LAST_DICE_ROLLED = 0
	get_current_player()
	
	if abs(CURRENT_DICE_ROLLED - LAST_DICE_ROLLED) == 2:
		SCORE += 3

	statement = 'Feral Hogs! You rolled {LAST_DICE_ROLLED} die last round and   {CURRENT_DICE_ROLLED} this round... and since they are 2 apart you get a bonus 3 points!'

def multiply_score_value(player_score):
	if len(player_score) == 1:
		multiplied_value = player_score*player_score
	else:
		multiplied_value = 1
		for digit in player_score:
			multiplied_value *= player_score[digit]
	return multiplied_value
	
		
rule_enabled_swine_swap = False
while rule_enabled_swine_swap:
	if get_player_score(get_current_player())

player_cur_score = get_player_score(get_opponent)
opp_cur_score = get_player_score
	
	if multiply_score_value(player_cur_score\) == multiply_score_value(opp_cur_score):
		(a,b) = (player_cur_score, opp_cur_score)
		(opp_cur_score, player_cur_score) = (b, a)
		statement = 'Swine Swap! When all  the digits of your score are multiplied, they equal all the digits multiplied of your opponent. Your scores have now been switched!'													
								
																
def main():
	main_is_on = True
	while main_is_on:
		
		player_count = 0
		value_returned = enter_user_string('name')
	
		player_1 = HogPlayer(value_returned)
		print('Player 1 is called ' + player_1.get_player_name())
		
	
main()
