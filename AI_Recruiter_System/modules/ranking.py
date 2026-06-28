import pandas as pd


def rank_candidates(candidates):

    df = pd.DataFrame(candidates)

    df = df.sort_values(
        by="ATS Compatibility Score",
        ascending=False
    ).reset_index(drop=True)

    df.insert(0, "Rank", range(1, len(df) + 1))

    return df