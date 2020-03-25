w = int(input("Weight: "))
weight = input("(L)bs or (K)g :")
if weight.upper() == "L":
    w = w * 0.45
    print(f'You are {w} kilos')
elif weight.upper() == "K":
    w = w / 0.45
    print(f'You are {w} pounds')
else:
    print("Please enter valid letter")


