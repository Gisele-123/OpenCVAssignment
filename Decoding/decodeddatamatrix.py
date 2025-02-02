from pylibdmtx.pylibdmtx import decode
import cv2


image = cv2.imread("image2.jpg", cv2.IMREAD_GRAYSCALE) 


decoded_image = decode(image)

for obj in decoded_image:
    data = obj.data.decode("utf-8")
    print("Decoded Data:", data)


out_file = "decoded_datamatrix.png"
cv2.imwrite(out_file, image)
print(f" Annotated image saved as {out_file}")

cv2.imshow("Barcode with Annotation", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
