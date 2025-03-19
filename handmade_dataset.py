import pandas as pd


df = pd.DataFrame(columns = ['Item', 'Type', 'Effect', 'Recipe'])

df = df.append({'Item':'B.F.대검', 'Type':'기본', 'Effect':'공격력 +10%', 'Recipe':'-'}, ignore_index=True)
df = df.append({'Item':'곡궁', 'Type':'기본', 'Effect':'공격속도 +10%', 'Recipe':'-'}, ignore_index=True)
df = df.append({'Item': '쇠사슬 조끼', 'Type': '기본', 'Effect': '방어력 +20', 'Recipe': '-'}, ignore_index=True)
df = df.append({'Item': '음전자 망토', 'Type': '기본', 'Effect': '마법 저항력 +20', 'Recipe': '-'}, ignore_index=True)
df = df.append({'Item': '쓸데없이 큰 지팡이', 'Type': '기본', 'Effect': '주문력 +10', 'Recipe': '-'}, ignore_index=True)
df = 