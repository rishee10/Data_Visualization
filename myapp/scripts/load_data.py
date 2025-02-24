import json
from datetime import datetime
from django.utils.timezone import make_aware
from myapp.models import DataPoint

def load_json_data():
    with open('jsondata.json', encoding='utf-8') as file:
        data = json.load(file)
        for entry in data:
            try:
                # Extract datetime strings
                added_str = entry.get('added', '').strip()
                published_str = entry.get('published', '').strip()

                # Remove comma from date string
                added_str = added_str.replace(',', '')
                published_str = published_str.replace(',', '')

                # Convert only if the string is not empty
                added_dt = None
                published_dt = None

                if added_str:
                    try:
                        added_dt = make_aware(datetime.strptime(added_str, '%B %d %Y %H:%M:%S'))
                    except ValueError:
                        print(f"Skipping entry due to invalid added date: {entry}")

                if published_str:
                    try:
                        published_dt = make_aware(datetime.strptime(published_str, '%B %d %Y %H:%M:%S'))
                    except ValueError:
                        print(f"Skipping entry due to invalid published date: {entry}")

                # Save to database
                if added_dt is not None and published_dt is not None:
                    DataPoint.objects.create(
                        end_year=entry.get('end_year', ''),
                        intensity=entry.get('intensity', 0),
                        sector=entry.get('sector', ''),
                        topic=entry.get('topic', ''),
                        insight=entry.get('insight', ''),
                        url=entry.get('url', ''),
                        region=entry.get('region', ''),
                        start_year=entry.get('start_year', ''),
                        impact=entry.get('impact', ''),
                        added=added_dt,
                        published=published_dt,
                        country=entry.get('country', ''),
                        relevance=entry.get('relevance', 0),
                        pestle=entry.get('pestle', ''),
                        source=entry.get('source', ''),
                        title=entry.get('title', ''),
                        likelihood=entry.get('likelihood', 0)
                    )
                else:
                    print(f"Skipping entry due to missing or invalid date: {entry}")
            except Exception as e:
                print(f"Error processing entry: {entry}, Error: {e}")
