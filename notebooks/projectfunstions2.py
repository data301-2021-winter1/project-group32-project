import pandas as pd
df = pd.read_csv('filing_counts.csv')
def load_and_process(filing_counts):
    df = (
        pd.read_scv('filing_counts.csv')
        .drop('for_total',axis=1)
        .drop('case_action',axis=1)
        .assign(case_type_state=lambda x: x['case_type']+x['state'])
    )
    return df

df