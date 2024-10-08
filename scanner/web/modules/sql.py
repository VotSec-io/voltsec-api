import urllib
import requests
import re
import urllib.parse
import asyncio
from pydantic import BaseModel

class Vernabilities(BaseModel):
      name: str
      description: str
      level: str
      remeditation: str



async def checkSqlInjection(url: str) -> bool:
    sqlPayloads = [
        "'", "' OR '1'='1", "' OR '1'='1' --", '"', '" OR "1"="1', '" OR "1"="1" --',
        ' OR 1=1', ' OR 1=1 --', ' OR 1=1#', ' OR 1=1/*']
    for payload in sqlPayloads:
        try:
            response = requests.get(url=url + urllib.parse.quote(payload))
            if re.search(r'error|syntax|database|sql', response, re.IGNORECASE):
                return True
        except:
            continue
    return False


# kafi dur tk codes files dekh li....
# atrangi chize dekhne ko mili hogi apko to😂😂

# but chalo aab razz batata hu G spot kaise hit kre.
# first of all unke belly ko, breast ko, neck ko, neck ke piche wale balo ko apna gulab bana lo itna kiss kro...
# fir jab niche aao novel me zoor sa kiss aur halki si bite do
# fir jab usse niche aao..
# Ayeeee Hyeeeee Tharki insan kitna dhyn se par rhaa hai
# find part 2 somewhere in this folder