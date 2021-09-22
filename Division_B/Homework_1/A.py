completion_code_r = int(input())
interactor_verdict = int(input())
checker_verdict = int(input())


def logic():
    if interactor_verdict == 0:
        if completion_code_r != 0:
            return 3
        else:
            return checker_verdict
    elif interactor_verdict == 1:
        return checker_verdict
    elif interactor_verdict == 4:
        if completion_code_r != 0:
            return 3
        else:
            return 4
    elif interactor_verdict == 6:
        return 0
    elif interactor_verdict == 7:
        return 1
    return interactor_verdict


print(logic())
