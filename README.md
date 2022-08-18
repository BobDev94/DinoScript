# DinoScript
A basic Python script to play the Chrome Dino game

The script works by taking a 100x14 pixel sized image in front of the dino and cropping it into two equal parts for comparison. If the two parts have an unequal pixel color sum, this means an obstacle is approaching and the script will command the dino to jump. The origin point for the box is increased with number of jumps over time to give the dino more time and distance to jump at high speeds. The script will fail once speed of the game is too high. The current high score achieved with this script is 2342.
