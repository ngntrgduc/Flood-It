 # Flood-It

[Flood It game](https://www.google.com/search?q=flood+it) written in Python.

## Rules

The goal of this game is to fill the whole game board with the same color. Click on one of the six colored cells of the game board to start filling. Filling always starts in the top left corner of the game board.

## Features

- 10 x 10 board, 6 colors, Infinity Level (Randomly generated).
- Simple yet addictive strategy game, and also a time killer. Chilling and relaxing.
- Customize board size, number of cell and theme.

## How to play

1. Clone this repo/[Download zip](https://github.com/ngntrgduc/Flood-It/archive/refs/heads/master.zip) and extract to your folder:
```
git clone https://github.com/ngntrgduc/Flood-It.git
```
2. Install [pygame](https://www.pygame.org/news):
```
pip install pygame
```
3. Go to the folder you have just cloned/downloaded, and run:
```py
py main.py
```

to play game with another board size:
```py
py main.py -s 780
```

and more cells:
```py
py main.py -s 780 -c 20
```

## Usage
```
$ python main.py -h
usage: main.py [-h] [--size SIZE] [--cell CELL]

Flood It game written in Python

options:
  -h, --help            show this help message and exit
  --size SIZE, -s SIZE  Change board size
  --cell CELL, -c CELL  Change number of cells of each row/column
```

## Screenshots
![image](https://user-images.githubusercontent.com/47920109/216643275-3da9226c-2305-4516-816f-f190dff4b1e7.png)
![image](https://user-images.githubusercontent.com/47920109/216643516-fe08dc6d-de0d-450c-a116-ea069d949df3.png)


## TODO(N'T)

- [x] Add flexible board size, cells
- [x] Add more theme
- [x] Add command-line arguments
