import discord
import requests
from discord import Webhook, RequestsWebhookAdapter

str = str(input("Strink: "))
#https://discord.com/api/webhooks/891757387080429668/eWgDqZ-yQ4EpjGAjZHoapjl4OItagOwbHOL9cuytx8XOsLyrT3PeK7TpDR3XZ6B-GEhd = RA ND
webhook = Webhook.from_url("https://discord.com/api/webhooks/888510340311187526/ab6CZW5vcjI_q8qxhBIqZgbX_t-rVLzkGOZXnn5urt3CB6nPSrcpbMQEvVZeeQEWaE59", adapter=RequestsWebhookAdapter())
webhook.send(str)
print("Message sent!")
#ol