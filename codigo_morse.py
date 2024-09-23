# Importação da biblioteca para interface do usuário
import tkinter as tk

# Dicionário com caracteres e seus valores correspondentes em código Morse
morse_code_dict = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
    'Z': '--..',  '0': '-----',  '1': '.----', '2': '..---', '3': '...--',
    '4': '....-',  '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',  ' ': '/'
}

def text_to_morse_code(text):
    text = text.upper()
    morse_code = []
    
    for char in text:
        if char in morse_code_dict:
            morse_code.append(morse_code_dict[char])
        else:
            morse_code.append('?')  # Caracteres desconhecidos pelo dicionário
    
    return ' '.join(morse_code)

def convert():
    user_input = input_text.get("1.0", tk.END).strip()
    morse_output = text_to_morse_code(user_input)
    output_text.delete("1.0", tk.END)  # Limpa a caixa de saída
    output_text.insert(tk.END, morse_output)

# Configuração da interface gráfica
root = tk.Tk()
root.title("Conversor de Texto para Código Morse")

# Widgets da GUI
input_label = tk.Label(root, text="Digite o texto:")
input_label.pack()

input_text = tk.Text(root, height=5, width=40)
input_text.pack()

convert_button = tk.Button(root, text="Converter", command=convert)
convert_button.pack()

output_label = tk.Label(root, text="Código Morse:")
output_label.pack()

output_text = tk.Text(root, height=5, width=40)
output_text.pack()

# Inicia o loop da interface gráfica
root.mainloop()