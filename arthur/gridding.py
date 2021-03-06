import numpy as np
from arthur import constants


def grid(U, V, C, duv, size):
    G = np.zeros((size, size), np.complex64)
    G.fill(0)
    for a1 in range(constants.NUM_ANTS):
        for a2 in range(constants.NUM_ANTS):
            p = 1.0
            if a1 == a2:
                p = 0.5

            u = U[a1, a2] / duv + size / 2 - 1
            v = V[a1, a2] / duv + size / 2 - 1

            w = int(np.floor(u))
            e = int(np.ceil(u))
            s = int(np.floor(v))
            n = int(np.ceil(v))

            west_power = p - (u - w)
            east_power = p - (e - u)
            south_power = p - (v - s)
            north_power = p - (n - v)

            south_west_power = south_power * west_power
            north_west_power = north_power * west_power
            south_east_power = south_power * east_power
            north_east_power = north_power * east_power

            G[s, w] += south_west_power * C[a1, a2]
            G[n, w] += north_west_power * C[a1, a2]
            G[s, e] += south_east_power * C[a1, a2]
            G[n, e] += north_east_power * C[a1, a2]
    return G
