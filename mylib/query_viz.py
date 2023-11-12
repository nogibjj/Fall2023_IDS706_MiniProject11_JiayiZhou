"""
query and viz file
"""

from pyspark.sql import SparkSession
import matplotlib.pyplot as plt

# sample query
def query_transform():
    """
    Run a predefined SQL query on a Spark DataFrame.

    Returns:
        DataFrame: Result of the SQL query.
    """
    spark = SparkSession.builder.appName("Query").getOrCreate()
    query = (
        "SELECT AllTeams.team AS Team, COUNT(*) AS TotalMatchesPlayed "
        "FROM ( "
        "    SELECT team1 AS team FROM wwc_matches_1_delta "
        "    UNION ALL "
        "    SELECT team2 AS team FROM wwc_matches_1_delta "
        "    UNION ALL "
        "    SELECT team1 AS team FROM wwc_matches_2_delta "
        "    UNION ALL "
        "    SELECT team2 AS team FROM wwc_matches_2_delta "
        ") AS AllTeams "
        "GROUP BY Team "
        "ORDER BY TotalMatchesPlayed DESC"
    )
    query_result = spark.sql(query)
    return query_result

# sample viz for project
def viz():
    query = query_transform()
    count = query.count()
    if count > 0:
        print(f"Data validation passed. {count} rows available.")
    else:
        print("No data available. Please investigate.")

    df = query.toPandas()

    # Create a bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(
        df["Team"],
        df["TotalMatchesPlayed"],
        color="blue",
    )
    plt.xlabel("Team")
    plt.ylabel("Total Matches Played")
    plt.title("Total Matches Played by Team")
    plt.xticks(rotation=45)
    plt.show()

if __name__ == "__main__":
    query_transform()
    viz()
