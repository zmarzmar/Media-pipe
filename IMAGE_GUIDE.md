# Image Setup Guide

This guide will help you choose and prepare the perfect images for your tongue detection app!

## Required Images

You need **2 PNG images**:

1. **`apple.png`** - Displayed when tongue is NOT out (normal state)
2. **`appletongue.png`** - Displayed when tongue IS out (silly state)

Both images will automatically be resized to **960x720 pixels**, so any size works!

## Where to Find Images

### Option 1: Emoji Images

Find large emoji PNG files:

Websites:
- [Emojipedia](https://emojipedia.org/) - Click any emoji → Download PNG
- [Emoji.gg](https://emoji.gg/) - Large collection of emoji PNGs
- [Flaticon](https://www.flaticon.com/) - Free emoji and icon PNGs
- Google Images - Search "apple emoji png transparent"

Suggested combos:
- 🍎 Apple + 😛 Face with Tongue
- 😊 Happy Face + 🤪 Zany Face
- 🐶 Dog + 🥴 Woozy Face
- ⭐ Star + 💥 Explosion
- 👍 Thumbs Up + 🤘 Rock On

### Option 2: Meme Templates

Use popular meme formats:

Good sources:
- [Imgflip Meme Generator](https://imgflip.com/memetemplates) - Download blank templates
- [Know Your Meme](https://knowyourmeme.com/) - Browse and download memes
- Reddit (r/memes, r/dankmemes) - Save images (respect copyright!)

Suggested meme pairs:
- Drake Disapproving / Drake Approving
- Distracted Boyfriend (normal) / Distracted Boyfriend (exaggerated)
- This is Fine Dog (calm) / This is Fine Dog (fire)
- Stonks (normal) / Stonks (rising)

### Option 3: Create Your Own

Using Paint/Paint 3D (Windows):
1. Open Paint
2. Create a simple drawing or add text
3. Save as PNG
4. Create a second "silly" version

Using Canva (free online):
1. Go to [Canva.com](https://www.canva.com/)
2. Create a new design (960x720)
3. Add text, shapes, or images
4. Download as PNG
5. Create a matching "tongue out" version

Using GIMP (free software):
1. Download [GIMP](https://www.gimp.org/)
2. Create a 960x720 canvas
3. Design your images
4. Export as PNG

### Option 4: Personal Photos

Make it personal!

Ideas:
- Your pet looking normal + Your pet being silly
- A serious selfie + A funny face selfie
- Your favorite food + Same food with ketchup/sauce
- Before coffee / After coffee

How to prepare photos:
1. Take/find two photos (similar but different energy)
2. Crop to similar sizes
3. Save as PNG format

## Image Requirements

### Must Have:
- File format: **PNG** (.png extension)
- File names: **exactly** `apple.png` and `appletongue.png` (lowercase)
- Location: Same folder as `main.py`

### Recommended:
- High contrast images (easier to see)
- Bright colors (more fun)
- Similar themes (creates a good before/after effect)
- Square or landscape orientation (looks better when resized)

### Avoid:
- Very dark images (hard to see)
- Tiny images (will look pixelated when enlarged)
- Corrupted files (won't load)
- Copyrighted material (if sharing publicly)

## Step-by-Step: Download Example Images

Let's use emoji as an example:

### 1. Download apple.png (Normal State)

1. Go to [Emojipedia - Red Apple](https://emojipedia.org/red-apple)
2. Scroll down to a platform (e.g., "Apple" or "Google")
3. Right-click the large emoji image → "Save image as..."
4. Save as `apple.png` in your project folder

### 2. Download appletongue.png (Tongue Out State)

1. Go to [Emojipedia - Face with Tongue](https://emojipedia.org/face-with-tongue)
2. Choose your favorite style
3. Right-click → "Save image as..."
4. Save as `appletongue.png` in your project folder

### 3. Verify Files

Check that you have:
```
next/
├── main.py
├── apple.png          ← This file
├── appletongue.png    ← This file
└── ...
```

## Converting Other Formats to PNG

Have a JPG or other format? Convert it:

### Online (Easiest):
1. Go to [CloudConvert](https://cloudconvert.com/)
2. Upload your image
3. Select "PNG" as output format
4. Download the converted file

### Using Paint (Windows):
1. Open the image in Paint
2. File → Save As → PNG
3. Rename to `apple.png` or `appletongue.png`

### Using Preview (Mac):
1. Open the image in Preview
2. File → Export
3. Format: PNG
4. Save with correct name

## Testing Your Images

After adding images:

1. Run the app: `python3.11 main.py`
2. You should see `apple.png` in the "Meme Output" window
3. Stick your tongue out
4. The image should change to `appletongue.png`

If images don't load:
- Check filenames (must be exact)
- Check file format (must be .png)
- Check location (same folder as main.py)
- Try opening the PNG in an image viewer to verify it's valid

## Creative Ideas

Once you have it working, try these fun combinations:

### Themed Sets:
- **Food:** 🍕 Pizza → 🌮 Taco
- **Animals:** 🐱 Cat → 🦁 Lion
- **Weather:** ☀️ Sunny → ⛈️ Stormy
- **Emotions:** 😐 Neutral → 🤯 Mind Blown
- **Gaming:** 🎮 Controller → 🏆 Trophy

### Seasonal:
- **Halloween:** 🎃 Pumpkin → 👻 Ghost
- **Christmas:** 🎄 Tree → 🎅 Santa
- **Valentine's:** 💌 Love Letter → 💘 Cupid Arrow
- **Summer:** 🏖️ Beach → 🍦 Ice Cream

### Funny Reactions:
- **Mild → Spicy:** 🌶️ Pepper → 🔥 Fire
- **Calm → Panic:** 😌 Relieved → 😱 Screaming
- **Awake → Asleep:** ☕ Coffee → 😴 Sleeping

## Copyright Considerations

If you're sharing your project:

**OK to use:**
- Your own photos/drawings
- Public domain images
- Creative Commons (CC0) images
- Emoji (generally okay for personal/educational use)

**Ask permission or use differently:**
- Copyrighted memes (better to create your own)
- Celebrity photos
- Brand logos
- Professional photography

Safe sources for free images:
- [Unsplash](https://unsplash.com/) - Free high-quality photos
- [Pexels](https://www.pexels.com/) - Free stock photos
- [Pixabay](https://pixabay.com/) - Free images and illustrations

## Need Help?

Images not showing?
1. Check `main.py` output for error messages
2. Verify filenames are exactly `apple.png` and `appletongue.png`
3. Make sure files are in the correct directory
4. Try with simple emoji images first

Want different behavior?
- Edit `main.py` to change image names
- Add more images for different gestures (see TUTORIAL.md)
- Create a slideshow that cycles through images

Have fun creating!

