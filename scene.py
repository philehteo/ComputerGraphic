from player import Player
from cube import Cube
import numpy as np
from light import Light
from sphere import Sphere
import random as rd


class Scene:

    def __init__(self):

        '''
            TO DO render target
            TO DO render ground
            TO DO render arrows
        
        '''
        
        self.sky = []

        self.targets = []

        self.arrows = []

        self.player = Player(position = [2,4,2])

        self.ground = []

        self.lights = []

        self.sky.append(Cube(
            position = [0,0,0],
            eulers = [1,0,0]
            )
        )

        self.targets.append(Cube(
            position = [0,0,3],
            eulers = [0,0,0]
            )
        )
        
        
        
        self.ground.append(Cube(
            position = [0,0,0],
            eulers = [1,1,1]
            )
        )

        self.lights.append(Light(
            [30,-30,25],
            [1,0.8,0.8],
            1
        )
        )
        self.lights.append(Light(
            [15,-15,8],
            [1,0.6,0],
            100
            )
        )


        
    def update(self,speed):
        self.moveArrows(speed)

   
    def move_player(self, dPos : list[2]):
        dPos = np.array(dPos, dtype = np.float32) * 0.15
        self.player.position[0] += dPos[0]
        self.player.position[1] += dPos[1]

      
    def spin_player(self, dTheta, dPhi):

        self.player.theta += dTheta * 0.1
        if self.player.theta > 360:
            self.player.theta -= 360
        elif self.player.theta <0:
            self.player.theta += 360
        
        self.player.phi = min(
            89, max(-89, self.player.phi + dPhi * 0.1)
        )

        self.player.update_vectors()

    def addArrow(self):
        arrow = Cube(
            position=self.player.position,
            eulers=self.player.rotate,
            direction=self.player.forwards
        )
        self.arrows.append(arrow)#TODO ajouter la fleche avec la direction

    def moveArrows(self,speed):
        for arrow in self.arrows:
            for target in self.targets :
                if(arrow.position[2]> 0.8 and np.linalg.norm(target.position-arrow.position) > 0.8 ):
                    arrow.position += arrow.direction * speed