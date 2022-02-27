import face_recognition as fr

def reconhece_face(url_foto):
    foto = fr.load_image_file(url_foto)
    rostos = fr.face_encodings(foto)
    if(len(rostos) > 0):
        return True, rostos
    
    return False, []

def get_rostos():
    rostos_conhecidos = []
    nomes_dos_rostos = []

    user1 = reconhece_face("./img/marcos.jpeg")
    if(user1[0]):
        rostos_conhecidos.append(user1[1][0])
        nomes_dos_rostos.append("Marcos")
    
    user2 = reconhece_face("./img/dani.jpeg")
    if(user2[0]):
        rostos_conhecidos.append(user2[1][0])
        nomes_dos_rostos.append("Daniel")

    user3 = reconhece_face("./img/gabriel.jpg")
    if (user3[0]):
        rostos_conhecidos.append(user3[1][0])
        nomes_dos_rostos.append("Gabriel")

    else:
        nomes_dos_rostos.append("Desconhecido")
    return rostos_conhecidos, nomes_dos_rostos
    