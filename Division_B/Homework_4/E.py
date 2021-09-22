message_count = int(input())
message_tree = {}

for message_id in range(1, message_count + 1):
    message_tree[message_id] = {}

    message_link = int(input())
    message_tree[message_id]['message_link'] = message_link

    if message_link == 0:
        message_topic = input()
        message_tree[message_id]['message_topic'] = message_topic
        message_tree[message_id]['links_count'] = 1
    else:
        while message_link != 0:
            prev_link = message_link
            message_link = message_tree[message_link]['message_link']
        message_tree[prev_link]['links_count'] += 1

    # don't need topic text at all
    _ = input()

topics = {(value['links_count'], message_count - key): value['message_topic']
          for key, value in message_tree.items()
          if value['message_link'] == 0}

print(topics[sorted(topics.keys(), reverse=True)[0]])
