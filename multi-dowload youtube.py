from pytube import YouTube, Playlist

opcion=int(input("1)Crear y Descargar\n2)Descargar Directamente\nOpcion:"))
if(opcion==1):
    pl=input("Ingrese Url playlist completa:")
    playlist = Playlist(pl)
    print('Number of videos in playlist: %s' % len(playlist.video_urls))

    urls=[]
    for url in playlist.video_urls:
        urls.append((url+"\n"))

    lista=open("video-list.txt", "w")
    lista.writelines(urls)
    lista.close()

    opcion=2
    
if(opcion==2):
    videos=[]
    cant=0

    lista=open("video-list.txt", "r")
    lines=lista.readlines()
    for linea in lines:
        cant+=1
        videos.append(linea)
    lista.close()
    for url in videos:
        YouTube(url).streams.first().download()
        cant-=1
        print("Cantidad de videos restantes: ", cant)
