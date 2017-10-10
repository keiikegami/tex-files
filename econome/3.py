import numpy as np
import pandas as pd
np.random.seed(123)
pop = 1000
time = 3

# (a) data set
v = np.random.normal(0,1, pop*time)
alpha = np.random.normal(0,1, pop)
alphas = np.array([alpha]*time).flatten()
u_1 = np.random.normal(0,1, pop*time)
u_2 = np.random.normal(0,1, pop*time)
x_1 = alphas + u_1
x_2 = alphas + u_2
z = np.random.normal(0,1, pop)
zs = np.array([z]*time).flatten()
y = 1 + x_1 + x_2 + zs + alphas + v

df = pd.DataFrame({"y" : y,
                  "x_1" : x_1,
                  "x_2" : x_2,
                  "z" : zs,
                  "alpha" : alphas,
                  "v" : v})

df.to_csv("sample_data.csv")

# (d) data set
v = np.random.normal(0,1, pop*time)
alpha = np.random.normal(0,1, pop)
alphas = np.array([alpha]*time).flatten()
u_1 = np.random.normal(0,1, pop*time)
u_2 = np.random.normal(0,1, pop*time)
x_1 = alphas + u_1
x_2 = alphas + 0.1 * u_2
z = np.random.normal(0,1, pop)
zs = np.array([z]*time).flatten()
y = 1 + x_1 + x_2 + zs + alphas + v

df2 = pd.DataFrame({"y" : y,
                  "x_1" : x_1,
                  "x_2" : x_2,
                  "z" : zs,
                  "alpha" : alphas,
                  "v" : v})

df2.to_csv("sample_data2.csv")