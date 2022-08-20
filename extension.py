def remove_extension(img):
    s = ""
    img = img[::-1]
    i = 0
    while(img[i] != '.'):
        s += img[i]
        i += 1
    s = s[::-1]
    print(s)


remove_extension(r'C:\Users\P.Dhanashreenydhi\Downloads\clear images\clear9.jpeg')
