from aspose.barcode import barcoderecognition
reader = barcoderecognition.BarCodeReader("image1.jpg", barcoderecognition.DecodeType.ALL_SUPPORTED_TYPES)
results = reader.read_bar_codes()
for barcode in results:
    print(barcode.code_text)