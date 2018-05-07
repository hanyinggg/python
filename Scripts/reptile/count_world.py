def count_world(world):
    a = world.count('a')
    o = world.count('o')
    i = world.count('i')
    e = world.count('e')
    u = world.count('u')
    print(a, o, i, e, u)


if __name__ == '__main__':
    word = input('请输入字符串：')
    count_world(word)