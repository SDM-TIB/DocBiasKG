import pandas as pd


def calculate_overrep_per_dataset(
    value_counts: pd.Series,
    thr: float
) -> dict:
    quantile = value_counts.quantile(q=thr)

    metric = len(value_counts[value_counts >= quantile])

    return {"Overrepresentation": metric}
    

def calculate_enrichment(
    x: float,
    q_thr: float
) -> float:
    return 100 * (1 - x/q_thr)


def calculate_enrichment_per_instance(
    value_counts: pd.Series,
    thr: float
) -> dict:
    # Get actual value for quantile threshold
    quantile = value_counts.quantile(q=thr)

    # Calculate % of enrichment for each category
    enrichment = value_counts.apply(
            lambda x: calculate_enrichment(
                x=x,
                q_thr=quantile
            )
        )\
        .reset_index(drop=False)
    enrichment.columns = [
        enrichment.columns[-1],
        "Enrichment"
    ]

    return {"Enrichment": enrichment.to_dict(orient="records")}


def calculate_overrep_per_instance(
    value_counts: pd.Series,
    thr: float
) -> dict:
    quantile = value_counts.quantile(q=thr)

    # Reformat data
    value_counts = value_counts\
        .reset_index(drop=False)
    value_counts.columns = [
        value_counts.columns[-1],
        "Counts"
    ]

    # Calculate metric
    value_counts["Overrepresented"] = None
    value_counts.loc[
        (value_counts["Counts"] >= quantile),
        "Overrepresented"
    ] = "Yes"
    value_counts.loc[
        (value_counts["Counts"] < quantile),
        "Overrepresented"
    ] = "No"

    value_counts = value_counts\
        .drop("Counts", axis=1)

    return {"Overrepresentation": value_counts.to_dict(orient="records")}


def calculate_overrep(
    series: pd.Series,
    thr: float,
    out_format: str = "dataset"
) -> dict:
    results = None
    value_counts = series.value_counts()

    if out_format == "dataset":
        results = calculate_overrep_per_dataset(
            value_counts=value_counts,
            thr=thr
        )

    elif out_format == "instance":
        results = calculate_overrep_per_instance(
            value_counts=value_counts,
            thr=thr
        )

    else:
        raise NotImplementedError

    return results


if __name__ == "__main__":
    data_df = pd.read_csv("newsuser.csv")

    print(
        calculate_enrichment_per_instance(
            value_counts=data_df["NewsID"].value_counts(),
            thr=0.90
        )
    )
