def giv_sam_leest(leest):
    me_sam = 0
    for ting in leest:
        me_sam += ting
    return me_sam

leest = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(giv_sam_leest(leest))