color = {
    "black": "0",
    "brown": "1",
    "red": "2",
    "orange": "3",
    "yellow": "4",
    "green": "5",
    "blue": "6",
    "violet": "7",
    "grey": "8",
    "white": "9",
}

print(int(color[input().rstrip()]+color[input().rstrip()]+"0"*int(color[input().rstrip()])))