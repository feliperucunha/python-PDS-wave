
snd = Sound() 
snd.read('teste1.ogg') 
snd.play()

c = SnackCanvas() 
c.pack() 
c.create_waveform(0, 0, sound=snd) 

print("Tocando Música")




input("Pressione algo para sair")
sys.exit()