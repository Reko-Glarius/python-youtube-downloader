try:
    from pytube import YouTube, Playlist
    from os import mkdir, getcwd
    from re import compile

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
            playlist._video_regex=compile(r"\"url\":\"(/watch\?v=[\w-]*)")
            w=1

        except:
            print("Url ingresada de manera incorrecta, por favor vuelva a intentarlo")
            w=0
    print("Numero de videos añadidos:", len(playlist.video_urls))

    urls=[]
    for url in playlist.video_urls:
        urls.append((url+"\n"))

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
                cant-=1
                YouTube(url).streams.first().download(ap+'/Videos')
                print("Cantidad de videos restantes: ", cant)

            except:

                print("Descarga del video a fallado; registrando y procediendo al siguiente")
                urls.append(url)
                cant+=1
        videos=[]

    lista = open("video-list.txt", "w")
    lista.writelines(urls)
    lista.close()

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