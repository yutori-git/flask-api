pre_script = '''
ゆっくり霊夢「それって、まさにゲームの世界に閉じ込められるってこと？」
ゆっくり魔理沙「そういうことだぜ。今のVRでも、長時間プレイすると現実と仮想の区別がつかなくなる『サイバースペース酔い』って現象がある。フルダイブVRなら、それがさらに深刻な問題になる可能性があるんだ。」
ゆっくり霊夢「確かに、それは怖いわね。」
ゆっくり魔理沙「さらに、脳に信号を送ることで、外部から人の意識を操作することが可能になる危険性もある。たとえば、悪意のあるプログラムが侵入したら、プレイヤーの感情や記憶を操作することができるかもしれないんだぜ。」
'''


def main(text):
    lines = text.split('\n')
    formatted_text = ',\n'.join([f"'{line.strip()}'" for line in lines])
    print(formatted_text)

text = [f"{formatted_text}"]

 #セリフを文ごとに分割する関数（区切り文字：。、！、？）
def split_lines(text):
    result = []
    for line in text:
        # 正規表現で「。」、「！」「？」で区切り
        sentences = re.split(r'([。！？])', line)
        for i in range(0, len(sentences) - 1, 2):  # 文と句読点をペアにする
            sentence = sentences[i].strip() + sentences[i+1]  # 文と句読点を結合
            if sentence.strip():  # 空でない場合にのみ追加
                result.append(f"'{sentence.strip()}」',")  # カンマなしで追加
    return result

if __name__ == "__main__":
    main(pre_script)

# 実行して結果を表示
formatted_text = split_lines(text)
for line in formatted_text:
    print(line)