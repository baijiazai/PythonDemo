# 个体
class Item:
    def __init__(self, name, value, weight):
        """" name 为名称，value 为价格，weight 为重量 """
        self.name = name
        self.value = value
        self.weight = weight
    
    def get_value(self):
        return self.value

    def get_weight(self):
        return self.weight

    def __str__(self):
        return '<%s,%s,%s>' % (self.name, str(self.value), str(self.weight))


def use_value(item):
    return item.value


def weight_inverse(item):
    return 1.0 / item.value


def density(item):
    return item.value / item.weight


# 贪婪算法
def greedy(items, max_weight, key_func):
    """ items 为列表，max_weight 为最大承受重量，key_func 为计算函数 """
    items_copy = sorted(items, key=key_func, reverse=True)
    res = []
    total_value, total_weight = 0.0, 0.0
    for i in range(len(items_copy)):
        if total_weight + items_copy[i].weight <= max_weight:
            res.append(items_copy[i])
            total_weight += items_copy[i].weight
            total_value += items_copy[i].value
    return (res, total_value)


# 创建物品列表
def build_items():
    names = ['clock', 'painting', 'pad', 'book', 'computer']
    values = [2800, 1500, 1800, 100, 4400]
    weights = [2, 1.5, 1, 1, 4]
    items = []
    for i in range(len(values)):
        items.append(Item(names[i], values[i], weights[i]))
    return items


# 测试
def test_greedy(items, max_weight, key_func):
    """ items 为列表，max_weight 为最大重量，key_func 为比较函数 """
    taken, val = greedy(items, max_weight, key_func)
    print('Total value of items taken is', val)
    for item in taken:
        print('', item)


def test_greedys(max_weight=4):
    items = build_items()
    print('Use greedy by value to fill knapsack of size', max_weight)
    test_greedy(items, max_weight, use_value)
    print('\nUse greedy by weight to fill knapsack of size', max_weight)
    test_greedy(items, max_weight, weight_inverse)
    print('\nUse greedy by density to fill knapsack of size', max_weight)
    test_greedy(items, max_weight, density)


# 背包问题的最优解
def get_binary_rep(n, num_digits):
    """ n 和 num_digits 为非负整数 """
    res = ''
    while n > 0:
        res = str(n % 2) + res
        n //= 2
    if len(res) > num_digits:
        raise ValueError('not enough digits')
    for i in range(num_digits - len(res)):
        res = '0' + res
    return res


def gen_powerset(lst):
    """ lst 为列表 """
    powerset = []
    for i in range(0, 2 ** len(lst)):
        bin_str = get_binary_rep(i, len(lst))
        subset = []
        for j in range(len(lst)):
            if bin_str[j] == '1':
                subset.append(lst[j])
        powerset.append(subset)
    return powerset


# 背包问题的暴力最优解
def choose_best(pset, max_weight, get_val, get_weight):
    best_val = 0.0
    best_set = None
    for items in pset:
        items_val = 0.0
        items_weight = 0.0
        for item in items:
            items_val += get_val(item)
            items_weight += get_weight(item)
        if items_weight <= max_weight and items_val > best_val:
            best_val = items_val
            best_set = items
    return (best_set, best_val)


def test_best(max_weight=4):
    items = build_items()
    pset = gen_powerset(items)
    taken, val = choose_best(pset, max_weight, Item.get_value, Item.get_weight)
    print('Total value of items taken is', val)
    for item in taken:
        print(item)


if __name__ == "__main__":
    # test_greedys()
    test_best()