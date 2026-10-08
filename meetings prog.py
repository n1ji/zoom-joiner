import webbrowser
from pathlib import Path
from tkinter import Button, Label, Listbox, Tk

# Resolve links.txt next to this script so it works regardless of the working directory
LINKS_FILE = Path(__file__).resolve().parent / "links.txt"


def read_meetings(path):
    """Parse 'link;name' lines into a list of {'link', 'name'} dicts."""
    meetings = []
    try:
        with open(path, encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                link, sep, name = line.partition(";")
                if sep and link.strip() and name.strip():
                    meetings.append({"link": link.strip(), "name": name.strip()})
                else:
                    print(f"Warning: Skipping invalid line: {line}")
    except OSError as e:
        print(f"Error: Could not read '{path}': {e}")
    return meetings


def open_meeting(listbox, meetings):
    selection = listbox.curselection()
    if not selection:
        print("Please select a meeting to join.")
        return
    link = meetings[selection[0]]["link"]
    webbrowser.open(link)
    print(f"Opening meeting link: {link}")


def main():
    meetings = read_meetings(LINKS_FILE)
    if not meetings:
        print("No meeting data found in the file.")

    window = Tk()
    window.title("Zoom Meeting Joiner")

    Label(window, text="Select a Meeting:").pack()

    listbox = Listbox(window, height=20, width=50)
    listbox.pack()
    listbox.insert("end", *(m["name"] for m in meetings))
    listbox.bind("<Double-Button-1>", lambda event: open_meeting(listbox, meetings))

    Button(window, text="Join Meeting", command=lambda: open_meeting(listbox, meetings)).pack()
    Label(window, text="prog by plaui").pack()

    window.mainloop()


if __name__ == "__main__":
    main()
