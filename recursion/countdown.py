def countdown(x):
    if x == 0:
        print('Done')
        return
    else:
        print(f'{x}...')
        countdown(x-1)
        print(f'{x}...')

countdown(3)