from src.parser import parse_chat, clean_chat, save_chat
input_path='data/raw/_chat.txt'
output_path='data/processed/chat.csv'





print(f"chat guardado en {output_path}")

def main():
    print("cargando chat")
    df = parse_chat(input_path)
    print("limpiando datos")
    df = clean_chat(df)
    print("guardando chat")
    save_chat(df,output_path)

 
if __name__ == '__main__':
    main()