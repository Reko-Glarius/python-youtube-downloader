try:
    from pytube import YouTube, Playlist
    from os import mkdir, getcwd

except:
    print("Error: Librerias del sistem no se encuentran instaladas")
    exit()

### Funciones
def option1():
    w=0

    while(w==0):
        pl=input("Ingrese Url playlist completa:")
        try:
            playlist=Playlist(pl)
            w=1

        except:
            print("Url ingresada de manera incorrecta, por favor vuelva a intentarlo")
            w=0
    print("Numero de videos añadidos:", len(playlist.video_urls))

    urls=[]
    for url in playlist.video_urls:
        urls.append((url))

    lista=open("video-list.txt", "w+")
    lista.writelines(urls)
    lista.close()

def option2():
    try:
        mkdir("Videos")
    except:
        pass

    ap=getcwd()
    videos = []
    lista = open("video-list.txt", "r")
    lines = lista.readlines()
    lista.close()

    for linea in lines:
        videos.append(linea)

    cant=len(videos)
    while(len(videos)!=0):
        urls=[]
        for url in videos:
            try:
                YouTube(url).streams.first().download(ap+'/Videos')
                cant-=1
                print("Cantidad de videos restantes: ", cant)

            except:
                print("--")
                if(url=="" or (url in urls)):
                    pass
                else:
                    print("El programa a fallado, por favor reinicie la aplicacion")
                    urls.append(url)
                    cant+=1
        videos=urls

### Main
def main():
    opcion=int(input("1)Añadir video\n2)Descargar videos enlistados\nOpcion:"))
    if(opcion==1):
        option1()
    elif(opcion==2):
        option2()
    else:
        print("Opcion ingresada no valida.")


if __name__=="__main__":
    main()