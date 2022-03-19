from ssl import ALERT_DESCRIPTION_UNKNOWN_PSK_IDENTITY
import tkinter as tk
import requests, time, math

global apikey
apikey = "########-####-####-####-############" 

def hypixelinfo(canvas):
    global apikey
    BASE = 10_000
    GROWTH = 2_500
    REVERSE_PQ_PREFIX = -(BASE - 0.5 * GROWTH) / GROWTH
    REVERSE_CONST = REVERSE_PQ_PREFIX
    GROWTH_DIVIDES_2 = 2 / GROWTH
    ign = textField.get()
    api = "https://api.hypixel.net/player?key="+ apikey +"&name=" + ign
    
    data = requests.get(api).json()
    username = data['player']['displayname']
    ap = data["player"]["achievementPoints"]
    exp = int(data["player"]["networkExp"])
    exp2 = math.floor(1 + REVERSE_PQ_PREFIX + math.sqrt(REVERSE_CONST + GROWTH_DIVIDES_2 * exp))

    try:
        rank = data['player']['newPackageRank']

        try:
            rank = data['player']['monthlyPackageRank']

            if rank == 'NONE':
                rank = data['player']['newPackageRank']
            
        except KeyError:
            pass

        if rank == 'VIP_PLUS':
            rank = 'VIP+'
        elif rank == 'MVP_PLUS':
            rank = 'MVP+'
        elif rank == 'SUPERSTAR':
            rank = 'MVP++'
        elif rank == 'NONE':
            pass

    except KeyError:
        pass

    final_info = f"[{rank}] {username}"  
    final_data = f"\nHypixel Network Level: {exp2}\nAchievement Points: {ap}" 
    credits = f"\n©2022 www.bludenz.dev. All rights reserved"
    label1.config(text = final_info)
    label2.config(text = final_data)
    label3.config(text = credits)


canvas = tk.Tk()
canvas.geometry("550x400")
canvas.title("Hypixel Stats")
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textField = tk.Entry(canvas, justify='center', width = 20, font = t)
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', hypixelinfo)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()
label3 = tk.Label(canvas, font=f)
label3.pack()
canvas.mainloop()
