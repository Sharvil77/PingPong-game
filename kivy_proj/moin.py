import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import NumericProperty as NP,ReferenceListProperty as RLP,ObjectProperty as OP
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint
class PongPaddle(Widget):
    score = NP(0)
    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            ball.v_x *= -1.1

class PongBall(Widget):
    v_x=NP(0)
    v_y=NP(0)
    v=RLP(v_x,v_y)
    def mov(self):
        self.pos = Vector(*self.v)+self.pos

class PongGame(Widget):
    ball = OP(None)
    player1 = OP(None)
    player2 = OP(None)
    def serve_ball(self):
        self.ball.v = Vector(4,0).rotate(randint(0,360))

    def update(self, dt):
        self.ball.mov()
        if(self.ball.y<0) or (self.ball.y > self.height-50):
            self.ball.v_y *=-1
        if (self.ball.x < 0):
            self.ball.v_x *= -1
            self.player2.score += 1
        if(self.ball.x > self.width-50):
            self.ball.v_x *= -1
            self.player1.score += 1

        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)


    def on_touch_move(self, touch):
        if touch.x< self.width / 1/4:
            self.player1.center_y= touch.y
        if touch.x> self.width * 3/4:
            self.player2.center_y= touch.y

class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update,1.0/60.0)
        return game
PongApp().run()