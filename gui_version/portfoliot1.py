#じゃんけん王GUI版 2025/6/15
import tkinter as tk
import random

# キャラセリフ（簡易版）
shironos_lines = {
    "win": ["やった！焚き火マシュマロより嬉しい！"],
    "lose": ["うぅ…次こそは！"],
    "draw": ["あいこだね〜！"]
}
kronos_lines = {
    "win": ["フッ…これが都会の実力さ。"],
    "lose": ["チッ…今回は運がなかっただけだ。"],
    "draw": ["引き分けか。無駄な時間だな。"]
}

# 勝敗判定ロジック
def judge(player, cpu):
    if player == cpu:
        return "draw"
    elif (player == "グー" and cpu == "チョキ") or \
         (player == "チョキ" and cpu == "パー") or \
         (player == "パー" and cpu == "グー"):
        return "win"
    else:
        return "lose"

# ボタンを押したときの処理
def play(player_hand):
    cpu_hand = random.choice(["グー", "チョキ", "パー"])
    result = judge(player_hand, cpu_hand)

    # 結果を画面に表示
    result_text = f"シロノス：{player_hand}　vs　クロノス：{cpu_hand}\n"

    if result == "win":
        result_text += "🎉 勝ち！\n"
    elif result == "lose":
        result_text += "😿 負け…\n"
    else:
        result_text += "🤝 あいこ！\n"

    # セリフ表示
    result_text += f"\n🗨 シロノス：{random.choice(shironos_lines[result])}"
    result_text += f"\n🗨 クロノス：{random.choice(kronos_lines[result])}"

    result_label.config(text=result_text)

# -------------------------------
# Tkinterウィンドウの作成
# -------------------------------
root = tk.Tk()
root.title("Pythonじゃんけん王 GUI版")

# ウィンドウサイズ
root.geometry("400x400")

# ラベル（メッセージ表示）
result_label = tk.Label(root, text="シロノスとじゃんけんしよう！", font=("Helvetica", 14), wraplength=350)
result_label.pack(pady=20)

# ボタン配置（グー・チョキ・パー）
button_frame = tk.Frame(root)
button_frame.pack()

for hand in ["グー", "チョキ", "パー"]:
    btn = tk.Button(button_frame, text=hand, width=10, height=2, font=("Helvetica", 12),
                    command=lambda h=hand: play(h))
    btn.pack(side="left", padx=10)

# メインループ（ウィンドウを表示し続ける）
root.mainloop()
