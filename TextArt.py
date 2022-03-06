from PIL import Image, ImageFont, ImageDraw

image = Image.new('RGB', (600, 600), (255, 255, 255))
font = ImageFont.truetype("D2Coding-Ver1.3.2-20180524-all.ttc", 12)
draw = ImageDraw.Draw(image)
draw.text((0, 0), "Hosung.Kim\nTest\nhi hi", fill="black", font=font)
image.save("test.png")