import json

text_messages_clean = []

with open(r"posts.json") as file:
    for line in file.readlines():
        wall = json.loads(line)

        parsed_response = json.JSONDecoder().decode(json.dumps(wall))
        nodes = []
        for key, value in parsed_response.items():
            nodes.append(value.get("items"))

        for node in nodes:
            for post in node:
                if post.get("type") == "ads":
                    continue
                text_messages_clean.append(post.get("text"))



words = {}

for message in text_messages_clean:
    if message is None:
        print(message)
        continue
    for word in message.split():
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1

words = dict(sorted(words.items(), key=lambda item: item[1], reverse=True))

for word in words:
    print(f"{word} - {words[word]}")