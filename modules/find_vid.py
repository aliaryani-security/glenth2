import pathlib

p = pathlib.Path("/media/thehannibalist/NewF")
files = list(p.glob("*.mkv"))
for f in files:
    print (f)