# Slider Puzzles
### *Heuristic Slider Puzzle Solving using AStar and BFS Algorithms*

## What is a Slider Puzzle?
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/15-puzzle-02.jpg/1200px-15-puzzle-02.jpg"  width="30%" >
This is a picture of a slider puzzle. A puzzle is considered solved when the numbers are in order and there is a blank space at the bottom right. 

The script astar.py takes in an unsolved puzzle as a string where a dot is considered the blank space. It can solve 3x3 and 4x4 slider puzzles.\
***In the 4x4, instead of using double-digit numbers, the input has letters A,B,C,D,E,F.***

The purpose of this was for my Artificial Intelligence 1 class in my Junior year of high school at Thomas Jefferson High School of Science & Technology.

### The Process: 
I initially solved the puzzles with a brute force algorithm, but this was not fast enough for me. To combat the challenges in speed, I transitioned to an AStar algorithm that used bucketing to achieve my maximum solving speed.


### Running and Testing:
These scripts are to be run directly from the command line in the following form

> `python eights.py 26348157_` or \
>   `python eights.py "Eckel55G.txt"`

The slider puzzles are 3x3 or 4x4, written in the format 2561437_8 where the actual puzzle is\
| 2 | 5 | 6 | \
| 1 | 4 | 3 | \
| 7 | _ | 8 |

