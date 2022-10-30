from watchdog.events import FileSystemEventHandler
from pathlib import Path
import re

class FileTracking(FileSystemEventHandler):
    def on_created(self, event):
        file_name :str = Path(event.src_path).stem
        for letter in list(file_name):
            vowel_letter :re = re.match('а|о|у|ы|э|е|ё|и|ю|я|a|e|i|o|u|y', letter, re.IGNORECASE)
            consonant_letter :re = re.match('б|в|г|д|ж|з|й|л|к|н|м|с|п|р|ц|ф|ч|щ|ш|d|b|m|n|l|k|p|t|v|z|p|h', letter, re.IGNORECASE)

            if vowel_letter:
                print(letter.lower())
            elif consonant_letter:
                print(letter.upper())
