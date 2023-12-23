# PingPongGame
Readme Details
1. Introduction:
This program simulates the classic Pong game using the Kivy framework in Python. Players can control paddles using the keyboard or by touch (for touch-enabled devices) to bounce the ball back and forth. The objective is to prevent the ball from passing your paddle.

How to Run the Program:
I.	Ensure you have Python and the Kivy framework installed on your computer.
II.	Navigate to the directory containing `main.py` and `pong.kv`.
III.	Run the ‘main.py’ to start the game.

Additional Information:
- The game's logic is written in `main.py`, while the visual elements and layout are defined in `pong.kv`.
- Players can control the left paddle using the 'W' and 'S' keys and the right paddle using the 'UP' and 'DOWN' arrow keys.

2.  User Experience Details


•	Responsiveness: The game has a fixed refresh rate of 60Hz (1/60 seconds), which should make ball and paddle movements smooth for the user.

•	Restart Mechanism: Whenever a point is scored, the ball is re-served to restart the game. This immediate restart keeps the gameplay flowing without much downtime.

•	Accessibility: The game seems accessible for players who prefer keyboard or touch input. 

•	Feedback & Dynamics: The ball's speed increases by 10% every time it bounces off a paddle. This can make the game progressively challenging the longer a rally goes on, increasing tension and engagement. Scoring is straightforward. If the ball goes past a player's paddle, the opposite player scores a point.

•	Simplicity: The game of Pong is inherently simple. Two paddles, one ball, and a basic objective of preventing the ball from passing your paddle. This simplicity ensures that users can understand the game mechanics almost instantly.

•	Control Mechanisms: 
o	Keyboard Input: The game supports keyboard inputs for both players. Player 1 uses the 'W' and 'S' keys, and Player 2 uses the 'UP' and 'DOWN' arrow keys. This split setup is familiar for two-player games on a single keyboard.
o	Touch Input: The game also supports touch-based movement. Players can drag their paddles up or down on touch devices. This feature makes the game mobile friendly.
