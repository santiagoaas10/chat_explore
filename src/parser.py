import re
import pandas as pd

# Expresión regular para extraer fecha, hora, remitente y mensaje
pattern = re.compile(r"\[(\d{2}/\d{2}/\d{2}), (\d{1,2}:\d{2}:\d{2}\s?[ap]\.m\.)\] (.*?): (.*)")
# Expresión regular para detectar marcas de tiempo dentro de los mensajes
embedded_timestamp_pattern = re.compile(r"\[\d{2}/\d{2}/\d{2}, \d{1,2}:\d{2}:\d{2}\s?[ap]\.m\.\] .*?:")

omitidos = ['<Multimedia omitido>', 'Este mensaje fue eliminado', 'You deleted this message', "imagen omitida", "video omitido", "audio omitido", "sticker omitido", "documento omitido", "gif omitido", "contacto omitido", "ubicación omitida", "cita omitida", "tarjeta de pago omitida", "archivo omitido", "voz omitida", "pegatina omitida", "tarjeta de evento omitida", "tarjeta de perfil omitida", "tarjeta de grupo omitida", "tarjeta de pago omitida", "tarjeta de ubicación omitida", "tarjeta de contacto omitida", "tarjeta de archivo omitida", "tarjeta de voz omitida", "tarjeta de pegatina omitida", "tarjeta de gif omitida", "tarjeta de documento omitida", "tarjeta de audio omitida", "tarjeta de video omitida", "tarjeta de imagen omitida", "tarjeta de mensaje omitida", "tarjeta de enlace", 'GIF omitido']



def parse_chat(filename):
    data = []
    
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            match = pattern.match(line)
            if match:
                date, time, sender, message = match.groups()
                timestamp = f"{date} {time}"
                data.append([timestamp, sender, message])
            elif data:
                if pattern.match(line.strip()):
                    data.append([None, None, line.strip()])  # Agregar como línea separada para revisión
                else:
                    data[-1][2] += " " + line.strip()
    
    df = pd.DataFrame(data, columns=['timestamp', 'sender', 'message'])
    df.dropna(subset=['timestamp'], inplace=True)  # Eliminar líneas incorrectamente añadidas

    return df

def clean_chat(df):
        # Filtrar mensajes que contienen marcas de tiempo incrustadas
    df['message'] = df['message'].apply(lambda x: embedded_timestamp_pattern.sub("", x).strip())
    
    df['message'] = df['message'].str.replace("\u200E", "", regex=True)


    df["message"] = df["message"].replace("|".join(omitidos),"", regex=True)
    df["message"] = df["message"].str.strip()

    return df


def save_chat(df, output_path):
    df.to_csv(output_path, index=False)
    print(f"chat guardado en {output_path}")



"""# Uso del script
df = parse_chat('_chat.txt')
#pd.set_option('display.max_colwidth', None)

print(df.head())
print("\n")

df["message"] = df["message"].replace("|".join(omitidos), "", regex=True)
df["message"] = df["message"].str.strip()
df.to_csv('chat.csv', index=False)
print(df.iloc[1:10,[1,2]])"""