import re
import urllib
import asyncio
import requests
import urllib.parse

# kabhi kabhi dil me khayal aata hai.. na jane kya rakha hai duniya dari me, ladki me...
# kas ye khayal hilane ke phele aa jata.

async def checkXXS(url: str) -> bool:
    xxs = [
        "<script>alert('XSS')</script>", 
        "<img src='x' onerror='alert(1)'>", 
        "<svg onload='alert(1)'>"
    ]
    for check in xxs:
        response = requests.get(url=url + urllib.parse.quote(check))
        try:
            if re.search(re.escape(check), response):
                return True
        except:
            continue
    return False


# wahhh! gspot ki itni talab ki yaha tk pooch gaye chalo dekh lo fir...

# fir in the pussy above the hole you will find something called "clit"
# aab chutiyo ke tara ye maat poochna clit kya hota hai google kr lo. 😑
# hole ke barabr uper dot sa hoga kush reh...
# usko aise touch kro jaise feather ho.. usko halka halka sa hilo 
# na zada tezz na zada halka... bohot aarm se taki usko pleasure mile

# lo bdsk hit kr liya gspot itna tk tumara nahi nikla to kr lena aage ka karikram