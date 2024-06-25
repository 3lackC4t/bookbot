def sort_on(dict):
    return dict["num"]

characters = [
    {'char': '6', 'num': 10}, {'char': '9', 'num': 13}, 
    {'char': '5', 'num': 16}, {'char': '4', 'num': 17}, 
    {'char': '3', 'num': 18}, {'char': '8', 'num': 20}, 
    {'char': '0', 'num': 21}, {'char': '7', 'num': 23}, 
    {'char': '2', 'num': 24}, {'char': '1', 'num': 92}, 
    {'char': 'z', 'num': 243}, {'char': 'q', 'num': 324}, 
    {'char': 'j', 'num': 504}, {'char': 'x', 'num': 677}, 
    {'char': 'k', 'num': 1755}, {'char': 'v', 'num': 3833}, 
    {'char': 'b', 'num': 5026}, {'char': 'g', 'num': 5974}, 
    {'char': 'p', 'num': 6121}, {'char': 'w', 'num': 7638}, 
    {'char': 'y', 'num': 7914}, {'char': 'f', 'num': 8731}, 
    {'char': 'c', 'num': 9243}, {'char': 'u', 'num': 10407}, 
    {'char': 'm', 'num': 10604}, {'char': 'l', 'num': 12739}, 
    {'char': 'd', 'num': 16863}, {'char': 'h', 'num': 19725}, 
    {'char': 'r', 'num': 20818}, {'char': 's', 'num': 21155}, 
    {'char': 'n', 'num': 24367}, {'char': 'i', 'num': 24613}, 
    {'char': 'o', 'num': 25225}, {'char': 'a', 'num': 26743}, 
    {'char': 't', 'num': 30365}, {'char': 'e', 'num': 46043}
]
characters.sort(reverse=True, key=sort_on)
print(vehicles)