encodings = ['ansi', 'utf-8', 'utf-16','utf-16-le', 'utf-16-be', 'utf-32', 'euc-kr', 'cp949']

enc_text = open("C:\Users\hello\Downloads\ca4d6e857668c62b2cc37c6557b04192bab00d", "rb").read()#.split(b"\n")

dec_text = ""

for i in enc_text:
    
    for enc in encodings:

        try:
            if i[:3] == b'\x00\x00\x00':
                i = i.replace(b'\x00\x00\x00', b'')
            decode_str = i.decode(enc)
            dec_text += decode_str + "\n"
            break

        except UnicodeDecodeError:
            pass

print(dec_text)