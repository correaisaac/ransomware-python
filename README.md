# 🔐 Sistema de Criptografia de Arquivos (Ransomware Didático)

Este projeto foi desenvolvido como uma demonstração prática dos conceitos de criptografia simétrica aplicados à segurança de arquivos. Os scripts utilizam o algoritmo **AES (Advanced Encryption Standard)** em modo de operação **CTR (Counter)** para criptografar e descriptografar arquivos de forma eficiente.

- **Autor:** Isaac Corrêa de Oliveira
- **Disciplina:** Segurança da Informação

## 🚀 Como Funciona

O projeto é composto por dois scripts principais:

1.  `encrypt_folder.py`: Varre a pasta `Arquivos Importantes`, criptografa cada arquivo encontrado e salva a versão criptografada com a extensão `.zukado`. **O arquivo original é removido após a criptografia**.
2.  `decrypt_folder.py`: Procura por arquivos `.zukado` na mesma pasta, os descriptografa usando a chave correta e restaura os arquivos originais. **O arquivo criptografado é removido após a descriptografia**.

## 📋 Instruções de Uso

### 1. Pré-requisitos

Certifique-se de ter o Python instalado. Você também precisará da biblioteca `pyaes`. Instale-a com o seguinte comando:

```bash
pip install pyaes
```

### 2. Preparação

No mesmo local onde os scripts `encrypt_folder.py` e `decrypt_folder.py` estão salvos, tem uma pasta chamada Arquivos Importantes, coloque lá o que quer que seja criptografado

### 3. Execução

**Para Criptografar**

Execute o script de criptografia.
```bash
python encrypt_folder.py
```

**Para Descriptografar**

Execute o script de criptografia.
```bash
python decrypt_folder.py
```