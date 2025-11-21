#splits string and returns number of words
def word_count(text):
    split_text = text.split()
    return len(split_text)

#splits string into dictionary of letters and counts total number of each
def character_count(text):
    text = text.lower()
    char_info = {"a": 0,
                 "b": 0,
                 "c": 0,
                 "d": 0,
                 "e": 0,
                 "f": 0,
                 "g": 0,
                 "h": 0,
                 "i": 0,
                 "j": 0,
                 "k": 0,
                 "l": 0,
                 "m": 0,
                 "n": 0,
                 "o": 0,
                 "p": 0,
                 "q": 0,
                 "r": 0,
                 "s": 0,
                 "t": 0,
                 "u": 0,
                 "v": 0,
                 "w": 0,
                 "x": 0,
                 "y": 0,
                 "z": 0,
                };
    print(char_info["a"]);
    char_list = list(text);
    for c in char_list:
        if c == " ":
            continue;
        elif c == "a":
            char_info["a"] += 1;
        elif c == "b":
            char_info["b"] += 1;
        elif c == "c":
            char_info["c"] += 1;
        elif c == "d":
            char_info["d"] += 1;
        elif c == "e":
            char_info["e"] += 1;
        elif c == "f":
            char_info["f"] += 1;
        elif c == "g":
            char_info["g"] += 1;
        elif c == "h":
            char_info["h"] += 1;
        elif c == "i":
            char_info["i"] += 1;
        elif c == "j":
            char_info["j"] += 1;
        elif c == "k":
            char_info["k"] += 1;
        elif c == "l":
            char_info["l"] += 1;
        elif c == "m":
            char_info["m"] += 1;
        elif c == "n":
            char_info["n"] += 1;
        elif c == "o":
            char_info["o"] += 1;
        elif c == "p":
            char_info["p"] += 1;
        elif c == "q":
            char_info["q"] += 1;
        elif c == "r":
            char_info["r"] += 1;
        elif c == "s":
            char_info["s"] += 1;
        elif c == "t":
            char_info["t"] += 1;
        elif c == "u":
            char_info["u"] += 1;
        elif c == "v":
            char_info["v"] += 1;
        elif c == "w":
            char_info["w"] += 1;
        elif c == "x":
            char_info["x"] += 1;
        elif c == "y":
            char_info["y"] += 1;
        elif c == "z":
            char_info["z"] += 1;
        else:
            continue;
    return char_info;