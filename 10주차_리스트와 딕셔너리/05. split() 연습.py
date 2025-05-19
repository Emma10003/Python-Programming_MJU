text = "I saw a stray cat near my home."
tokens = text.split()
print(tokens)
print(f"tokens의 자료형: {type(tokens)}")

print("-"*50)

re_text = " ".join(tokens)
print(re_text)
print(f"re_text의 자료형: {type(re_text)}")