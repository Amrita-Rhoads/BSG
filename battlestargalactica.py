# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 19:59:26 2018

@author: Amrita

TODO: next few days - have all locations + at least one character + move
"""
import random
import numpy as np


### Generally useful functions.
def read_message(filepath):
    """
    Opens and returns a text file as a string.
    """
    message = open(filepath, 'r').read()
    return message


### Exceptions:
class InvalidMoveError(Exception):
    pass


### Cards.
class Card:
    """
    A card in a game of Battlestar Galactica.

    Attributes:
        expansion - the expansion associated with this card.
        game - the game associated with this card.
        deck - the deck associated with this card.
        text - the text printed on the card.
    """
    def __init__(self):
        self.expansion = "Base"


class SkillCard(Card):
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


class CrisisCard(Card):
    """
    A crisis card in a game of Battlestar Galactica.

    Attributes:
        expansion - the expansion associated with this card.
        game - the Game class instance associated with this card.
        type - the type of Crisis Card this is.
        text - the text printed on the card.
    """


class DestinationCard(Card):
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


### Player stuff.
class Player:
    """
    A player in a game of Battlestar Galactica.

    Attributes:
        game - the game this player is in.
        user_id - the id associated with the Telegram user.
        name - the name associated with this player.
        character - the character this player is playing.
    """
    def __init__(self, game, user_id, name):
        self.game = game
        self.user_id = user_id
        self.name = name
        self.character = None


### Character stuff.
class Character:
    """
    A character in a game of Battlestar Galactica.

    Attributes:
        expansion - the expansion associated with this character.
        game - the Game instance associated with this character.
        player - the player associated with this character.
        group - what class this character falls into.
        name - the name of this character.
        draw - this character's draws.
        text - the text on this character sheet.
        location - the character's location.
        is_human - True if character is not a revealed Cylon.
        miracle_tokens - The number of miracle tokens remaining.
    """
    def __init__(self, game, player):
        self.expansion = "Base"
        self.game = game
        self.player = player
        self.group = None
        self.name = "Character McCharacterface"
        self.draw = np.zeros((5, 5))
        self.text = "This page intentionally left blank."
        self.location = None
        self.is_human = True
        self.miracle_tokens = 1

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


### Locations.
class Location:
    """
    A location in Battlestar Galactica.

    Attributes:
        expansion - the expansion associated with this location.
        game - the Game instance associated with this location.
        ship - the ship this location is on.
        name - the name of this location.
        text - the text on this location card.
        players - a list of players currently present there.
        action - the action that can be taken at that location.
        is_hazardous - whether a location can be moved to.
        is_damaged - whether this location is damaged.
        is_human - False if this location is accessible to revealed Cylons.
    """
    def __init__(self, game):
        self.expansion = "Base"
        self.game = game
        self.ship = "Galactica"
        self.name = "Location McLocationface"
        self.text = "Blank location."
        self.players = []
        self.action = None
        self.is_hazardous = False
        self.is_damaged = False
        self.is_human = True

    def __str__(self):
        to_ret = self.name
        if self.is_damaged:
            to_ret += " (Damaged)"
        to_ret += ":"
        to_ret += self.text
        if self.players:
            to_ret += "\n Players present: "
            to_ret += " ".join(players)
        return to_ret


class FTL(Location):
    """
    An FTL in a game.

    Attributes:
        expansion - 'Base'
        game - the Game instance associated with this location.
        ship - 'Galactica'
        name - 'FTL Control'
        text - the text on this location card.
        players - a list of players currently present there.
        action - the action that can be taken at that location.
        is_hazardous - whether a location can be moved to.
        is_damaged - whether this location is damaged.
        is_human - False if this location is accessible to revealed Cylons.
    """
    def __init__(self, game):
        """
        Initialize an FTL location.
        """
        Location.__init__(self, game)
        self.name = "FTL Control"
        self.text = read_message("text/loc_desc/ftl.txt")
        self.action = self.ftl_jump

    def ftl_jump(self):
        """
        Jump using FTL.
        """
        pass


class Command(Location):
    """
    A Command location.

   Attributes:
        expansion - 'Base'
        game - the Game instance associated with this location.
        ship - 'Galactica'
        name - 'Command'
        text - the text on this location card.
        players - a list of players currently present there.
        action - the action that can be taken at that location.
        is_hazardous - whether a location can be moved to.
        is_damaged - whether this location is damaged.
        is_human - False if this location is accessible to revealed Cylons.
    """
    def __init__(self, game):
        Location.__init__(self, game)
        self.name = "Command"
        self.txt = read_message("text/loc_desc/command.txt")
        self.action = self.command

    def command(self):
        pass


class Weapons(Location):
    """
    A Weapons Control location.

   Attributes:
        expansion - 'Base'
        game - the Game instance associated with this location.
        ship - 'Galactica'
        name - 'Weapons Control'
        text - the text on this location card.
        players - a list of players currently present there.
        action - the action that can be taken at that location.
        is_hazardous - whether a location can be moved to.
        is_damaged - whether this location is damaged.
        is_human - False if this location is accessible to revealed Cylons.
    """
    def __init__(self, game):
        Location.__init__(self, game)
        self.name = "Weapons Control"
        self.txt = read_message("text/loc_desc/weapons.txt")
        self.action = self.weapons

    def weapons(self):
        pass


class Command(Location):
    """
    A Command location.

   Attributes:
        expansion - 'Base'
        game - the Game instance associated with this location.
        ship - 'Galactica'
        name - 'Command'
        text - the text on this location card.
        players - a list of players currently present there.
        action - the action that can be taken at that location.
        is_hazardous - whether a location can be moved to.
        is_damaged - whether this location is damaged.
        is_human - False if this location is accessible to revealed Cylons.
    """
    def __init__(self, game):
        Location.__init__(self, game)
        self.name = "Command"
        self.txt = read_message("text/loc_desc/command.txt")
        self.action = self.command

    def command(self):
        pass


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
    pass


class Game:
    """
    A game of Battlestar Galactica.

    Attributes:
        bot - the bot associated with this game.
        players - a list of Player objects.
        spectators - a dictionary of player ids and names spectating.
        is_ongoing - True if the game has started.
    """
    def __init__(self, bot):
        self.bot = bot
        self.players = []
        self.spectators = []
        self.is_ongoing = False

    def __str__(self):
        return "A game of Battlestar Galactica."

    def add_player(self, user_id, name):
        """
        Adds a player to the game.

        Parameters:
            user_id - the user id of the player to add.
            name - the name of the player to add.
        """
        if self.is_ongoing:
            raise InvalidMoveError("A game has already started!")
        player = Player(self, user_id, name)
        self.players.append(player)
