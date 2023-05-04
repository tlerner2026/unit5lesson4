import pandas as pd
import matplotlib.pyplot as plt
url = "https://en.wikipedia.org/wiki/United_States"
dfs = pd.read_html(
    url,
    match = "Historical population"
)
df = dfs[0]
df = df.iloc[0:-2]
df = df[["Census", "Pop."]].astype("int")
print(df)
df.plot(x = "Census", y = "Pop.")
plt.show()