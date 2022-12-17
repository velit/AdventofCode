#!/usr/bin/env python3

def calc_spoken(n):
    inputs = [1,0,15,2,10,13]

    latest_spoken = {}
    for t, spoken in enumerate(inputs[:-1]):
        latest_spoken[spoken] = t

    spoken = inputs[-1]

    for t in range(t + 1, n - 1):
        if spoken in latest_spoken:
            latest_spoken_t = latest_spoken[spoken]
            latest_spoken[spoken] = t
            spoken = t - latest_spoken_t
        else:
            latest_spoken[spoken] = t
            spoken = 0

    return spoken

print(calc_spoken(2020))
print(calc_spoken(30000000))
