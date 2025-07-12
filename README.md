# Maze Solver
## Idea
_"An agent traverses a randommly generated Maze"_

## Current Progress
### Maze Generation
Running `mazeGen.py` returns a window with a 10x10 grid that can be navigated using WASD 

<img width="1014" height="969" alt="image" src="https://github.com/user-attachments/assets/a65f95b0-6a54-4c97-8ed7-c8991944f4e5" />

_(Initial Map)_

Grid walls will automatically be deleted upon approaching them, enabling the user to create a free maze with no restrictions (No fixed ends or minimum wall restrictions)

<img width="1177" height="958" alt="image" src="https://github.com/user-attachments/assets/6e61d26a-6d64-491f-823e-f72ac86982c5" />

_(User Inputed Map)_

### Traversal Logic

The `randomDfs.py` file tackles traversal of the maze using Randomized Depth First Searching.
The Tree to be traversed is created in `treeMaker.py` which converts a 10x10 array into a complete graph which is then traversed 

The `mazeGen.py` file wil utilize the path array in order to open grid walls to make a maze instead of asking the User to input WASD keys 
