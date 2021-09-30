# TODO: Можно решить с двумя левыми поисками, один больше-вавно, и другой строго больше


# 1. Для начала определяем функции бинарного поиска сдева и справа:
#    (все в соответствии с тем подходом, который был изложен в лекции)
def l_bin_search(left, right, check, check_params):

    while left < right:
        m = (left + right) // 2
        if check(m, check_params):
            right = m
        else:
            left = m + 1
    return left


def r_bin_search(left, right, check, check_params):

    while left < right:
        m = (left + right + 1) // 2
        if check(m, check_params):
            left = m
        else:
            right = m - 1
    return left


# 2. Обрабатываем ввод:
#    (обратите внимание на то, что массив сразу сортируется)
n = int(input())
nums = sorted([int(num) for num in input().split()])


# 3. Определяем функции проверки условий для поисковых функций:
def check(m, eq):
    return nums[m] >= eq


def r_check(m, eq):
    return nums[m] <= eq


# 4. Зная количество запросов можно сразу выделить память под ответы:
check_n = int(input())
ans = ['0'] * check_n

# 5. Для каждого запроса выполняем два поиска по ранее упорядоченному массиву:
for i in range(check_n):
    l, r = map(int, input().split())
#   Суть в том, что мы ищем левую и правую границы области,
#   содержащей элементы со значениями от L до R:
    left_i = l_bin_search(0, n - 1, check, l)
    right_i = r_bin_search(0, n - 1, r_check, r)
#   Далее можно легко посчитать количество элементов в этой области
#   путем вычисления разницы между найенными индексами:
    count = right_i - left_i + 1
    # Ниже проверяем граничные условия:
    if (left_i == right_i == 0 and nums[0] > r) or (left_i == right_i == (n - 1) and nums[n-1] < l):
        ans[i] = '0'
    else:
        ans[i] = str(count)

# 6. Выводим результаты:
print(' '.join(ans))
