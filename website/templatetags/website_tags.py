from django import template
from blog.models import Post
import requests

register = template.Library()

@register.inclusion_tag('website/latestposts.html')
def latestposts(arg=3):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:arg]
    return {'posts':posts }

@register.inclusion_tag('website/cryptoinfo.html')
def cryptoinfo():
    r1= requests.get('https://coinlib.io/api/v1/coin?key=1789a141d49d72a1&symbol=LTC')
    r2= requests.get('https://coinlib.io/api/v1/coin?key=1789a141d49d72a1&symbol=XMR')
    r3= requests.get('https://coinlib.io/api/v1/coin?key=1789a141d49d72a1&symbol=XRP')
    r4= requests.get('https://coinlib.io/api/v1/coin?key=1789a141d49d72a1&symbol=ETH')
    r5= requests.get('https://coinlib.io/api/v1/coin?key=1789a141d49d72a1&symbol=BTC')

    l_price = r1.json()['price']
    l_day = float(r1.json()['delta_24h'])
    l_week = float(r1.json()['delta_7d'])

    m_price = r2.json()['price']
    m_day = float(r2.json()['delta_24h'])
    m_week = float(r2.json()['delta_7d'])

    r_price = r3.json()['price']
    r_day = float(r3.json()['delta_24h'])
    r_week = float(r3.json()['delta_7d'])

    e_price = r4.json()['price']
    e_day = float(r4.json()['delta_24h'])
    e_week = float(r4.json()['delta_7d'])

    b_price = r5.json()['price']
    b_day = float(r5.json()['delta_24h'])
    b_week = float(r5.json()['delta_7d'])

    return {
        'l_price':l_price,
        'l_day':l_day,
        'l_week':l_week,
        'm_price':m_price,
        'm_day':m_day,
        'm_week':m_week,
        'r_price':r_price,
        'r_day':r_day,
        'r_week':r_week,
        'e_price':e_price,
        'e_day':e_day,
        'e_week':e_week,
        'b_price':b_price,
        'b_day':b_day,
        'b_week':b_week,
    }
