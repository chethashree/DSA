import os
import time
from datetime import datetime
from PIL import ImageGrab
import xml.etree.ElementTree as ET

# Configuration# Change SAVE_DIR from "screenshots" to static/screenshots
SAVE_DIR = os.path.join("static", "screenshots")

#SAVE_DIR = "screenshots"
XML_FILE = "screenshot_log.xml"
CAPTURE_INTERVAL = 10  # seconds

# Create directory if it doesn't exist
os.makedirs(SAVE_DIR, exist_ok=True)

# Initialize XML if not present
def init_xml():
    if not os.path.exists(XML_FILE):
        root = ET.Element("screenshots")
        tree = ET.ElementTree(root)
        tree.write(XML_FILE)
    return ET.parse(XML_FILE)

# Log screenshot data to XML
def log_screenshot(filename, timestamp):
    tree = init_xml()
    root = tree.getroot()
    entry = ET.SubElement(root, "screenshot")
    ET.SubElement(entry, "filename").text = filename
    ET.SubElement(entry, "timestamp").text = timestamp
    tree.write(XML_FILE)

# Take screenshot and save it
def take_screenshot():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"screenshot_{timestamp}.png"
    path = os.path.join(SAVE_DIR, filename)
    img = ImageGrab.grab()
    img.save(path)
    log_screenshot(filename, timestamp)
    print(f"[✓] Screenshot saved: {filename}")

# Main loop
def main():
    print(f"[INFO] Starting automatic screenshot capture every {CAPTURE_INTERVAL} seconds...")
    while True:
        take_screenshot()
        time.sleep(CAPTURE_INTERVAL)

if __name__ == "__main__":
    main()
