# 🎮 Super Tic Tac Toe

Super Tic Tac Toe is an advanced version of the classic Tic Tac Toe game built using **Python and Pygame**.  
The game features a **3×3 super board**, where each cell contains its own **3×3 sub-board**, creating deeper and more strategic gameplay.

---

## 🧠 How the Game Works

- The main board is a **3×3 grid**
- Each main cell contains a **3×3 sub-board**
- Players take turns placing **X** and **O**
- A move in a sub-cell determines the **next forced sub-board** for the opponent
- If the forced sub-board is already won, the opponent may play anywhere
- Winning three sub-boards in a row, column, or diagonal wins the game

---

## 🧮 Board Structure

### Sub-Board (3×3)
```
[ s00  s01  s02 ]
[ s10  s11  s12 ]
[ s20  s21  s22 ]
```

### Super Board (Matrix of Sub-Boards)
```
super_board[3][3][3][3]
```

### Winner Board
```
[ w00  w01  w02 ]
[ w10  w11  w12 ]
[ w20  w21  w22 ]
```

---

## ✨ Features

- Interactive 2D board using Pygame
- Forced next-board rule
- Sub-board and super-board win detection
- Winning line animation
- Game lock after win
- Restart button
- Clean and minimal UI

---

## 🛠️ Installation

### Clone the Repository
```bash
git clone https://github.com/adeshkamble09/super-tic-tac-toe.git
cd super-tic-tac-toe
```

### Install Dependencies
```bash
pip install pygame
```

### Run the Game
```bash
python Super_Tic_Tac_Toe.py
```

---

## 🎮 Controls

- **Mouse Click** → Place X / O
- **Restart Button** → Reset the game

---

## 🖥️ Requirements

- Python 3.8+
- Pygame 2.x
- Windows / Linux / macOS

---

## 🔮 Future Improvements

- Single-player mode with AI
- Online multiplayer
- Sound effects and advanced animations
- Mobile support

---

## 📜 License

This project is open-source and free to use.

---

## 🙏 Acknowledgements

Thanks to the **Pygame** community for the game framework.

---

> *“Think in matrices. Play with logic.”*
