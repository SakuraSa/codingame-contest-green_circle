#coding: utf-8

import sys
import math
import random
from collections import namedtuple

# Complete the hackathon before your opponent by following the principles of Green IT

SCORE_DEPTH = 1

def shadow_input():
    line = input()
    # debug('__input__', line)
    return line


def debug(*args, **wkargs):
    wkargs['file'] = sys.stderr
    print(*args, **wkargs)


class Room:
    def __init__(self, _id, attr):
        self.id = _id
        self.attr = attr

    def modifity_game(self, game):
        for loc in game.locations:
            if loc.cards_location == 'HAND':
                now_count = getattr(loc, self.attr)
                setattr(loc, self.attr, now_count + 1)
                break


Rooms = {
    0: Room(0, "training_cards_count"),
    1: Room(1, "coding_cards_count"),
    2: Room(2, "daily_routine_cards_count"),
    3: Room(3, "task_prioritization_cards_count"),
    4: Room(4, "architecture_study_cards_count"),
    5: Room(5, "continuous_delivery_cards_count"),
    6: Room(6, "code_review_cards_count"),
    7: Room(7, "refactoring_cards_count"),
}

SkillNames = [
    "training",
    "coding",
    "daily_routine",
    "task_prioritization",
    "architecture_study",
    "continuous_delivery",
    "code_review",
    "refactoring",
]


class App:
    def __init__(self):
        self.object_type = 0
        self.id = 0
        self.training_needed = 0
        self.coding_needed = 0
        self.daily_routine_needed = 0
        self.task_prioritization_needed = 0
        self.architecture_study_needed = 0
        self.continuous_delivery_needed = 0
        self.code_review_needed = 0
        self.refactoring_needed = 0

    def input(self):
        inputs = shadow_input().split()
        self.object_type = inputs[0]
        self.id = int(inputs[1])
        self.training_needed = int(inputs[2])  # number of TRAINING skills needed to release this application
        self.coding_needed = int(inputs[3])  # number of CODING skills needed to release this application
        self.daily_routine_needed = int(inputs[4])  # number of DAILY_ROUTINE skills needed to release this application
        self.task_prioritization_needed = int(inputs[5])  # number of TASK_PRIORITIZATION skills needed to release this application
        self.architecture_study_needed = int(inputs[6])  # number of ARCHITECTURE_STUDY skills needed to release this application
        self.continuous_delivery_needed = int(inputs[7])  # number of CONTINUOUS_DELIVERY skills needed to release this application
        self.code_review_needed = int(inputs[8])  # number of CODE_REVIEW skills needed to release this application
        self.refactoring_needed = int(inputs[9])  # number of REFACTORING skills needed to release this application
        return self

    def clone(self):
        a = App()
        a.object_type = self.object_type
        a.id = self.id
        a.training_needed = self.training_needed
        a.coding_needed = self.coding_needed
        a.daily_routine_needed = self.daily_routine_needed
        a.task_prioritization_needed = self.task_prioritization_needed
        a.architecture_study_needed = self.architecture_study_needed
        a.continuous_delivery_needed = self.continuous_delivery_needed
        a.code_review_needed = self.code_review_needed
        a.refactoring_needed = self.refactoring_needed
        return a

    def get_skill_needs(self, skill_name):
        return getattr(self, skill_name + "_needed")

class Player:
    def __init__(self):
        self.player_location = 0
        self.player_score = 0
        self.player_permanent_daily_routine_cards = 0
        self.player_permanent_architecture_study_cards = 0

    def input(self):
        inputs = shadow_input().split()
        self.player_location = int(inputs[0])
        self.player_score = int(inputs[1])
        self.player_permanent_daily_routine_cards = int(inputs[2])
        self.player_permanent_architecture_study_cards = int(inputs[3])
        return self

    def clone(self):
        p = Player()
        p.player_location = self.player_location
        p.player_score = self.player_score
        p.player_permanent_daily_routine_cards = self.player_permanent_daily_routine_cards
        p.player_permanent_architecture_study_cards = self.player_permanent_architecture_study_cards
        return p

class Location:
    def __init__(self):
        self.cards_location = 0
        self.training_cards_count = 0
        self.coding_cards_count = 0
        self.daily_routine_cards_count = 0
        self.task_prioritization_cards_count = 0
        self.architecture_study_cards_count = 0
        self.continuous_delivery_cards_count = 0
        self.code_review_cards_count = 0
        self.refactoring_cards_count = 0
        self.bonus_cards_count = 0
        self.technical_debt_cards_count = 0

    def input(self):
        inputs = shadow_input().split()
        self.cards_location = inputs[0]  # the location of the card list. It can be HAND, DRAW, DISCARD or OPPONENT_CARDS (AUTOMATED and OPPONENT_AUTOMATED will appear in later leagues)
        self.training_cards_count = int(inputs[1])
        self.coding_cards_count = int(inputs[2])
        self.daily_routine_cards_count = int(inputs[3])
        self.task_prioritization_cards_count = int(inputs[4])
        self.architecture_study_cards_count = int(inputs[5])
        self.continuous_delivery_cards_count = int(inputs[6])
        self.code_review_cards_count = int(inputs[7])
        self.refactoring_cards_count = int(inputs[8])
        self.bonus_cards_count = int(inputs[9])
        self.technical_debt_cards_count = int(inputs[10])
        return self

    def clone(self):
        loc = Location()
        loc.cards_location = self.cards_location
        loc.training_cards_count = self.training_cards_count
        loc.coding_cards_count = self.coding_cards_count
        loc.daily_routine_cards_count = self.daily_routine_cards_count
        loc.task_prioritization_cards_count = self.task_prioritization_cards_count
        loc.architecture_study_cards_count = self.architecture_study_cards_count
        loc.continuous_delivery_cards_count = self.continuous_delivery_cards_count
        loc.code_review_cards_count = self.code_review_cards_count
        loc.refactoring_cards_count = self.refactoring_cards_count
        loc.bonus_cards_count = self.bonus_cards_count
        loc.technical_debt_cards_count = self.technical_debt_cards_count
        return loc

    def get_skill_card_count(self, skill_name):
        return getattr(self, skill_name + '_cards_count')

    def set_skill_card_count(self, skill_name, count):
        setattr(self, skill_name + "_cards_count", count)
    
    def get_total_card_count(self):
        return self.training_cards_count + \
            self.coding_cards_count + \
            self.daily_routine_cards_count + \
            self.task_prioritization_cards_count + \
            self.architecture_study_cards_count + \
            self.continuous_delivery_cards_count + \
            self.code_review_cards_count + \
            self.refactoring_cards_count + \
            self.bonus_cards_count + \
            self.technical_debt_cards_count


class Game:
    def __init__(self):
        self.phase = ""
        self.applications = []
        self.players = []
        self.locations = []
        self.actions = []

    def _obj_arr_read(self, cls, count=None):
        if count is None:
            count = int(shadow_input())
        return [cls().input() for _ in range(count)]

    def clone(self):
        g = Game()
        g.phase = self.phase
        g.applications = [a.clone() for a in self.applications]
        g.players = [p.clone() for p in self.players]
        g.locations = [loc.clone() for loc in self.locations]
        g.actions = list(self.actions)
        return g

    def input(self):
        self.phase = shadow_input()
        self.applications = self._obj_arr_read(App)
        self.players = self._obj_arr_read(Player, count=2)
        self.locations = self._obj_arr_read(Location)
        self.actions = [shadow_input() for _ in range(int(shadow_input()))]

    def loop(self):
        while True:
            self.input()

            action_and_score = [
                (eval_game_score(self, act, SCORE_DEPTH), act) 
                for act in self.actions
                if act != 'RANDOM'
            ]
            action_and_score.sort(reverse=True)

            debug_top = 3
            for i, (score, act) in enumerate(action_and_score[:debug_top]):
                debug("act", i, act, score)
            _, best_action = max(action_and_score)

            print(best_action)

    def take_action(self, action):
        args = action.split()
        if args[0] == 'WAIT':
            pass
        elif args[0] == 'MOVE':
            self.take_action_move(int(args[1]))
        elif args[0] == 'RELEASE':
            self.take_action_release(int(args[1]))
        return self

    def take_action_move(self, room_id):
        room = Rooms.get(room_id, None)
        if room is not None:
            room.modifity_game(self)
        else:
            debug("Warn room_id", room_id, "is not defined")  

    def take_action_release(self, app_id):
        hands = None
        hands_after_release = None
        draws = None
        discard = None
        for loc in self.locations:
            if loc.cards_location == 'HAND':
                hands = loc
            elif loc.cards_location == 'DRAW':
                draws = loc
            elif loc.cards_location == 'DISCARD':
                discard = loc
        if draws is None:
            draws = Location()
            self.locations.append(draws)
        if discard is None:
            discard = Location()
            self.locations.append(discard) 
        hands_after_release = hands.clone()

        app = None
        for a in self.applications:
            if a.id == app_id:
                app = a
                break
        if app is None:
            raise ValueError("bad app id=%s: %s" % (app_id, [a.id for a in self.applications]))

        # use skill card
        remain_needs = {
            skill: app.get_skill_needs(skill)
            for skill in SkillNames
        }
        shoddy_skill = 0
        for skill in SkillNames:
            needs = remain_needs.get(skill, 0)
            if needs == 0:
                continue
            cards = hands.get_skill_card_count(skill)
            if cards == 0:
                continue
            used = min(needs, cards)
            shoddy_skill += used
            remain_needs[skill] -= used
            hands_after_release.set_skill_card_count(skill, cards - used)

        # use bonus card
        remain_total = sum(remain_needs.values())
        bonus = hands.bonus_cards_count
        used = min(remain_total, bonus)
        shoddy_skill += used
        remain_total -= used
        hands.bonus_cards_count -= used

        # use shoddy skill
        used = min(remain_total, shoddy_skill)
        shoddy_skill -= used
        remain_total -= used
        debt_added = used

        if remain_total > 0:
            # skill not enough
            return False
        
        # apply changes
        self.locations = [loc for loc in self.locations if loc.cards_location != 'HAND']
        self.locations.append(hands_after_release)
        discard.technical_debt_cards_count += debt_added
        self.players[0].player_score += 1

        return True


Score = namedtuple('Score', [
    'player_score',
    'future_socre',
    'debt_rate',
    'bonus_rate',
], defaults=(0, 0, 0, 0))


def eval_game_score(game, action, depth=0):
    if depth <= 0:
        return Score()

    if action != 'WAIT':
        game = game.clone().take_action(action)

    # feature0: player score
    player_score = game.players[0].player_score

    # feature1: player hand card count
    hands = None
    draws = Location()
    discard = Location()
    for loc in game.locations:
        if loc.cards_location == 'HAND':
            hands = loc
        elif loc.cards_location == 'DRAW':
            draws = loc
        elif loc.cards_location == 'DISCARD':
            discard = loc
    
    total_cards = hands.get_total_card_count() + \
        draws.get_total_card_count() + \
        discard.get_total_card_count()
    
    # feature2: player debt count
    total_debet = hands.technical_debt_cards_count + \
        draws.technical_debt_cards_count + \
        discard.technical_debt_cards_count
    
    # feature3: player debt rate
    debt_rate = total_debet / float(total_cards)

    # feature4: player bonus card count
    bonus = hands.bonus_cards_count + \
        draws.bonus_cards_count + \
        discard.bonus_cards_count
    
    # feature5: player bonus card rate
    bonus_rate = bonus / float(total_cards)

    # feature6: future socre
    future_socre = Score(0, 0, 0, 0)
    if game.phase == 'MOVE':
        next_phase_game = game.clone()
        next_phase_game.phase = 'RELEASE'
        for app in game.applications:
            future_socre = max(
                future_socre, 
                eval_game_score(next_phase_game, "RELEASE %d" % app.id, depth-1))
    # # only predict future score when MOVE phase
    # elif game.phase == 'RELEASE':
    #     next_phase_game = game.clone()
    #     next_phase_game.phase = 'MOVE'
    #     for room in Rooms.values():
    #         future_socre = max(
    #             future_socre, 
    #             eval_game_score(next_phase_game, "MOVE %d" % room.id, depth-1))

    score = Score(
        player_score=player_score, 
        future_socre=future_socre, 
        debt_rate=-debt_rate, 
        bonus_rate=bonus_rate,
    )

    return score


def main():
    try:
        Game().loop()
    except EOFError:
        pass


if __name__ == '__main__':
    main()
