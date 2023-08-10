import pandas as pd

# read from CSV
df = pd.read_csv('/home/bishal.halder/unit_scripts/usg_usagebackoffice/cli/BRF/NORM/BRFAW2/UAW2M00A_NORM.csv')
# to concatenate all string columns 
def merge_string_columns(row):
    merged = ' '.join([str(x) for x in row if isinstance(x, str)])
    return merged

# apply the function to each row of the DataFrame
df['merged_column'] = df.apply(merge_string_columns, axis=1)

# display the result
print(df)
df.to_csv('06.csv', index=False)
