pizzaWidth = int(input())
pizzaCheese = int(input())
result = ""
if pizzaWidth==3 and pizzaCheese>=95:
  result="absolutely"
elif pizzaWidth==1 and pizzaCheese<=50:
  result="fairly"
else:
  result="very"

print(f"C.C. is {result} satisfied with her pizza.")