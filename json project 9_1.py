import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

infile = open("US_fires_9_1.json", "r")
outfile = open("9-1_data.json", "w")
fires = json.load(infile)
json.dump(fires, outfile, indent=4)

f = [x for x in fires if x ["brightness"] > 450]
brightns=[x["brightness"] for x in f]

lat = [x["latitude"] for x in f]
lon = [x['longitude'] for x in f]

data = [
    {
        "type": "scattergeo",
        "lon": lon,
        "lat": lat,
        "text": brightns,
        "marker": {
            "size": [.05 * b for b in brightns],
            "color": brightns,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Brightness"}}}]

layout = Layout(title = "US Fires - 9/1/2020 through 9/13/2020")
figure = {"data": data, "layout": layout}

offline.plot(figure, filename = "USFIRES91913.html")

print(brightns)
print(lon)
