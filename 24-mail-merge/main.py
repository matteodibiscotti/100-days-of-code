
def main():
    with open("./Input/Letters/starting_letter.txt", mode="r") as data:
        body = data.read()
    with open("./Input/Names/invited_names.txt", mode="r") as names:
        recipients = names.readlines()
    for i in recipients:
        recipients[recipients.index(i)] = i.strip()
    for i in recipients:
        with open(f"./Output/ReadyToSend/{i}.txt", mode='w') as letter:
            content = body
            content = content.replace("[name]", i)
            letter.write(content)

if __name__ == "__main__":
    main()