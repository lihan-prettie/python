# 字串處理split()和replace()
text = "a,b,c,d,e,f"
sentence1 = "i like to code"

letters = text.split(",")  # 以逗號分割字串
print(letters)  # 輸出: ['a', 'b', 'c', 'd', 'e', 'f']

sentence2 = sentence1.replace("like", "don't like")
print(sentence2)  # 輸出: i don't like to code
