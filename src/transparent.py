# pip install rembg
from rembg import remove

with open("cloud3.png", "rb") as f:
    result = remove(f.read())

with open("cloud3_transparent.png", "wb") as f:
    f.write(result)