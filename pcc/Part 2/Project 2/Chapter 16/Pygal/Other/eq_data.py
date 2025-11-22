from pathlib import Path
import json

path = Path("Desktop/eq_data.geojson")
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
	mag = eq_dict['properties']['mag']
	mags.append(mag)
	lon = float(eq_dict['geometry']['coordinates'][0])
	lat = float(eq_dict['geometry']['coordinates'][1])
	lons.append(lon)
	lats.append(lat)

print(mags[:10])
print(lons[:5])
print(lats[:5])


