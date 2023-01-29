import httpx
from colorama import Fore

url = 'https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt'

resp = httpx.get(url)

mena = input(Fore.MAGENTA + 'Vyberte měnu ze které chcete konvertovat: ').upper()

kurz = False
for i in resp.text.split('\n'):
    if mena in i:
        kurz = float(i.split('|')[-1].replace(',', '.')) / int(i.split('|')[2])
        break
else:
    print(Fore.RED + f'K měně {mena} nemáme informace.')

if kurz:
    obnos = int(input(Fore.MAGENTA + f'Obnos {mena}: '))
    print(Fore.LIGHTBLUE_EX + f'\n{obnos} {mena} => {round(obnos * kurz, 3)} CZK')
