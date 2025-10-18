import os
from pprint import pprint

import vk_api as vk
from dotenv import load_dotenv

load_dotenv()

VK_ACCESS_TOKEN = os.getenv("VK_ACCESS_TOKEN")

session = vk.VkApi(token=VK_ACCESS_TOKEN)

vk = session.get_api()
posts = vk.wall.get(domain="beluniversity", count=5)

pprint(posts)
