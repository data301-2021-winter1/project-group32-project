import pandas as pd
def load_and_process(filing_counts):
    df = (
        pd.read_csv('filing_counts.csv')   
    )
    df1 =(
        df
        .drop('for_total',axis=1)
        .drop('case_action',axis=1)
        .assign(state_agegroup=lambda x: x['age_group']+x['state'])
    )

    return df