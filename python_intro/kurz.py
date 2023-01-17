import httpx

url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"

resp = httpx.get(url)

for i in resp.text.split("\n"):
    if "EUR" in i:
        print("Kurz eura je: " + i.split('|')[-1])