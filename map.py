from settings import TILE

text_map = ["WWWWWWWWWWWW",
            "W.W.WW.....W",
            "W...W...WWWW",
            "W.W.W.....WW",
            "W.......W..W",
            "WWWWWWWWWWWW"]

world_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == "W":
            world_map.add((i * TILE, j * TILE))
