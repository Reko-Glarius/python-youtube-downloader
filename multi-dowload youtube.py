from pytube import YouTube, Playlist #Importacion de elementos de la libreria pytube y pytube3

opcion=int(input("1)Crear y Descargar\n2)Descargar Directamente\nOpcion:")) #Captura eleccion tomada

if(opcion==1): #Opcion 1, crea un archivo .txt con todas las url de todos los videos de la playlist
    pl=input("Ingrese Url playlist completa:")
    playlist = Playlist(pl)
    print('Number of videos in playlist: %s' % len(playlist.video_urls))

    urls=[]
    for url in playlist.video_urls: #For para almacenar las url, para luego almacenar en el .txt
        urls.append((url+"\n")) #Se añade un \n al final para mayor orden y control

    lista=open("video-list.txt", "w") #Apertura de archivo .txt
    lista.writelines(urls) #Almacenamiento en el .txt
    lista.close() #Cerrado y guardado de datos en .txt

    opcion=2 #Permite pasar inmediatamente a el apartado 2, descargar videos
    
if(opcion==2): #Opcion 2, en funcion de todas las urls de todos los videos de la playlist, va descargando cada video
    videos=[]
    cant=0

    lista=open("video-list.txt", "r") #Apertura de archivo .txt para obtencion de urls
    lines=lista.readlines() #Almacenamiento de urls
    for linea in lines: #Ciclo para almacenar todas las urls en el sistema
        cant+=1 #registra cantidad total de videos
        videos.append(linea)
        
    lista.close() #Cerrado de archivo de .txt
    
    for url in videos: #Ciclo para descargar videos url por url
        YouTube(url).streams.first().download() #Funcion para descargar video
        cant-=1
        print("Cantidad de videos restantes: ", cant) #Imprime por consola cuantos videos restan
