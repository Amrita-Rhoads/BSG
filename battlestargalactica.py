# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 19:59:26 2018

@author: Amrita

TODO: next few days - have all locations + at least one character + move 
"""
import random


class SkillCard:
    """
    A skill card in a game of Battlestar Galactica.

    Attributes:
        expansion - the expansion associated with this card.
        game - the game associated with this card.
        type - the type of skill card this is.
        value - the value in skill checks.
        text - the text printed on this card.
        action - the action associated with playing this card.
        skillcheck - the effect of playing this into a skill check.
        discard - the effect of discarding this card.
    """
    def __init__(self):
        pass
    

class CrisisCard:
    """
    A crisis card in a game of Battlestar Galactica.

    Attributes:
        expansion - the expansion associated with this card.
        game - the Game class instance associated with this card.
        type - the type of Crisis Card this is.
        text - the text printed on the card. 
    """


class DestinationCard:
    """
    A destination card in a game of Battlestar Galactica.
    
    Attributes:
        text - the text printed on the card.
        distance - the distance of the destination.
        cost - the cost of travelling that distance.
        effect - any additional effects to call.
    """


class Deck:
    """
    A deck containing cards. (Also has a discard pile.)

    Attributes:
        game - the game this pertains to.
        draw - the draw pile.
        discard - the discard pile.
    """


class Character:
    """
    A player in a game of Battlestar Galactica.

    Attributes:
        expansion - the expansion associated with this player.
        game - the Game instance associated with this player.
        class - what class this player falls into.
        name - the name of this player.
        draw - this player's draws.
        text - the text on this player's character sheet.
        location - the character's location.
        is_human - True if player is not a revealed Cylon.
    """
    def __init__():
        pass

    def move(self, location):
        """
        Move this character to a different location.
        
        Note that since this does not enforce discards, one must ensure that
        a player moving to a different ship discards one card.
        Parameters:
            location - Location to be moved to.
        Raises:
            InvalidMoveError - if Location is not valid.
        """
        if location.is_hazardous:
            raise InvalidMoveError("Cannot move to a hazardous location!")
        elif location.is_human != player.is_human:
            raise InvalidMoveError("Not accessible to your allegiance!")
        else:
            self.location = location

    def draw(self):
        pass

    def discard(self, cards):
        """
        Discard an arbitrary number of cards.
        """
        pass


class Location:
    """
    A location in Battlestar Galactica.

    Attributes:
        expansion - the expansion associated with this location.
        game - the Game instance associated with this location.
        ship - the ship this location is on.
        players - a list of players currently present there.
        action - the action that can be taken at that location.
        is_hazardous - whether a location can be moved to.
        is_damaged - whether this location is damaged.
        is_human - False if this location is accessible to revealed Cylons.
    """
    def __init__(self):
        self.expansion = "Base"
        self.ship = "Galactica"
        self.is_hazardous = False
        self.is_damaged = False
        self.players = []


class Board:
    """
    A board for Battlestar Galactica.

    Attributes:
        game - the game this belongs to.
        locations - the list of locations on this board.
        food - the amount of food remaining.
        fuel - the amount of fuel remaining.
        population - the amount of population remaining.
        morale - the amount of morale remaining.
    """


class Game:
    """
    A game of Battlestar Galactica.
    """
    

