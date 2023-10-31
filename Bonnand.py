# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
#     notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version,
#       -jupytext.text_representation.format_version,-language_info.version, -language_info.codemirror_mode.version,
#       -language_info.codemirror_mode,-language_info.file_extension, -language_info.mimetype,
#       -toc, -rise, -version
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
#   language_info:
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
# ---

# %% [markdown]
# # un notebook vierge
#
# sauvé en Python

# %%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd




# %%
df = pd.read_csv("media/planetes.csv", skiprows = 96)

df2 = df[["pl_rade", "pl_bmasse"]]
df2= df2.dropna()
df2["radius(km)"] = df2["pl_rade"]*6371
df2["mass(kg)"] = df2["pl_bmasse"]*5.972*10**24
df2["density"] = df2["mass(kg)"]/((4/3)*3.14159*(df2["radius(km)"]*10**3)**3)
df2.plot.scatter("radius(km)", "density", loglog = True, marker = ".", s = 1, color = "green" )
df2.plot.scatter("mass(kg)", "density", loglog = True, marker = ".", s = 1, color = "red" )
df2.plot.scatter("mass(kg)", "radius(km)", loglog = True, marker = ".", s = 1, color = "blue" )

# %%
df = pd.read_csv("media/planetes.csv", skiprows = 96)
df2 = df[["sy_dist", "disc_year"]].dropna()
df3 = df.groupby(by = "disc_year")
annees = df['disc_year'].unique()
dist = []
for a in annees:
    dist.append(df3.get_group(a)['sy_dist'].sum())
plt.plot(annees, dist, marker = 'o', linestyle = '')
plt.show()





# %%

# %%

# %%
