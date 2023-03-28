import pandas as pd
import rdfizer
import csv


def calculate_overrep_per_dataset(
    value_counts: pd.Series,
    thr: float
) -> pd.DataFrame:
    """Calculates overrepresentation for the whole dataset defined as the number
    of entities that show a count higher than the specified quantile.

    :param value_counts: The counts for all the given instances.
    :type value_counts: pd.Series
    :param thr: The threshold percentage to define overrepresentation.
    :type thr: float
    :returns: The calculated overrepresentation for all instances.
    :rtype: pd.DataFrame
    """
    quantile = value_counts.quantile(q=thr)

    metric = len(value_counts[value_counts >= quantile])

    return {"Overrepresentation": metric}


def calculate_overrep_per_instance(
    value_counts: pd.Series,
    thr: float
) -> pd.DataFrame:
    """Calculates overrepresentation for each instance defined as a boolean indicating whether such instance appears a number of times more
    than or equal to the value of the specified quantile.

    :param value_counts: The counts for all the given instances.
    :type value_counts: pd.Series
    :param thr: The threshold percentage to define overrepresentation.
    :type thr: float
    :returns: The calculated overrepresentation for all instances.
    :rtype: pd.DataFrame
    """
    quantile = value_counts.quantile(q=thr)

    # Format value counts
    value_counts = value_counts\
        .reset_index(drop=False)\
        .rename(columns={
            value_counts.name: "RawCounts",
            "index": value_counts.name
        })

    # Add metadata
    value_counts["MeasureID"] = 2
    value_counts["MeasureName"] = "Overrepresented"
    value_counts["MeasureThreshold"] = thr
    value_counts["MeasureThresholdCounts"] = quantile

    # Calculate metric
    value_counts["MeasureValue"] = None
    value_counts.loc[
        (value_counts["RawCounts"] >= quantile),
        "MeasureValue"
    ] = True
    value_counts.loc[
        (value_counts["RawCounts"] < quantile),
        "MeasureValue"
    ] = False

    return value_counts


def calculate_overrep(
    value_counts: pd.Series,
    thr: float,
    out_format: str = "dataset"
) -> pd.DataFrame:
    """Wrapper for calculating overrepresentation for either the whole dataset
    or per instance.

    :param value_counts: The counts for all the given instances.
    :type value_counts: pd.Series
    :param thr: The threshold percentage to define overrepresentation.
    :type thr: float
    :returns: The calculated overrepresentation for all instances.
    :rtype: pd.DataFrame
    """
    results = None

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


def calculate_enrichment(
    x: float,
    q_thr: float
) -> float:
    """Calculates enrichment as the percentage of change between the instance
    counts and the counts for the specified threshold.

    For x < q_thr, the result is a negative percentage (it is not enriched).
    For x > q_thr, the percentage is positive and, thus, the instance shows enrichment over the given threshold.

    For example, for x=190 counts and q_thr=150 counts, the instance will have an enrichment of: 100 * (190 - 150) / 150 = 26.67

    On the other hand, for x=90 counts and q_thr=150 counts, the instance will
    have a enrichment of: 100 * (90 - 150) / 150 = -40

    :param x: The counts for the given instance.
    :type x: float
    :param q_thr: The counts corresponding to the quantile threshold.
    :type q_thr: float
    :returns: The enrichment percentage.
    :rtype: float
    """
    return 100 * (x - q_thr) / q_thr


def calculate_enrichment_per_instance(
    value_counts: pd.Series,
    thr: float
) -> pd.DataFrame:
    """Calculates overrepresentation for each instance.

    :param value_counts: The counts for all the given instances.
    :type value_counts: pd.Series
    :param thr: The threshold percentage to define enrichment.
    :type thr: float
    :returns: The calculated enrichment for all instances.
    :rtype: pd.DataFrame
    """
    # Get actual value for quantile threshold
    quantile = value_counts.quantile(q=thr)

    # Format value counts
    value_counts = value_counts\
        .reset_index(drop=False)\
        .rename(columns={
            value_counts.name: "RawCounts",
            "index": value_counts.name
        })

    # Add metadata
    value_counts["MeasureID"] = 1
    value_counts["MeasureName"] = "Enrichment"
    value_counts["MeasureThreshold"] = thr
    value_counts["MeasureThresholdCounts"] = quantile

    # Calculate metric
    value_counts["MeasureValue"] = value_counts["RawCounts"].apply(
            lambda x: calculate_enrichment(
                x=x,
                q_thr=quantile
            )
        )

    return value_counts


def execute_rdfizer(mapping_file, data, output_file):
    triples_map_list = rdfizer.mapping_parser(mapping_file)
    base = rdfizer.extract_base(mapping_file)
    with open(output_file, "w", encoding = "utf-8") as output_file_descriptor:
        for tp in triples_map_list:
            rdfizer.semantify_file(tp, triples_map_list, ",", output_file_descriptor, data)


if __name__ == "__main__":
    data_df = pd.read_csv("newsuser.csv")

    # Calculate overrepresentation per instance
    overrep_df = calculate_overrep(
        value_counts=data_df["NewsID"].value_counts(),
        thr=0.90,
        out_format="instance"
    )

    # Calculate overrepresentation for the whole dataset
    # print(
    #     calculate_overrep(
    #         value_counts=data_df["NewsID"].value_counts(),
    #         thr=0.90,
    #         out_format="dataset"
    #     )
    # )

    # Calculate enrichment per instance
    # print(
    #     calculate_enrichment_per_instance(
    #         value_counts=data_df["NewsID"].value_counts(),
    #         thr=0.90
    #     )
    # )

    # Calculate enrichment per instance for users
    # print(
    #     calculate_enrichment_per_instance(
    #         value_counts=data_df["SharedByUser"].value_counts(),
    #         thr=0.90
    #     )
    # )

    # Change name of user field in the results (change original column)
    # data_df = data_df.rename(columns={"SharedByUser": "UserID"})

    enrichment_df = calculate_enrichment_per_instance(
        value_counts=data_df["NewsID"].value_counts(),
        thr=0.90
    )

    # IMPORTANT: format as dictionary for rdfizer
    enrichment_dict = enrichment_df.to_dict(orient="records")

    mapping = "mappingbias.ttl"
    output = "output.nt"

    execute_rdfizer(
        mapping_file=mapping,
        data=enrichment_dict,
        output_file=output
    )
