from rembg import remove

input_path = 'örnek.jpg'#silinmesini istediğiniz arkaplanı olan resim 
output_path = 'örnek1.png'#çıktı olarak verilecek isim giriniz

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)
