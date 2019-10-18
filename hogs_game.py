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



Project 1: The Game of Hog hog.zip
5-sided die

I know! I'll use my
Higher-order functions to
Order higher rolls.
Introduction
Important submission note: For full credit:

Submit with Phase 1 complete by Monday, September 9 (worth 1 pt).
Submit with Phases 2 and 3 complete by Thursday, September 12.
Although the checkpoint date is only a few days from the final due date, you should not put off completing Phase 1. We recommend starting and finishing Phase 1 as soon as possible to give yourself adequate time to complete Phases 2 and 3, which are can be more time consuming.

You do not have to wait until after the checkpoint date to start Phases 2 and 3.

Phase 1 is individual, Phases 2 and 3 can be completed with a partner.

You can get 1 extra credit point by submitting the entire project one day early on Wednesday, September 11.

In this project, you will develop a simulator and multiple strategies for the dice game Hog. You will need to use control statements and higher-order functions together, as described in Sections 1.2 through 1.6 of Composing Programs.

Rules
In Hog, two players alternate turns trying to be the first to end a turn with at least 100 total points. On each turn, the current player chooses some number of dice to roll, up to 10. That player's score for the turn is the sum of the dice outcomes.

rule_enabled_pig_out = True
#To spice up the game, we will play with some special rules:

while rule_enabled_pig_out:

#Pig Out. If any of the dice outcomes is a 1, the current player's score for the turn is 1.

#Example 1: The current player rolls 7 dice, 5 of which are 1's. They score 1 point for the turn.
#Example 2: The current player rolls 4 dice, all of which are 3's. Since Pig Out did not occur, they score 12 points for the turn.

rule_enabled_free_bacon = True

def get_current_player():
	return

def get_opponent_score(current_player):
	if current_player == player1:
		return get_player_score(player2)
	elif current_player == player2:
		return get_player_score(player1)
	else:
		return 'error'

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

rule_enabled_feral_hogs = True
while rule_enabled_feral_hogs:
	CURRENT_DICE_ROLLED = 0
	LAST_DICE_ROLLED = 0
	get_current_player()
	
	if abs(CURRENT_DICE_ROLLED - LAST_DICE_ROLLED) == 2:
		SCORE += 3

	statement = 'Feral Hogs! You rolled {LAST_DICE_ROLLED} die last round and   {CURRENT_DICE_ROLLED} this round... and since they are 2 apart you get a bonus 3 points!'

def multiply_score_value(player_score):
	if len(player_score) == 1:
		return 0
	else:
		return player_score[0] * player_score[1]
		
rule_enabled_swine_swap = True
while rule_enabled_swine_swap:
	if get_player_score(get_current_player())

player_cur_score = get_player_score(get_opponent)
opp_cur_score = get_player_score
	
	if multiply_score_value(player_cur_score\) == multiply_score_value(opp_cur_score):
		(a,b) = (player_cur_score, opp_cur_score)
		(opp_cur_score, player_cur_score) = (b, a)
		statement = 'Swine Swap! When all  the digits of your score are multiplied, they equal all the digits multiplied of your opponent! your scores have now been switched!.'
		

Example 1: At the end of a turn, the players have scores of 2 and 4. Since 2 * 2 != 4 * 4, the scores are not swapped.
Example 2: At the end of a turn, the players have scores of 22 and 4. Since 2 * 2 != 4 * 4, the scores are not swapped.
Example 3: At the end of a turn, the players have scores of 28 and 4. Since 2 * 8 == 4 * 4, the scores are swapped.
Example 4: At the end of a turn, the players have scores of 124 and 2. Since 1 * 4 == 2 * 2, the scores are swapped.
Example 5: At the end of a turn, the players have scores of 44 and 28. Since 4 * 4 == 2 * 8, the scores are swapped.
Example 6: At the end of a turn, the players have scores of 2 and 0. Since 2 * 2 != 0 * 0, the scores are not swapped.
Example 7: At the end of a turn, the players have scores of 10 and 0. Since 1 * 0 == 0 * 0, the scores are swapped.
Download starter																
								
																
def main():
	main_is_on = True
	while main_is_on:
		
		player_count = 0
		value_returned = enter_user_string('name')
	
		player_1 = HogPlayer(value_returned)
		print('Player 1 is called ' + player_1.get_player_name())
		
	
main()
