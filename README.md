# Zoom Joiner

A tiny desktop app that lists your online-class or meeting links and opens the one you pick in your browser with a single click. Built for teachers and students who join several Zoom (or Google Meet, Teams, etc.) calls a day.

## Features

- Simple window with a list of your meetings, pick one and press **Join Meeting**
- Meetings live in a plain text file, so there is no need to touch any code
- Works with any link, not only Zoom
- Teachers can share one `links.txt` with the whole class
- No dependencies beyond Python's standard library

## Requirements

- Python 3 with Tkinter (included with the standard Python installers for Windows and macOS; on some Linux distributions install `python3-tk`)

## Usage

1. Edit `links.txt`, one meeting per line, in the format `link;name`:

   ```text
   https://zoom.us/j/1234567890;Math, Monday 10:00
   https://meet.google.com/abc-defg-hij;Physics lab
   ```

2. Start the app from this folder:

   ```bash
   python "meetings prog.py"
   ```

3. Select a meeting and press **Join Meeting**.

Run the program from the folder that contains `links.txt`, since the file is looked up in the current directory.

## For teachers

Fill in `links.txt` with your class links and send the file to your students. They only need to replace their own `links.txt` with yours and the list updates.

## Issues

Something not working? Open an [issue](https://github.com/plaui228/zoom-joiner/issues).

## License

GPL-3.0, see [LICENSE](LICENSE).

Made by Plaui.
