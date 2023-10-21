import qm

quine = qm.QuineMcCluskey()
print(
    quine.simplify([
        1, 12, 24, 26, 29, 30, 31, 35, 39, 40, 42, 45, 46, 47, 48, 49, 51, 54,
        58, 62, 66, 69, 73, 33, 74, 56, 36
    ]))
