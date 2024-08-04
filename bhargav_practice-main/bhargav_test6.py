# write plus mode
def file_in_write_plus_mode(*i):
    fil, mm = i
    h = open(fil, mm)
    print(h.writable())

    h.write("hello hello hello from write plus mode\n")
    h.writelines("bhargav\nbhargav\nbhargav\nbhargav")

    h.seek(0)

    data = h.read()
    print("text file data:")
    print(data)

    h.close()


file_in_write_plus_mode("bhargav.txt", "w+")


# append plus mode

def file_append_plus_mode(**d):
    fil, mod = d.get("file"), d.get("mode")
    h = open(fil, mod)

    a = h.write("hello\nhello\nhello")
    b = h.write("\nhello\nhello\nhello")
    print(a, b)

    h.seek(0)

    content = h.read()
    print("test file data:")
    print(content)

    h.close()


file_append_plus_mode(file="bhargav2.txt", mode="a+")


# differance between write and write plus

# "w" Mode

# Write-only mode.
# Opens the file for writing.
# If the file already exists, its content is truncated.
# If the file does not exist, a new file is created.
# Reading Not allowed. Attempting to read from a file opened in w mode will raise an error.

# "w+" Mode

# Read and write mode.
# Opens the file for both reading and writing.
# If the file already exists, its content is truncated (erased).
# If the file does not exist, a new file is created.
# Reading Allowed. You can read from the file after writing to it.

# differance between append and append plus

# "a" Mode

# Append-only mode.
# Opens the file for writing.
# If the file already exists, new data will be written at the end of the file without truncating it.
# If the file does not exist, a new file is created.
# Reading Not allowed. Attempting to read from a file opened in a mode will raise an error.

# "a+" Mode
# Read and append mode.
# Opens the file for both reading and appending.
# If the file already exists, new data will be written at the end of the file without truncating it.
# If the file does not exist, a new file is created.
# Reading Allowed. You can read from the file as well as append to it.
