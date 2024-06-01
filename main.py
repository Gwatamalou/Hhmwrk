#таск 1
def _transposition_str(strA):
    third = int((len(strA))/3)
    strB = strA[third:third*2] + ''.join(strA[third*2:] if len(strA)%3 == 0 else strA[third*2:]) + strA[:third]
    return strB

#таск 2
def _swap_chr(strA, i, y):
    strA = list(strA)
    strA[i-1], strA[y-1] = strA[y-1], strA[i-1]
    strB = ''.join(strA)
    return str(strB)

#таск 3
def _task_3():
    li = [1, 2, 3, 4, 5]
    print('a:', li[0], 'б:', li[-1], 'в:', li[1], 'г:', li[-2],)
    li[li.index(5)] = 6
    li.append(7)
    li.insert(li.index(6), 5)
    print('д, е, ж:', li)
    return

#таск 4
def _task_4(li, i, y):
    li[i-1], li[y-1] = 0, 0
    li[0], li[-1] = li[-1], li[0]
    return li




print('таск 1')
print(_transposition_str(input('enter text: ')))

print('таск 2')
print(_swap_chr(str(input('enter text: ')), int(input('enter index first item: ')), int(input('enter nidex second item: '))))

print('таск 3')
_task_3()

print('таск 4')
print(_task_4([10, 20, 30, 40, 50, 60], int(input('enter index first item: ')), int(input('enter nidex second item: '))))



