import itertools
import json


def character_name_from_count(count):
    JAPANESE_NAME = ['0', 'イチ', 'に', '三', 'ヨン', 'ご', '六', 'ナナ', 'はち', '九', '拾']
    if count > 10:
        return f'{JAPANESE_NAME[10]}{JAPANESE_NAME[count % 10]}'
    return JAPANESE_NAME[count]


SET_TAGS = ['Usa', 'コザ', 'さいたま', '津']
count = 0
# タグの組み合わせを全パターン出す
characters = []
for len_count in range(len(SET_TAGS) + 1):
    for tags in itertools.combinations(SET_TAGS, len_count):
        characters.append({
            'name': character_name_from_count(count),
            'tags': tags,
        })
        count += 1

print(json.dumps(characters, ensure_ascii=False, indent=2))
