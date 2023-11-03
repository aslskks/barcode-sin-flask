import sys
from tkinter import messagebox
def main():
  import barcode
  from barcode.writer import ImageWriter
  from cv2 import imread, imshow, waitKey, destroyAllWindows
  number = input("ingresa 11 digitos: ")
  barcode_format = barcode.get_barcode_class("upc")
  my_barcode = barcode_format(number, writer=ImageWriter())
  inpus = input("ingresa nombre del barcode(sin .png o .jpg) (la imagen es generada en .png): ")
  my_barcode.save(inpus)
  image_path = f"{inpus}.png"
  image = imread(image_path)
  imshow('brcode imagen', image)
  waitKey(0)
  destroyAllWindows()
if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    sys.exit()
  except Exception as e:
    messagebox.showerror(title="generador de codigo de barras", message=f"{e}"
