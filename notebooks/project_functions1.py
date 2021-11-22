import pandas as pd
import numpy as np

def load_and_process(filing_counts):
    df = (
        pd.read_csv('filing_counts.csv')   
<<<<<<< HEAD
        .drop('for_total',axis=1)
        .drop('case_action',axis=1)
        .drop('year', axis=1)
        .assign(state_agegroup=lambda x: x['age_group']+x['state'])
)
    return df
=======
    )
    df1 =(
        df
        .drop('for_total',axis=1)
        .drop('case_action',axis=1)
        .assign(state_agegroup=lambda x: x['age_group']+x['state'])
    )

    return df
>>>>>>> 934944162d38fda218199cad19bbb69c0112a4b1
