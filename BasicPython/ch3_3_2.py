fam={
    "엄마":"김자옥",
    "아빠":"이석진",
    "아들":"이동민",
    "딸":"이지영"
}

print(fam.values())  #value들의 목록을 보여준다.

print("이지영" in fam.values())

for i in fam.values():
    print(i)

print(fam.keys())

for i in fam.keys():
    vv=fam[i]
    print(i,vv)

#위와 아래가 같은 내용
for i,j in fam.items():
    print(i,j)
