import json

notes = dict()

def add_note(title, text):
    global notes
    notes[title] = text
    print("your note has been added")


def update_notes():
    global notes
    with open('notes.json', 'r') as file:
     notes = json.load(json_note)

def display_notes():
    updated_notes()
if len(notes) == 0:
    print("No notes yet")
else:
    for title, text in notes.items():
      print(f"{title}: {text}")

def delete_note(title):
        if title in notes.keys():
            del notes[title]
            print(f'The {title} note has been deleted')
        else:
            print('The note does not exist')

def save_note(title , text):
        with open("notes.json", "w") as file:
           json.dump(notes, file)

def main():
         while True:
             print("1. Add a note")
             print("2. View all notes")
             print("3. Delete a note")
             print("4. Exit")
             choice = input("Choose an action: ")
             if choice == "1":
                note_title = input("Enter the note title: ")
                note_text = input("Enter the note text: ")
                add_note(note_title, note_text)
                save_note()
             elif choice == "2":
                display_notes()
                save_note()
             elif choice == "3":
               update_notes()
               for title in notes.keys():
                print(title)
                title_to_del = input('Enter the note title to delete: ')
                delete_note(title_to_del)
                save_note()
             elif choice == "4":
              break
             else:
                print("Incorrect input. Please try again.")

main()
