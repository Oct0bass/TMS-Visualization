from manim import *


class Citizen(VMobject):
    def __init__(self, neck, **kwargs):
        super().__init__(self, **kwargs)
        pelvis = neck + .02 * DOWN

        self.add(Circle(.012).move_to(neck).shift(.012*UP))
        self.add(Line(neck, pelvis))
        self.add(Line(pelvis, pelvis + (-.01, -.015, 0)), Line(pelvis, pelvis + (.01, -.015, 0)))

        self.set_fill().set_stroke(WHITE, .2)


class ChinaBrain(MovingCameraScene):
    def construct(self):
        china = SVGMobject(file_name="assets/China-outline.svg").scale(3.5).set_fill(opacity=0).set_stroke(WHITE, 1)

        self.add(china)
        self.next_section("citizens")
        self.play(self.camera.frame.animate.set(width=2))
        citizens = VMobject()
        cx, cy = np.mgrid[-3:3.1:.1, -2:2.1:.1]
        citizen_points = np.vstack((cx.flatten(), cy.flatten())).T
        for point in citizen_points:
            citizens.add(Citizen(np.append(point, (0,))))

        self.play(Create(citizens))
        #self.play(self.camera.frame.animate.set(width=8))
