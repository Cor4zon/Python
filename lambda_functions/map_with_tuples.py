"""Modify list of tuples"""
bands = [("Beatles", 10), ("Rolling Stones", 12), ("Misfits", 5),
         ("Metallica", 4)]

extra_bands = list(map(lambda band: (band[0], band[1] + 1), bands))
print(bands)
print(extra_bands)