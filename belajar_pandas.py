import pandas as pd

data = {
'nama': ['Debby', 'Yandri'],
'umur': [18, 19],
'departemen': ['Ilkel', 'Mtk']
}
df = pd.DataFrame(data)

print(df.index)