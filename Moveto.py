# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 14:00:15 2024

@author: angel
"""

    def killWumpus(self):
        if self.wumpus_location:
            wx, wy = self.wumpus_location.row, self.wumpus_location.col
            if wy < self.y:
                return "shoot_up"
            elif wy > self.y:
                return "shoot_down"
            elif wx < self.x:
                return "shoot_left"
            elif wx > self.x:
                return "shoot_right"
        return None

    def moveTo(self, point):
        if point.row < self.y:
            self.y -= 1
            return "move_up"
        elif point.row > self.y:
            self.y += 1
            return "move_down"
        elif point.col < self.x:
            self.x -= 1
            return "move_left"
        elif point.col > self.x:
            self.x += 1
            return "move_right"
        return "stay"