#
# heuristic.py
#
# This Python script file provides two functions in support of minimax search
# using the expected value of game states. First, the file provides the
# function "expected_value_over_delays". This function takes as an argument
# a state of game play in which the current player has just selected an
# action. The function calculates the expected value of the state over all
# possible random results determining the amount of time before the
# Guardian changes gaze direction. This function calculates this value
# regardless of whose turn it is. The value of game states that result from
# different random outcomes is determined by calling "value". Second, the
# file provides a heuristic evaluation function for non-terminal game states.
# The heuristic value returned is between "max_payoff" (best for the
# computer player) and negative one times that value (best for the opponent).
# The heuristic function may be applied to any state of play. It uses
# features of the game state to predict the game payoff without performing
# any look-ahead search.
#
# This content is protected and may not be shared, uploaded, or distributed.
#
# PLACE ANY COMMENTS, INCLUDING ACKNOWLEDGMENTS, HERE
#
# Simple Game
# 1D Board Game
# -13 ... -2 -1 0 1 2 ... 13
# |C | ...| |  |G| | |...|H|
# West->             <- East
# Goal is try to reach 0 asap, the guardian spot
# Computer player starts at West, -13
# Human player starts at East, 13
# Code is run as Computer player
# Code is asking us to play as Human Player
# its a stociastic game, some uncertainly
# when guardian is looking in 1 direction, guardian has some x time until it turns to look in other direction
# how decide time step is based on flipping a coin
# flip a coin 3 times
# Head 1 Tail 0
# Repeats 3 times and adds 2 to that result
# therfore it can be anywhere between 2-5, 2 worst case, 5 best case
# in time step, human should chose how many steps i should take
# based on luck,chance, if chose # > than time step, then they will get caught
# game terminates in 2 conditions
# if someone wins or if someone gets caught
# can decide the range is from 1 - 4
# if chose 1, only move 1 step forward, safest decision
# 4 b.c should always be 1 less than max guardian time step
# minimax always looking ahead
# trys to find path which is maximum the ultity for itself and miniumum the ulutity for opponent
# 2ply = looks ahead 2 plays
# computer player can only look ahead 2 plays
# need to add heustric to estimate ultity
# not necessary to look in depth in game.py
# some attributes that are good to know about
# have location, current turn, action, time steps before guardian turns
# minimax is already done
# in minimax function value, expectedvalueaftermove
# probablyoftime returns probablyity of each time step
# good heurstic function who can estimate this ultity
# heurstic function for player, want lower the better
# heurstic function for computer, want higher the better
# could use this expression from slides to give us the emaximum expected ultility
# have done iterating over actions
# how to see what actions has best ultity max
# already know action
# just need to iterate over delays
# then * probablity delay and othe rthings
# then add them up together
#
# Denylson Fuentes on helping me understand what the equation from the slides meant and I overheard his conversation with the TA and how to get the probability
# the TA helped me understand how to get the expected value
#
#
#

# PLACE YOUR NAME AND THE DATE HERE
# Jim Nguyen 11/03/2021


from parameters import *
from minimax import probability_of_time
from minimax import value


def expected_value_over_delays(state, ply):
    """Calculate the expected utility over all possible randomly selected
    Guardian delay times, ranging from 2 to 5 steps. Return this expected
    utility value."""
    val = 0.0
    tmpVal = 0.0

    # PLACE YOUR CODE HERE
    # Note that the value of "ply" must be passed along, without
    # modification, to any function calls that calculate the value
    # of a state.
    # pretty simple
    # just follow the equation given on slides
    # given probably of time and actions

    # EU(A,S) = SUM(Probablity(Result(A,S) Given a State And Doing the action(A)) * Utility(Result(A,S)))
    # Taken from lecture 19 slide 26
    # have action, iterate over possible delays
    # for this action, see what delay for 2,3,4,5 and see what utility we can get.

    # called during in actions
    # minimax iterates over all possible states
    # needs 1 extra info
    # needs utility

    for delay in range(2, 5+1):
        state.time_remaining = delay
        val += probability_of_time(delay) * value(state, ply)

    # THIS IS DONE!!!!!

    # we already have actions
    # want to find the sum of all the probabilities given the delay times
    # before sum need to multiply the probabytime * value of something

    #val = max(tmpval)

    #Probalbity(Result() | S ^ Do(A))

    return val


def heuristic_value(state):
    """Return an estimate of the expected payoff for the given state of
    game play without performing any look-ahead search. This value must
    be between the maximum payoff value and the additive inverse of the
    maximum payoff."""
    val = 0.0
    tmpVal = 0.0

    tmpVal = abs(state.w)
    # up to us what heuristic function to make
    # use location and distance stuff to help find it
    # consider board size as well.
    # PLACE YOUR CODE HERE

    return val
