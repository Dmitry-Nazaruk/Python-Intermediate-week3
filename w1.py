with open(input('Which file to read? '), 'r') as r_f_l:
    c = 0
    with open(input('Which file to write? '), 'w') as w_f:
        for i in r_f_l.readlines():
            c += 1
            w_f.write(f'{c}: ' + i)


