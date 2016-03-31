'''

'''

def dayofweek(d, m, y):
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    y -= m < 3
    return (y + y/4 - y/100 + y/400 + t[m-1] + d) % 7

def main():
    day = dayofweek(30, 8, 2010)
    print(int(day))

if __name__ == '__main__':
    main()