import json
import os

import vk_api as vk
from dotenv import load_dotenv

load_dotenv()

VK_ACCESS_TOKEN = os.getenv("VK_ACCESS_TOKEN")

session = vk.VkApi(token=VK_ACCESS_TOKEN)

vk_api = session.get_api()

groups = vk_api.groups.get()
posts = {}

for group_id in groups["items"][:40]:
    posts[group_id] = vk_api.wall.get(owner_id=-group_id, count=5)

with open("posts.json", "w") as file:
    file.write(json.dumps(posts))

