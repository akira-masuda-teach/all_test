quizs = ["りんご","みかん","ぶどう"]

print("クイズです")
print("appleは日本語で？")
print()
j = 0
for i in quizs:
    j += 1
    print(str(j)+"."+i)

text = input("回答：")
print(f"あなたは{text}って答えたね！")
print("正解は「りんご」だよ！")