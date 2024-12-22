from geometry import *
import numpy as np

class PID:
    """
    Représente un correcteur proportionnel intégral dérivateur. 
    Les coefficients de l'asservissement sont passés en argument à la création de l'instance
    """
    def __init__(self, kp, ki, kd):
        self.Kp = kp
        self.Ki = ki
        self.Kd = kd

        self.error_sum = 0
        self.error_last = 0

    def reset(self):
        self.error_sum = 0
        self.error_last = 0
    
    def integrated(self, error: int) -> int:
        self.error_sum += error
        return self.Ki * self.error_sum

    def derivative(self, error: int) -> int:
        error_delta = error - self.error_last
        self.error_last = error
        return self.Kd * error_delta

    def proportional(self, error: int) -> int:
        return self.Kp * error
    
    def correct(self, error: int) -> int:
        """
        Renvoie la consigne corrigée en fct de l'erreur
        """
        return self.proportional(error) + self.integrated(error) + self.derivative(error)


class Position:
    """
    Permet d'obtenir l'estimation de la position du centre du robot, en se basant sur les
    caractéristiques géométriques du robot.
    """
    def __init__(self, x=0, y=0, angle=np.pi/2):
        self.x = x #En centimètres
        self.y = y #En centimètres
        self.orientation = angle #En degrés

    def update(self, e1: int, e2: int):
        """
        Met à jour la position en fct des incréments des codeurs des roues.
        """ 
        
        if e1 > e2:
            sign = 1
            e1, e2 = e2, e1
        else:
            sign = -1 

        R = WHEEL_SPACE * e1 / (e2-e1)

        theta = sign * (e1 / INCREMENTS) * (WHEEL_RADIUS / R) * 2 * np.pi #Sens trigonométrique
        du, dv = R * (1 - np.cos(theta)), R * np.sin(theta) #Dans le repère du robot
        dx = du * np.cos(self.orientation) - dv * np.sin(self.orientation) #Repère cartésien
        dy = du * np.sin(self.orientation) + dv * np.cos(self.orientation) #Repère cartésien

        self.x += dx
        self.y += dy
        self.orientation += theta 

if __name__ == "__main__":
    pos = Position()
    increment = (3, 6)
    pos.update(*increment)
