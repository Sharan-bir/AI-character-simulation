# AI-Character Simulation (Pygame)

A 2D game built with **Pygame** featuring animated sprites, loading screens, background music, and an interactive menu system.  
This project includes a custom loading screen, animated character on the menu, and smooth UI transitions.

---

## 🎮 Features

- ✔️ Loading screen with fade-in animation  
- ✔️ Main menu with animated sprite (6-frame idle cycle)  
- ✔️ Custom fonts and dialogue UI  
- ✔️ Background music  
- ✔️ Clean project structure using modular files  
- ✔️ Easily expandable for full game logic  

---

## 📁 Project Structure

project/
│── assets/
│ ├── characters/
│ │ └── menu_girl/front_Idle_0–5.png
│ ├── font/Audiowide-Regular.ttf
│ └── music/bg_music.mp3
│── config.py
│── asset_loader.py
│── loading_screen.py
│── menu.py
│── main.py
│── requirements.txt
└── README.md


---

## ▶️ Running the Game

### 1. Create & activate virtual environment

#### Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
OR

#### Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Install all Required packages:
```bash
pip install -r requirements.txt
```

#### Run the game: 
```bash
python main.py
```

#### Contributions :
Feel free to fork the repo and submit pull requests!