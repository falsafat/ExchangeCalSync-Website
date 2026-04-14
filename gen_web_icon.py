import sys
from PIL import Image

def process_icon():
    source_path = sys.argv[1]
    dest_path = "app-icon.png"
    
    img = Image.open(source_path)
    img = img.convert("RGBA")
    
    # Resize to 512x512 for web
    img = img.resize((512, 512), Image.Resampling.LANCZOS)
    
    img.save(dest_path, "PNG")
    print(f"Icon saved to {dest_path}")

if __name__ == "__main__":
    process_icon()
