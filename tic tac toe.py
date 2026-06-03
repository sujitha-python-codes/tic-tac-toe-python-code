import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("750x850")
root.configure(bg= "#0f172a")
root.resizable(False,False)

title = tk.Label(root,
                 text = "TIC TAC TOE",
                 font=("Helvetica", 40, "bold"),
                 fg='white',
                 bg='#0f172a'
                 )
title.pack(pady=20)

label1 = tk.Label(root,
              text= "Player X's Turn",
              font=("Arial", 24),
              fg="#38bdf8",
              bg="#0f172a"
              )
label1.pack(pady=15)

frame=tk.Frame(root,bg="#0f172a")
frame.pack(pady=20)

x_score = 0
o_score = 0
draw_score = 0
current_player='X'

score_frame = tk.Frame(
    root,
    bg="#111827",
    bd=2
)

score_frame.pack(pady=20)

x_label = tk.Label(score_frame,
                   text= "X Wins\n0",
                   font=("Arial",18,"bold"),
                   fg='#3b82f6',
                   bg='#111827')
x_label.grid(row=0,column=0,padx=40)

draw_label = tk.Label(score_frame,
                   text= "Draws\n0",
                   font=("Arial",18,"bold"),
                   fg="#facc15",bg="#111827")
draw_label.grid(row=0,column=1,padx=40)

o_label = tk.Label(
    score_frame,
    text="O Wins\n0",
    font=("Arial",18,"bold"),
    fg="#ef4444",
    bg="#111827"
)

o_label.grid(row=0,column=2,padx=40)

def button_click(btn):

    global current_player, x_score, o_score, draw_score

    if btn['text'] == '':
        btn['text'] = current_player
        winner = check_winner()
        if winner:
            if winner == 'X':
                x_score += 1
                x_label.config(text=f"X Wins\n{x_score}")
            else:
                o_score += 1
                o_label.config(text=f"O Wins\n{o_score}")

            messagebox.showinfo("Game Over",f"Player {winner} Wins!" )

            disable_buttons()
            return
        
        if check_draw():
            draw_score += 1
            draw_label.config(
                text=f"Draws\n{draw_score}")
            messagebox.showinfo("Game Over","It's a Draw!")
            disable_buttons()
            return

        current_player = ('O' if current_player == 'X' else 'X')
        label1.config(text=f"Player {current_player}'s Turn")
def disable_buttons():
    for btn in buttons:
        btn.config(state="disabled")
        
def restart_game():
    global current_player
    current_player ="X"
    label1.config(text = "Player X's Turn")
    
    for btn in buttons:
        btn["text"] = ""
        btn["state"] = "normal"
            
buttons=[]
for i in range (3):
    for j in range(3):
        btn=tk.Button(frame,text = "",
                    width=5,
                    height=2,
                    font=("arial",28,"bold"),
                    bg='#1e293b',
                    fg='white',
                    activebackground="#374151"
                    
        )
        btn.config(command=lambda b=btn:button_click(b))
        btn.grid(row=i,column=j,padx=8,pady=8)
        buttons.append(btn)
              
def check_winner():
    winning_positions= [
        [0,1,2],[3,4,5],[6,7,8],  #rows
        [0,3,6],[1,4,7],[2,5,8],  #columns
        [0,4,8],[2,4,6]           #diagonals
        ]
    for pos in winning_positions:
        if(buttons[pos[0]]["text"] != "" and
           buttons[pos[0]]["text"] ==
           buttons[pos[1]]["text"] ==
           buttons[pos[2]]["text"]
        ):
            return buttons[pos[0]]["text"]
    return None
    
def check_draw():
    for btn in buttons:
        if btn['text']=='':
            return False
    return True

restart_btn=tk.Button(root,text="Restart Game",
                      command=restart_game,
                      font=("Arial",18,"bold"),
                      width=20,
                      height=2,
                      bg="#7c3aed",
                      activebackground="#8b5cf6",
                      fg='black')
restart_btn.pack(pady=20)

root.mainloop()