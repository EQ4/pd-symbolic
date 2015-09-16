
with open('./.lily_header.txt', 'r') as h:
    header = h.read()

with open("./.lily_music.txt", 'r') as m:
    music = m.read()

with open("./.lily_footer.txt", 'r') as f:
    footer = f.read()

with open("./.lily_code.ly", 'w+') as c:
    c.write(header)
    c.write (music)
    c.write(footer)
    c.close()
