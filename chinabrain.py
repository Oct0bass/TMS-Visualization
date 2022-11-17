from manim import *

import random
import math


class Citizen(VMobject):
    def __init__(self, neck, **kwargs):
        super().__init__(self, **kwargs)
        self.neck = neck
        self.pelvis = neck + .02 * DOWN

        self.add(Circle(.012).move_to(neck).shift(.012*UP))
        self.add(Line(neck, self.pelvis))
        self.add(Line(self.pelvis, self.pelvis + (-.01, -.015, 0)), Line(self.pelvis, self.pelvis + (.01, -.015, 0)))

        self.set_fill().set_stroke(WHITE, .2)

    def communicate(self, direction=None):
        if direction is None:
            direction = random.choice([LEFT, UL, UP, UR, RIGHT, DR, DOWN, DL])
        wave = FunctionGraph(lambda x: np.sin(100 * PI * x) * .02, x_range=np.array([0, .09]))\
            .rotate(angle_of_vector(direction))\
            .move_to(midpoint(self.neck, self.pelvis) + 0.1 * math.sqrt(2) * direction)\
            .set_stroke(BLUE, .15)

        return Create(wave, run_time=.5)


class ChinaBrain(MovingCameraScene):
    def construct(self):
        china = SVGMobject(file_name="assets/China-outline.svg").scale(3.5).set_fill(opacity=0).set_stroke(WHITE, 1)
        self.add(china)

        self.next_section("citizens")
        self.play(self.camera.frame.animate.set(width=2))
        citizens = VMobject()
        cx, cy = np.mgrid[-4:4.1:.1, -5:5.1:.1]
        citizen_points = np.vstack((cx.flatten(), cy.flatten())).T
        for point in citizen_points:
            citizens.add(Citizen(np.append(point, (0,))))

        self.play(Create(citizens))

        self.next_section("communication")
        comms = []
        for _ in range(100):
            comms.append(random.choice(citizens.submobjects).communicate())
        self.play(AnimationGroup(*comms))
        #self.play(self.camera.frame.animate.set(width=128/9))
