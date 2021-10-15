from PIL import Image
def co(string):
    i = 0
    while i < len(string):
        j = 0
        c = string[i]
        while i + j < len(string) and string[i + j] == c:
            j+=1
        if j > 3:
            adder = 1 + len(f"[{j}]")
            string = string[:i] + f"[{c}{j}]" + string[i+j:]
            i += adder
        else:
            i+=1
    return string

image = Image.open("image.jpg")
w,h = image.size
#image.show()
image = image.resize((w//4,h//4))
img = image.load()
output = ""
#115
#image.show()
w,h = image.size
print(w)
for i in range(w):
    for j in range(h):
        a,b,c = img[i,j]
        if a >= 240 and b >= 240 and c >= 240:
            output +="0"
        else:
            output +="1"
output = "".join([hex(int(output[i-4:i],base=2))[-1] for i in range(4,len(output),4)])
print(output)
print(len(output))

