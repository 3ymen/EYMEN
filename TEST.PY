meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey" ,
            "LOL": "Komik bir şeye verilen cevap",
            "CREEPY": "korkunç",
            "AGGRO": "agresifleşmek/sinirlenmek",
            "SHEESH": "onaylamamakCREEPY - korkunç",
            "AGGRO": "agresifleşmek/sinirlenmek" 
            }
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
if word in meme_dict.keys():
    print(meme_dict[word])
    # Kelime eşleşiyorsa ne yapmalıyız?
else:   
    print("Böyle Bir Kelime Yok")
    # Kelime eşleşmiyorsa ne yapmalıyız?
