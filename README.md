# 🧠 Super Tic Tac Toe (Matrix-Based Game)

Super Tic Tac Toe is an advanced version of the traditional Tic Tac Toe game, designed and implemented using **Python and Pygame**.  
The core logic of the game is built entirely on **matrix operations**, making it a practical application of mathematical concepts such as **2D matrices, nested matrices, and matrix traversal**.

---

## 📌 Project Overview

Unlike standard Tic Tac Toe, this version consists of:
- A **3×3 Super Board**
- Each cell of the super board contains a **3×3 Sub-Board**
- Total playable cells: **81**

The game enforces strategic gameplay using a **forced next-board rule**, where each move determines the opponent’s next playable sub-board.

---

## 🧮 Matrix-Based Design

This project is completely driven by matrices:

### 1️⃣ Sub-Board Matrix (3×3)
Each sub-board is represented as a **square matrix**:
[ x00  x01  x02 ] [ x10  x11  x12 ] [ x20  x21  x22 
### 2️⃣ Super Board Matrix (3×3 of 3×3)
The full game board is a **matrix of matrices**:
super_board[3][3][3][3]
### 3️⃣ Winner Board Matrix
Once a sub-board is won, the result is stored in a separate matrix:
[ w00  w01  w02 ] [ w10  w11  w12 ] [ w20  w21  w22 ]
This matrix is then used to determine the **overall winner**.

---

## 🎯 Game Rules

- Players take turns placing **X** and **O**
- A move inside a sub-board at position `(i, j)` forces the opponent to play in super-board cell `(i, j)`
- If the forced sub-board is already won, the opponent may play anywhere
- A player wins the game by winning **three sub-boards in a row, column, or diagonal**

---

## 🏆 Features

- Matrix-driven game logic
- Sub-board and super-board win detection
- Forced next-board rule
- Win animation across the super board
- Game lock after victory
- Restart button
- Clean and minimal UI using Pygame

---

## 🧑‍💻 Technologies Used

- **Python 3**
- **Pygame**
- **Matrix-based data structures (2D & 4D arrays)**

---

## 📚 Educational Value

This project demonstrates:
- Practical application of **matrix theory**
- Nested matrix traversal
- Index mapping and logical conditions
- Integration of mathematics with programming
- Real-time visualization of mathematical logic

It is suitable for:
- Academic projects
- Mathematics & programming demonstrations
- Viva and technical presentations

---

## 🚀 How to Run

1. Install dependencies:
   ```bash
   pip install pygame
2. to run game:
   python Board.py
