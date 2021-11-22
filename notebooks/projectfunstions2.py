import pandas as pd
def load_and_process(filing_counts):
    df = (pd.read_csv("filing_counts.csv")
          .drop("for_total",axis=1)
          .drop("case_action",axis=1)
          .drop("age_group",axis=1)
          .set_index('state')
         )
    return df
df.head()