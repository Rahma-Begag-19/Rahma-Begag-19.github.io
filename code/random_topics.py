import random

with open("./topics.txt", "r", encoding="utf-8") as file:
    topics = file.readlines()

# Remove empty lines and newline characters
topics = [topic.strip() for topic in topics if topic.strip()]

# Pick a random topic
random_topic = random.choice(topics)

print(random_topic)