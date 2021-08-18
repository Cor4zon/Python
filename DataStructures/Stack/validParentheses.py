from myStack import Stack

def func_real_func(s: str) -> bool:
    branches_stack = Stack()
    open_branches = '[({'
    close_branches = '])}'

    for i in range(len(s)):
        if s[i] in open_branches:
            branches_stack.push(s[i])
            continue
        if s[i] in close_branches:
            try:
                if open_branches.index(branches_stack.pop()) == close_branches.index(s[i]):
                    continue
                else:
                    return False
            except:
                # print("STACK UNDERFLOW")
                return False


    if len(branches_stack.stack) == 0:
        return True


