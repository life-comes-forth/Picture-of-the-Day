import ExtractTransform
import Load
import logging

logging.basicConfig(filename = "apod_pipeline.log", level = logging.INFO)

try:
    apod_data = ExtractTransform.fetch_apod(ExtractTransform.requestDate)
    transformed_data = ExtractTransform.transform_apod(apod_data)
    Load.store_metadata(transformed_data)
    logging.info(f"Successfully processed APOD for {apod_data['date']}.")
except Exception as e:
    logging.error(f"Pipeline failed: {str(e)}")
