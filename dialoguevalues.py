import json

def metadata_analysis(dialogues):
    characters = set()

    for dialogue_list in dialogues:
        for dialogue in dialogue_list:
            sender = dialogue["sender"]
            characters.add(sender)

    total_characters = len(characters)
    total_exchanges = sum(len(dialogue_list) for dialogue_list in dialogues)

    print("Metadata Analysis:")
    print(f"Total characters: {total_characters}")
    print(f"Total conversational exchanges: {total_exchanges}")

def main():
    # Read JSON file
    with open('dialogue.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Extract dialogues
    dialogues = [dialogue["dialog"] for dialogue in data]

    # Analyze metadata
    metadata_analysis(dialogues)

if __name__ == "__main__":
    main()
