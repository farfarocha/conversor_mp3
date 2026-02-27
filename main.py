from moviepy import AudioFileClip
import os

def converter_para_mp3(arquivo_origem):
    # Gera o nome do arquivo de saída trocando a extensão para .mp3
    arquivo_destino = os.path.splitext(arquivo_origem)[0] + ".mp3"
    
    try:
        print(f"Convertendo {arquivo_origem}...")
        
        # Carrega o áudio (funciona com .opus, .wav, .m4a, etc.)
        audio = AudioFileClip(arquivo_origem)
        
        # Salva como mp3
        # Usando qualidade variável (0 é a melhor, 9 é a menor - 4 é um ótimo equilíbrio)
        audio.write_audiofile(arquivo_destino, codec="libmp3lame", ffmpeg_params=["-q:a", "4"])
        
        # É importante fechar o arquivo para liberar a memória
        audio.close()
        
        print(f"Sucesso! Arquivo salvo em: {arquivo_destino}")
        
    except Exception as e:
        print(f"Erro na conversão: {e}")


if __name__ == '__main__':
    # Teste com seu arquivo opus
    converter_para_mp3("arquivo.aac")