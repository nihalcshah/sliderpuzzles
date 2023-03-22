# Slider Puzzles
### *Heuristic Slider Puzzle Solving using AStar and BFS Algorithms*

## What is a Slider Puzzle?
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/15-puzzle-02.jpg/1200px-15-puzzle-02.jpg"  width="30%" >
This is a picture of a slider puzzle. A puzzle is considered solved when the numbers are in order and there is a blank space at the bottom right. 

The script astar.py takes in an unsolved puzzle as a string where a dot is considered the blank space. It can solve 3x3 and 4x4 slider puzzles. 
***In the 4x4, instead of using double-digit numbers, the input has letters A,B,C,D,E,F.***

### The Process: 
I initially solved the puzzles with a brute force algorithm, but this was not fast enough for me. To combat the challenges in speed, I transitioned to an AStar algorithm that used bucketing to achieve my maximum solving speed.
