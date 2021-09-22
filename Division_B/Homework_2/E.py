_ = int(input())
folders = [int(folder) for folder in input().split()]


def solution():
    sum_watched = 0
    current_max_to_watch = 0

    for folder in folders:
        if folder > current_max_to_watch:
            sum_watched += current_max_to_watch
            current_max_to_watch = folder
        else:
            sum_watched += folder

    return sum_watched


print(solution())
