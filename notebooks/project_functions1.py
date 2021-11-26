import pandas as pd
import numpy as np

#Method Chain 1
def load_and_process(filing_counts):
    df = (
        pd.read_csv('filing_counts.csv')   
        .drop('for_total',axis=1)
        .drop('case_action',axis=1)
        .drop('year', axis=1)
        .assign(state_agegroup=lambda x: x['age_group']+x['state'])
        .drop_duplicates(inplace=True)
)
    return df
   
#Method Chain 2