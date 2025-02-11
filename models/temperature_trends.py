import pandas as pd
import logging

class TemperatureTrends:
    """handles temperature trend analysis"""

    @staticmethod
    def get_temperature_trends(df, country="Global", start_year=2000, end_year=2023):
        """computes basic statistics for temperature trends"""
        logging.info(f"Dataset columns: {df.columns}")
        if "Country" not in df.columns:
            return {"error": "Required column 'Country' is missing in dataset."}

        # reshape for testing
        year_columns = [col for col in df.columns if col.isdigit()]
        df_melted = df.melt(id_vars=["Country"], value_vars=year_columns, var_name="Year", value_name="Temperature")
        df_melted["Year"] = df_melted["Year"].astype(int)

        # year range f
        filtered_df = df_melted[(df_melted["Year"] >= start_year) & (df_melted["Year"] <= end_year)]

        # Filter by country
        if country != "Global":
            filtered_df = filtered_df[filtered_df["Country"] == country]

        # CHECK: if empty
        if filtered_df.empty:
            return {"error": "no data: check filters."}

        # stats
        stats = filtered_df["Temperature"].describe().to_dict()
        return stats