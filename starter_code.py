#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random
import sys
moves = ['rock', 'paper', 'scissors']
rival = ['repeat', 'random', 'reflect', 'cycle']

"""The Player class is the parent class for all of the Players
in this game"""

# parent class


class Player:
    # to save the move of a player for reflect player subclass
    player1_move = ""
    player2_move = ""
    flag = 0  # a variable for reflect aand cycle subclasses for its first call

    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass

# repeat subclass: always return rock as a move


class RepeatPlyer(Player):
    def move(self):
        return 'rock'

# random subclass: returns a random move


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

# human subclass: returns a move a human choice


class HumanPlayer(Player):
    def move(self):
        # take the human choice
        choice = input("\nWhat would you like to throw? ")
        choice = choice.lower()
        while choice not in moves:
            if choice == "z":
                sys.exit()
            choice = input("rock, paper, or scissors? ")
        return choice

# reflect subclass: returns the previos move of the other player


class ReflectPlayer(Player):
    def learn(self, my_move, their_move):
        self.player1_move = their_move
        self.player2_move = my_move

    def move(self):
        # if its the first call
        if self.flag == 0:
            self.flag += 1  # then increment the flag variable
            return 'paper'
        return self.player1_move

# cycle subclass: returns a move in a periodic way


class CyclePlayer(Player):
    def move(self):
        if self.flag % 3 == 0:
            self.flag += 1
            return 'rock'
        elif self.flag % 3 == 1:
            self.flag += 1
            return 'paper'
        else:
            self.flag += 1
            return 'scissors'

# returns the winner


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

# game class


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1  # initialize first player object
        self.p2 = p2  # initialize second player object
        self.score1 = 0  # first player score
        self.score2 = 0  # second player score

    # define the winner in each round and store score of each player
    def score(self, move1, move2):
        if beats(move1, move2):
            self.score1 += 1
            print("You won!")
        elif beats(move2, move1):
            self.score2 += 1
            print("Computer won!")
        else:
            self.score1 += 1
            self.score2 += 1
            print("It's a tie!")
        print("      score      ")
        print(" You    |     Computer")
        print(f"  {self.score1}     |\t  {self.score2}")

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You threw {move1}, computer threw {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        self.score(move1, move2)

    def play_game(self):
        print("\nGame start!")
        for round in range(1, 11):  # 10 rounds in each game
            print(f"\nRound {round}:")
            self.play_round()
        print("\n   final score      ")
        print(" You    |     Computer")
        print(f"  {self.score1}     |\t  {self.score2}\n")
        if self.score1 > self.score2:
            print("You win")
        elif self.score1 < self.score2:
            print("Computer wins")
        else:
            print("It's a tie!")
        print("\nGame over!")


if __name__ == '__main__':
    print("Here are the rules of the game:,"
          "scissor cuts paper,paper covers rock, and rock crushes scissors.\n"
          "Play either rock, paper, or scissors. "
          "If you want to stop playing, enter a z.\n"
          "Each game has 10 rounds")

    play = input('\nWho would you like to play with? '
                 'Please enter "random", "reflect",'
                 '"repeat", or "cycle"\n')
    while play != "z":
        while play not in rival:
            play = input('Please enter "random",'
                         '"reflect", "repeat", or "cycle"\n')
            if play == "z":
                sys.exit()

        if play == "random":
            p2 = RandomPlayer()
        elif play == "reflect":
            p2 = ReflectPlayer()
        elif play == "repeat":
            p2 = RepeatPlyer()
        else:
            p2 = CyclePlayer()

        game = Game(HumanPlayer(), p2)
        game.play_game()
        play = input('\nWho would you like to play with?, '
                     'Please enter "random",'
                     '"reflect", "repeat", or "cycle"\n')
