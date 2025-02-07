import pandas as pd
import logging
from statsmodels.tsa.arima.model import ARIMA
from prophet import Prophet
from modules.context_manager import context_manager

logging.basicConfig(level=logging.INFO)

class ScenarioProjection:
    """class for projecting scenarios and predictive modeling"""
    
    @staticmethod
    def project_climate_scenario(df, country, variable="Temperature Change", forecast_years=10):
        """projects climate scenarios using time series"""
        if df is not None:
            try: 
                logging.info(f"Dataset columns: {df.columns}")

                # reshaping for testing
                year_columns = [col for col in df.columns if col.isdigit()]
                df_melted = df.melt(id_vars=["Country"], value_vars=year_columns, var_name="Year", value_name=variable)
                df_melted["Year"] = df_melted["Year"].astype(int)

                # LOG
                logging.info(f"Reshaped dataset: {df_melted.head()}")

                # filter by country
                df_filtered = df_melted[df_melted["Country"] == country]

                # LOG
                logging.info(f"filtered dataset by country: {df_filtered.head()}")

                # CHECK: filtered dataset empty
                if df_filtered.empty:
                    return "no data: check filters."

                # forecast
                df_filtered = df_filtered.dropna()
                df_filtered = df_filtered.sort_values("Year")
                
                logging.info(f"filtered dataset after dropna and sort: {df_filtered.head()}")
                
                # arima
                arima_mod = ARIMA(df_filtered[variable], order=(5,1,0))
                arima_fit = arima_mod.fit()
                arima_forecast = arima_fit.forecast(steps=forecast_years)
                
                # prophet
                df_prophet = df_filtered.rename(columns={"Year": "ds", variable: "y"})
                prophet_model = Prophet()
                prophet_model.fit(df_prophet)
                future = prophet_model.make_future_dataframe(periods=forecast_years, freq='Y')
                prophet_forecast = prophet_model.predict(future)[['ds', 'yhat']].tail(forecast_years)
                
                # context mgr
                forecast_results = {
                    "ARIMA": arima_forecast.tolist(),
                    "Prophet": prophet_forecast.to_dict(orient='records')
                }
                context_manager.store("climate_forecast", forecast_results)
                
                logging.info(f"generated climate projections for {country}.")
                return forecast_results

            except Exception as e:
                logging.error(f"error in forecasting: {str(e)}")
                return "forecasting failed."
        else:
            return "dataset not loaded."