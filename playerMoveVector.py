import pygame


class PlayerMoveVector():

    def __init__(self,):
        self.vector = [0, 0]
        self.ACTIONS = {
            pygame.K_LEFT:  {"axis": 0, "value": -1},
            pygame.K_RIGHT: {"axis": 0, "value": 1},
            pygame.K_UP:    {"axis": 1, "value": -1},
            pygame.K_DOWN:  {"axis": 1, "value": 1},
        }

    def __getitem__(self, i):
        return self.vector[i]

    def do_action(self, key):
        self.vector[self.ACTIONS[key]["axis"]] = self.ACTIONS[key]["value"]

    def clearFirstAxis(self):
        self.vector[0] = 0

    def clearSecondAxis(self):
        self.vector[1] = 0

    def clearBothAxises(self):
        self.vector = [0,0]