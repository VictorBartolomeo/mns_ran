from ctypes.wintypes import PUSHORT

notes=(("franck",(5,14,8)),
    ("tom",(1,14,18)),
    ("Didier", (12,18,20)),
)

for personne in notes:
    note_personne=personne[1]
    moyenne=sum(note_personne)/len(note_personne)
    print(f"{personne[0]} a {moyenne:.2f} de moyenne")

