import base64
import requests
import traceback
import urllib.parse as ul

# It's possible to make requests without the api key, but the number of requests is very limited

url = "https://www.google.com/maps/@9.9950524,76.2921638,21z/data=!5m1!1e1"
urle = ul.quote_plus(url)
image_path = "google.jpg"

#key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
strategy = "desktop" # "mobile"
u = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?strategy={strategy}&url={urle}"

try:
    j = requests.get(u).json()
    ss_encoded = j['lighthouseResult']['audits']['final-screenshot']['details']['data'].replace("data:image/jpeg;base64,", "")
    ss_decoded = base64.b64decode(ss_encoded)
    with open(image_path, 'wb+') as f:
        f.write(ss_decoded)
except :
    print(traceback.format_exc())
    exit(1)