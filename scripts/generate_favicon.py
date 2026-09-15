from PIL import Image

def generate_square_favicons():
    # Open source image
    src_path = 'public/minecraft.png'
    img = Image.open(src_path).convert('RGBA')
    w, h = img.size
    
    # Create square canvas with transparent background
    max_dim = max(w, h)
    square_img = Image.new('RGBA', (max_dim, max_dim), (0, 0, 0, 0))
    # Center image in square
    offset_x = (max_dim - w) // 2
    offset_y = (max_dim - h) // 2
    square_img.paste(img, (offset_x, offset_y))
    
    # Generate multi-size favicon.ico (16, 32, 48, 64)
    ico_sizes = [(16, 16), (32, 32), (48, 48), (64, 64)]
    ico_frames = [square_img.resize(s, Image.Resampling.LANCZOS) for s in ico_sizes]
    
    # Save favicon.ico
    ico_frames[0].save(
        'public/favicon.ico',
        format='ICO',
        sizes=ico_sizes,
        append_images=ico_frames[1:]
    )
    print("Saved public/favicon.ico with sizes:", ico_sizes)
    
    # Generate standard PNG favicons
    square_img.resize((32, 32), Image.Resampling.LANCZOS).save('public/favicon-32x32.png', 'PNG')
    square_img.resize((48, 48), Image.Resampling.LANCZOS).save('public/favicon-48x48.png', 'PNG')
    square_img.resize((192, 192), Image.Resampling.LANCZOS).save('public/favicon-192x192.png', 'PNG')
    square_img.resize((512, 512), Image.Resampling.LANCZOS).save('public/favicon.png', 'PNG')
    print("Saved PNG favicons successfully.")

if __name__ == '__main__':
    generate_square_favicons()
