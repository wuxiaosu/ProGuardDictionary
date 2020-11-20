import random

result = set()

# keys = ["i", "I", "l", "L", "1"]

keys = ["0", "O", "o"]


# keys = ["欚", "襵", "聰", "纒", "矘"]


# keys = ["富强", "民主", "文明", "和谐",
#         "自由", "平等", "公正", "法治",
#         "爱国", "敬业", "诚信", "友善"]


def create():
    for o in range(1, 100000):
        # 长度 7- 13 位
        for l in range(6, 13):
            # 按照长度随机拼接
            temp = keys[random.randint(0, 1)]
            for i in range(1, l + 1):
                temp += random.choice(keys)
            result.add(temp)

    print("成功生成字典，数量：", len(result))

    with open("dict_2.txt", mode='w+', encoding='utf-8') as f:
        f.writelines("\n".join(result))
        f.flush()


if __name__ == '__main__':
    create()
