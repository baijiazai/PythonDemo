# 为拦截敌国巡航导弹袭击，某军工厂开发出一种导弹拦截系统。但这种导弹拦截系统的缺陷是第一发炮弹能到达20000米高度，
# 但是以后每一发炮弹都不能高于前一发炮弹的高度。通常一套这样的系统不能有效拦截所有敌导弹。
# 依次随机输入 N (N < 100) 枚导弹飞来的高度 (< 1000)，计算要拦截所有导弹需要配备多少套这种系统。
import random


def greedy(lst):
    count = 0
    last_hight = 0
    for i in lst:
        if i > last_hight:
            count += 1
        last_hight = i
    return count


if __name__ == "__main__":
    arr = []
    for _ in range(int(input('input 1 - 99 number:'))):
        arr.append(random.randint(1, 10 ** 3 - 1))
    print('导弹高度：', arr)
    print('需要 %d 套系统' % greedy(arr))