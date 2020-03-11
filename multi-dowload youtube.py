try:
    from pytube import YouTube, Playlist
    
except:
    print("Error: Librerias del sistem no se encuentran instaladas")
    exit()

opcion=int(input("1)Crear y Descargar\n2)Descargar Directamente\nOpcion:"))
if(opcion==1):
    w=0
    while(w==0):
        pl=input("Ingrese Url playlist completa:")
        try:
            playlist = Playlist(pl)
            w=1

        except:
            print("Url ingresada de manera incorrecta, por favor vuelva a intentarlo")
            w=0
        
    print('Number of videos in playlist: %s' % len(playlist.video_urls))

    urls=[]
    for url in playlist.video_urls:
        urls.append((url+"\n"))

    lista=open("video-list.txt", "w+")
    lista.writelines(urls)
    lista.close()

    opcion=2
    
if(opcion==2):
    videos=[]
    cant=0

    lista=open("video-list.txt", "r")
    lines=lista.readlines()
    j=len(lines)
    for linea in lines:
        cant+=1
        videos.append(linea)
    lista.close()
    for url in videos:
        try:
            YouTube(url).streams.first().download()
            cant-=1
            print("Cantidad de videos restantes: ", cant)

        except:
            print("El programa a fallado, por favor reinicie la aplicacion")
            for i in range(cant, len(videos)):
                vs.append(((videos[i])+"\n"))

            lista=open("video-list.txt", "w")
            lista.writelines(urls)
            lista.close()
                
