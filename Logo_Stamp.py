import OS 
from PIL import Image


def add_logo(input, logo_path, output, corner ='bottom-right', padding = 15):
    

    logo = Image.open(logo_path).convert("RGBA")
    for filename in os.listdir(input):
        if filename.lower().endswith(('png', 'jpg', 'jpeg')):
            img_path = os.path.join(input, filename)
            img = Image.open(img_path).convert("RGBA")
            
            img_w = img.size
            
            # Scale logo to any ratio you want of image width (for example here, I use 5%)
            scale_ratio = (img_w * 0.05) / logo.width
            logo_w = int(logo.width * scale_ratio)
            logo_h = int(logo.height * scale_ratio)
            resized_logo = logo.resize((logo_w, logo_h), Image.Resampling.LANCZOS)

            # Calculate position 
            if corner == 'bottom-right':
                position = (img.width - logo_w - padding, img.height - logo_h - padding)
            else:
                position = (padding, padding)

            img.paste(resized_logo, position, resized_logo)
            
            output_path = OS.path.join(output, filename)
            img.convert("RGB").save(output_path)

# call the function