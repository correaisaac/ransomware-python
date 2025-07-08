import os
import pyaes

# Nome da pasta a ser descriptografada
folder_name = "Arquivos Importantes"

# Chave de descriptografia (DEVE ser a mesma usada na criptografia)
key = b"12345678901234567890123456789012" #

# Inicializa o modo de operação do AES
aes = pyaes.AESModeOfOperationCTR(key) #

print(f"Iniciando a descriptografia da pasta: {folder_name}")

# Percorre todos os arquivos e subdiretórios da pasta especificada
for root, dirs, files in os.walk(folder_name):
    for file in files:
        # Verifica se o arquivo é um arquivo criptografado (.zukado)
        if file.endswith(".zukado"):
            file_path = os.path.join(root, file)

            # 1. Abrir e ler o arquivo criptografado
            with open(file_path, "rb") as f: #
                file_data = f.read() #

            # 2. Descriptografar os dados
            decrypted_data = aes.decrypt(file_data) #

            # 3. Definir o nome do arquivo original (removendo a extensão .zukado)
            original_file_name = os.path.splitext(file_path)[0] #
            
            # 4. Salvar o arquivo original descriptografado
            with open(original_file_name, "wb") as f: #
                f.write(decrypted_data) #

            print(f"Descriptografado: '{file_path}' -> '{original_file_name}'")

            # 5. Remover o arquivo criptografado
            os.remove(file_path) #

print("\nDescriptografia concluída com sucesso!")