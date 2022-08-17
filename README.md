# DinoScript
A basic Python script to play the Chrome Dino game

The script works by creating 3 box images, one base image, and 2 comparison images, one to check for birds, and one for cactus. Each box i basically only a line 1 pixel in height and 50 pixels in length, the small box size is kept small to reduce processing time.

The script will reliably play the game upto the point where day/night transition occurs; at that point, even if there is no obstacle, since the screen changes slightly between the period where the script creates the base and comparison image, the script will attempt to jump, ending in colliding with the next obstacle.
