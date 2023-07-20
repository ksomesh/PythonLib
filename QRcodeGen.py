try:
    import qrcode
except ImportError:
   pip.main(['install', 'qrcode[pil]'])
   import qrcode

def generate_qrcode(text, filename="qrcode.png"):
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(text)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        img.save(filename)
        print(f"QR code generated and saved as {filename}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    user_input = input("Enter the text to encode in the QR code: ")
    generate_qrcode(user_input)
