#画像＆スコア付きじゃんけん王
import tkinter as tk
from PIL import Image, ImageTk  # 画像を表示するためにPillowが必要！
import random

# --- キャラセリフ（簡略版） ---
shironos_lines = {
    "win": ["やった〜！マシュマロよりうれしい！"],
    "lose": ["うぅ…また負けたぁ…"],
    "draw": ["気が合うかも？"]
}
kronos_lines = {
    "win": ["フッ…都会の実力さ。"],
    "lose": ["チッ、こんなの偶然だ。"],
    "draw": ["引き分け…つまらんな。"]
}

# --- 勝敗判定 ---
def judge(player, cpu):
    if player == cpu:
        return "draw"
    elif (player == "グー" and cpu == "チョキ") or \
         (player == "チョキ" and cpu == "パー") or \
         (player == "パー" and cpu == "グー"):
        return "win"
    else:
        return "lose"

# --- 勝ち数管理 ---
player_score = 0
cpu_score = 0

# --- ゲーム処理 ---
def play(player_hand):
    global player_score, cpu_score
    cpu_hand = random.choice(["グー", "チョキ", "パー"])
    result = judge(player_hand, cpu_hand)

    # セリフ
    result_text = f"シロノス：{player_hand} vs クロノス：{cpu_hand}\n"
    if result == "win":
        result_text += "🎉 勝ち！\n"
        player_score += 1
    elif result == "lose":
        result_text += "😿 負け…\n"
        cpu_score += 1
    else:
        result_text += "🤝 あいこ！\n"

    result_text += f"\n🗨 シロノス：{random.choice(shironos_lines[result])}"
    result_text += f"\n🗨 クロノス：{random.choice(kronos_lines[result])}"

    # 表示更新
    result_label.config(text=result_text)
    score_label.config(text=f"🎌 シロノス：{player_score}勝　|　クロノス：{cpu_score}勝 🐾")

# --- GUI構築 ---
root = tk.Tk()
root.title("Pythonじゃんけん王 GUI版")
root.geometry("500x600")

# --- キャラ画像の読み込み（Pillowが必要） ---
shironos_img = Image.open("shironos.png").resize((150, 150))
kronos_img = Image.open("kronos.png").resize((150, 150))
shironos_photo = ImageTk.PhotoImage(shironos_img)
kronos_photo = ImageTk.PhotoImage(kronos_img)

# --- 画像表示 ---
image_frame = tk.Frame(root)
image_frame.pack(pady=10)

tk.Label(image_frame, image=shironos_photo).pack(side="left", padx=40)
tk.Label(image_frame, image=kronos_photo).pack(side="right", padx=40)

# --- スコア表示 ---
score_label = tk.Label(root, text="🎌 シロノス：0勝　|　クロノス：0勝 🐾", font=("Helvetica", 14))
score_label.pack(pady=10)

# --- 結果とセリフ ---
result_label = tk.Label(root, text="シロノスとじゃんけんしよう！", font=("Helvetica", 14), wraplength=450)
result_label.pack(pady=20)

# --- じゃんけんボタン ---
button_frame = tk.Frame(root)
button_frame.pack()

for hand in ["グー", "チョキ", "パー"]:
    btn = tk.Button(button_frame, text=hand, width=10, height=2, font=("Helvetica", 12),
                    command=lambda h=hand: play(h))
    btn.pack(side="left", padx=10)

root.mainloop()
