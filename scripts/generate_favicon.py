from PIL import Image, ImageDraw

def generate_square_favicons():
    # Open source image
    src_path = 'public/skull_glow.jpg'
    img = Image.open(src_path).convert('RGB')
    w, h = img.size
    
    # Center crop / fit the skull and red glow on a square white canvas
    # Glow region is roughly between x=256 and x=2209 (width ~1953)
    center_x = (256 + 2209) // 2
    glow_w = 2209 - 256
    glow_h = 1684 - 78
    side = int(max(glow_w, glow_h) * 1.05)
    
    strip_x0 = max(0, center_x - side // 2)
    strip_x1 = min(w, strip_x0 + side)
    strip = img.crop((strip_x0, 0, strip_x1, h))
    
    # Pure white background canvas
    square_img = Image.new('RGB', (side, side), (255, 255, 255))
    offset_y = (side - h) // 2
    square_img.paste(strip, (0, offset_y))
    
    # Apply supersampled circular mask so corners are transparent (round favicon)
    scale = 4
    mask_hi = Image.new('L', (side * scale, side * scale), 0)
    draw = ImageDraw.Draw(mask_hi)
    draw.ellipse((0, 0, side * scale - 1, side * scale - 1), fill=255)
    mask = mask_hi.resize((side, side), Image.Resampling.LANCZOS)

    round_img = square_img.convert('RGBA')
    round_img.putalpha(mask)
    
    # Generate multi-size favicon.ico (16, 32, 48, 64)
    ico_sizes = [(16, 16), (32, 32), (48, 48), (64, 64)]
    ico_frames = [round_img.resize(s, Image.Resampling.LANCZOS) for s in ico_sizes]
    
    # Save favicon.ico
    ico_frames[0].save(
        'public/favicon.ico',
        format='ICO',
        sizes=ico_sizes,
        append_images=ico_frames[1:]
    )
    print("Saved public/favicon.ico with sizes:", ico_sizes)
    
    # Generate standard PNG favicons
    round_img.resize((32, 32), Image.Resampling.LANCZOS).save('public/favicon-32x32.png', 'PNG')
    round_img.resize((48, 48), Image.Resampling.LANCZOS).save('public/favicon-48x48.png', 'PNG')
    round_img.resize((192, 192), Image.Resampling.LANCZOS).save('public/favicon-192x192.png', 'PNG')
    round_img.resize((512, 512), Image.Resampling.LANCZOS).save('public/favicon.png', 'PNG')
    print("Saved round PNG favicons successfully.")

if __name__ == '__main__':
    generate_square_favicons()
