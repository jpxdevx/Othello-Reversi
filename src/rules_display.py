from ursina import *
import menu

def view_rules():
    
    rules_container = Entity(parent=camera.ui)
    Entity(parent=rules_container, model="quad", scale=(1.8, 1), texture="textures/rules_background1.png", position=(0, 0, 1))

    Text("RULES", parent=rules_container, position=(-0.38, 0.38, 0),scale=2.2, color=color.orange, font='VeraMono.ttf')
    Entity(parent=rules_container, model="quad", scale=(0.65, 0.005),color=color.orange, position=(-0.3, 0.33, 0))

    rules = [
        "1. The game is played on an 8 × 8 board.",
        "2. Two players take turns.",
        "3. One player uses Black pieces, other uses White.",
        "4. Game starts with four pieces in the center:",
        "    Two black & two white arranged diagonally.",
        "5. Black always plays first.",
        "6. A player must place a piece on an empty square.",
        "7. A move is valid only if it captures opponent pieces.",
        "8. Pieces captured when surrounded in a straight line:",
        "    Horizontal, Vertical, Diagonal.",
        "9. All captured opponent pieces flip to your color.",
        "10. If a player has no valid move, their turn is skipped.",
        "11. The game ends when ",
        "     Board is full or",
        "     Neither player can make a move.",
        "12. Most pieces on the board wins.",
        "13. Equal pieces = draw.",
    ]
    i=1
    for rule in rules:
        c = color.white if rule.startswith("  ") else color.black
        Text(rule, parent=rules_container,position=(-0.6, 0.3 - i * 0.038, -1),scale=1.0, color=c)
        i+=1
    
    tutorial = Animation("textures/tutorial_frames/frame_",fps=15,lo0p=True,parent=rules_container,position=(0.4,0,-4),scale=(0.6,0.4))
    back = Button(text="Back", parent=rules_container,position=(-0.45, 0.43, -0.1), scale=(0.1, 0.05),color=color.orange, highlight_color=color.red,text_size=2.4, on_click=menu.back_to_menu)