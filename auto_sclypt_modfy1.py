import re


def split_dialogue(line, max_length=35):
    # キャラ名とセリフを分離
    match = re.match(r'(.+?「)(.+)(」)', line)
    if not match:
        return [line]  # 形式に合わない場合はそのまま返す

    prefix, text, suffix = match.groups()

    # 30字以内ならそのまま
    if len(text) <= max_length:
        return [line]

    # 分割候補（句読点、助詞の後で分割）
    split_points = [m.start() - 1 for m in re.finditer(r'『', text)] + [m.start() for m in re.finditer(r'[、。！？』]', text)]
    """
    if not split_points:
        split_points = [len(text) // 2]  # 分割点がない場合は強制的に2等分
    """

    # できるだけ均等に分割
    best_split = min(split_points, key=lambda x: abs(x - len(text) // 2))

    # セリフを分割
    first_part = text[:best_split + 1].strip()
    second_part = text[best_split + 1:].strip()

    if len(first_part) <= max_length:
        #分割後、P1とP2どちらも制限内なら改行
        if len(second_part) <= max_length:
            return [f"{prefix}{first_part}"] + [f"{second_part}」"]
        #P1は制限内だがP2が制限を超える場合、P1とP2を分割、P2は再度処理
        return [f"{prefix}{first_part}」"] + split_dialogue(f"{prefix}{second_part}」", max_length)
    #P2は制限内だがP1が制限を超える場合、P1とP2を分割、P1は再度処理
    if len(second_part) <= max_length:
        return split_dialogue(f"{prefix}{first_part}」", max_length) + [f"{prefix}{second_part}」"]
    #P1もP2も制限を超える場合、両方再処理
    return split_dialogue(f"{prefix}{first_part}」", max_length) + split_dialogue(f"{prefix}{second_part}」", max_length)


# --- 動作テスト ---
sample_lines = [
    'ゆっくり魔理沙「さて、今回は前回の動画『仮想現実は可能なのか』の続きについて話していくぜ。」',
'ゆっくり霊夢「よろしくお願いするわ。」',
'ゆっくり魔理沙「まだ前回の動画を見ていない人は、そっちから見ると楽しめるぜ。」',
'ゆっくり魔理沙「前回の動画は、右上の黒いやつ、概要欄、コメントから見れるぜ。」',
'ゆっくり魔理沙「さて、前回は『脳とコンピューターをつなぐ技術』について話したな。」',
'ゆっくり魔理沙「今回は『仮想世界を作る技術』について話していくぜ。」'
]
    

for line in sample_lines:
    formatted = split_dialogue(line)
    print("\n".join(formatted))
