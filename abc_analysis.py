import pandas as pd

def get_part_indexes(cum_pers, left_threshold_per, right_threshold_per):
    cum_pers = cum_pers.round(decimals=1)
    cum_pers_right = cum_pers[cum_pers <= right_threshold_per]
    cum_pers_result = cum_pers_right[cum_pers_right > left_threshold_per]
    part_indexes = cum_pers_result.index.values
    return part_indexes


def to_analyze(data, per_a, per_b, per_c):
    total_value = data.sum()
    percents = data / total_value * 100.0
    cum_percents = percents.cumsum()
    percents = pd.concat([data, pd.concat([percents, cum_percents], axis=1)], axis=1)

    a_indexes = get_part_indexes(cum_percents, 0.0, per_a)
    a = data.loc[a_indexes]

    b_indexes = get_part_indexes(cum_percents, per_a, per_b)
    b = data.loc[b_indexes]

    c_indexes = get_part_indexes(cum_percents, per_b, per_c)
    c = data.loc[c_indexes]
    return total_value, percents, a, b, c


df = pd.read_csv("all.csv")

print(df.columns)
print(df.head())

df_column = df['MarginShelvesDay']

print(df_column)

total_value, percents, a, b, c = to_analyze(df_column, 80, 95, 100)


print(df['Nomenclature'][a.index.values])
print(df['Nomenclature'][b.index.values])
print(df['Nomenclature'][c.index.values])