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
import numpy as np
import pandas as pd
import matplolib.pyplot as plt
from scipy import stats

df = pd.read_csv("media/planetes.csv", skiprows = 96)
df.head(7)


# %%
"""
df.plot.hist(df["disc_year"], by =  df["discoverymethod"].unique())

#on crée les colonnes avec le boléen la planète est découverte par la méthode
discov = df["discoverymethod"].unique()
year = df["disc_year"].unique()
for i, meth in enumerate(discov):
    df[meth] = np.zeros(df.shape[0], dtype=int) 
    df.loc[df["discoverymethod"]==meth, meth] = 1
df = df.set_index("disc_year")
pd.DataFrame("disc_year", columns = meth, stacked = True).plot.bar()
"""
df.hist("disc_year", cumulative = True)

# %%

# %%
