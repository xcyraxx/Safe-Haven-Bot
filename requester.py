import discord
import requests
from discord import Webhook, RequestsWebhookAdapter


webhook = Webhook.from_url("https://discord.com/api/webhooks/888510340311187526/ab6CZW5vcjI_q8qxhBIqZgbX_t-rVLzkGOZXnn5urt3CB6nPSrcpbMQEvVZeeQEWaE59", adapter=RequestsWebhookAdapter())
brr = discord.Embed(title="brr")