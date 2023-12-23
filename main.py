# Required imports
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint, choice
from kivy.core.window import Window

# Constants
PADDLE_SPEED = 10  # Speed of the paddle movement
BALL_SPEED = 4  # Base speed of the ball
REFRESH_RATE = 1.0 / 60.0  # Screen refresh rate

# Class definition for the pong paddle
class PongPaddle(Widget):
    score = NumericProperty(0)  # Score property for each player

    def bounce_ball(self, ball):
        # Check for collision between ball and paddle
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            # Calculate offset for angle of reflection
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1  # Increase the velocity by 10% after bounce
            ball.velocity = vel.x, vel.y + offset

# Class definition for the pong ball
class PongBall(Widget):
    # Define properties for velocity in X and Y directions
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)  # Combined property for velocity

    def move(self):
        # Move the ball according to its velocity
        self.pos = Vector(*self.velocity) + self.pos

# Main class for the Pong game
class PongGame(Widget):
    ball = ObjectProperty(None)  # Reference to the ball widget
    player1 = ObjectProperty(None)  # Reference to player 1's paddle
    player2 = ObjectProperty(None)  # Reference to player 2's paddle

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.init_keyboard()
        self.keys = set()  # Set to keep track of pressed keys

    def init_keyboard(self):
        # Request a keyboard object
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self._keyboard.bind(on_key_up=self._on_keyboard_up)

    def _keyboard_closed(self):
        # Unbind the keyboard events and close the keyboard
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        # Store the pressed key in the set
        self.keys.add(keycode[1])

    def _on_keyboard_up(self, keyboard, keycode):
        # Remove the released key from the set
        self.keys.remove(keycode[1])

    def serve_ball(self, vel=None):
        # Place the ball in the center and provide it with a starting velocity
        self.ball.center = self.center
        if vel is None:
            direction = choice([-1, 1])  # Randomly choose left or right direction
            self.ball.velocity = direction * BALL_SPEED, randint(-2, 2)
        else:
            self.ball.velocity = vel

    def update(self, dt):
        # Main game loop
        self.ball.move()  # Move the ball
        self.player1.bounce_ball(self.ball)  # Check for ball-paddle bounce for player 1
        self.player2.bounce_ball(self.ball)  # Check for ball-paddle bounce for player 2

        self.paddle_movement()  # Handle paddle movement
        self.check_ball_boundaries()  # Check if ball hits the boundaries
        self.check_scoring()  # Check for scoring

    def paddle_movement(self):
        # Handle paddle movement based on pressed keys
        # For player 1 (using W and S keys)
        if 'w' in self.keys and self.player1.top < self.top:
            self.player1.center_y += PADDLE_SPEED
        if 's' in self.keys and self.player1.y > self.y:
            self.player1.center_y -= PADDLE_SPEED
        # For player 2 (using arrow keys)
        if 'up' in self.keys and self.player2.top < self.top:
            self.player2.center_y += PADDLE_SPEED
        if 'down' in self.keys and self.player2.y > self.y:
            self.player2.center_y -= PADDLE_SPEED

    def check_ball_boundaries(self):
        # Invert ball's Y velocity if it hits the top or bottom boundary
        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1

    def check_scoring(self):
        # Update the score and re-serve the ball if it goes out of bounds
        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball()
        if self.ball.right > self.width:
            self.player1.score += 1
            self.serve_ball()

    def on_touch_move(self, touch):
        # Handle touch movement for controlling paddles on touch devices
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        elif touch.x > self.width * 2 / 3:
            self.player2.center_y = touch.y

# Main app class to run the Pong game
class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()  # Serve the ball initially
        Clock.schedule_interval(game.update, REFRESH_RATE)  # Schedule the game loop
        return game

# Start the app
if __name__ == '__main__':
    PongApp().run()
