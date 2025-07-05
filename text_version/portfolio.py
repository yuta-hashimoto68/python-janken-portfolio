#テキスト版「Pythonじゃんけん王」 2025/6/15

import random  # CPUの手をランダムにするためのモジュール

# プレイヤーとCPUの選べる手
hands = ["グー", "チョキ", "パー"]

# プレイヤー名（設定）
player_name = "シロノス（キャンプ好きの白猫）"
cpu_name = "クロノス（クールな黒猫）"

# スコア管理
player_score = 0
cpu_score = 0
draw_count = 0

print("🌲 Pythonじゃんけん王 🐾 開始！")
print(f"あなたのキャラ：{player_name}")
print(f"ライバル　　　：{cpu_name}")
print("-" * 30)

# 勝利条件（先に3回勝った方が勝利）
while player_score < 3 and cpu_score < 3:
    # プレイヤーの入力（選択）
    print("出す手を選んでください：")
    print("0: グー  1: チョキ  2: パー")
    try:
        player_choice = int(input("あなたの手は？（番号で入力）→ "))
        if player_choice not in [0, 1, 2]:
            print("⚠️ 0〜2の番号で選んでね。")
            continue
    except ValueError:
        print("⚠️ 数字で入力してね。")
        continue

    # CPUの手（ランダム）
    cpu_choice = random.randint(0, 2)

    print(f"\n{player_name}：{hands[player_choice]}")
    print(f"{cpu_name}　　：{hands[cpu_choice]}")
    
  # 勝敗判定
    if player_choice == cpu_choice:
        print("→ あいこ！また勝負だ！\n")
        print(f"{player_name}：『わっ、同じだったね。気が合うのかな？』")
        print(f"{cpu_name}　　：『ふっ…偶然だ。次は負けないぞ。』\n")
        draw_count += 1
    elif (player_choice == 0 and cpu_choice == 1) or \
         (player_choice == 1 and cpu_choice == 2) or \
         (player_choice == 2 and cpu_choice == 0):
        print("→ 勝ち！自然の力は負けない！\n")
        print(f"{player_name}：『やった！焚き火で焼いたマシュマロより嬉しいかも！』")
        print(f"{cpu_name}　　：『チッ…一度の勝ちで調子に乗るなよ。』\n")
        player_score += 1
    else:
        print("→ 負け…くっ、次こそ勝つ！\n")
        print(f"{player_name}：『うぅ〜、負けちゃった…。でも、あきらめないよ！』")
        print(f"{cpu_name}　　：『フッ…これが都会派の力さ。田舎者め。』\n")
        cpu_score += 1

    print(f"【現在のスコア】{player_name}：{player_score}勝 / {cpu_name}：{cpu_score}勝 / あいこ：{draw_count}回\n")
    print("-" * 30)

# 最終結果
print("🎉 結果発表 🎉")
if player_score == 3:
    print(f"{player_name} の勝利！\nキャンプ場に平和が戻った…🌲⛺")
else:
    print(f"{cpu_name} の勝利…\n自然派に勝つなんてやるな…🐾")