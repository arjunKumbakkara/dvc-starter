with open("artifacts01.txt","r") as f:
    text=f.read()

with open("artifacts03.txt","w") as f:
    f.write(text)

print("End of stage 03")