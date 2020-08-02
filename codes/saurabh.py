from PIL import Image

def black_and_white_dithering(input_image_path,output_image_path,dithering=True):
	color_image = Image.open(input_image_path)
	if dithering:
		bw = color_image.convert('1')
	else:
		bw = color_image.convert('1',dither=Image.NONE)
	bw.save(output_image_path)



def main():
	try:
		img = Image.open("/Users/saurbane/Downloads/saurabh.jpeg")
		img.show()
		print("worked ")
		check="/Users/saurbane/Downloads/saurabh.jpeg"
		print("lets convert the image to black and white")
		destination_file = input("enter destination file name>")
		black_and_white_dithering(check,destination_file)
		
	except IOError:
		pass

main()