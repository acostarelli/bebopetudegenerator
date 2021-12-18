def chord(*off):
    def fn(root):
        return (root + o for o in off)

    return fn

M   = chord(0, 4, 7, 11)
dom = chord(0, 4, 7, 10)
m   = chord(0, 3, 7, 10)

I   = 0
II  = 2
III = 4
IV  = 5
V   = 7
VI  = 9
VII = 11

sIV = 6