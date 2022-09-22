# TEST CASES
# - happy.jpg >> image/jpeg
# - document.pdf >> application/pdf

# .gif > image/gif
# .jpg > image/jpeg
# .jpeg > image/jpeg
# .png > image/png
# .pdf > application/pdf
# .txt > text/plain
# .zip > application/zip
# - default output >  application/octet-stream

text = input("File name: ")
# find period
text = text.split('.')
# var for last item, lowercase, no spaces
ext = text[-1].lower().strip()

if ext == "gif":
    print("image/gif")
elif ext == "jpg":
    print("image/jpeg")
elif ext == "jpeg":
    print("image/jpeg")
elif ext == "png":
    print("image/png")
elif ext == "pdf":
    print("application/pdf")
elif ext == "txt":
    print("text/plain")
elif ext == "zip":
    print("application/zip")
else:
    print("application/octet-stream")
