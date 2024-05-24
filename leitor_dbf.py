from dbfread import DBF

# Caminho para o arquivo .dbf
dbf_path = 'C:/Users/PREDATOR/Downloads/testeRais2009/RAIS01.DBF'

# Prefixo para os arquivos de saída
output_prefix = 'D:/saidaDBF/RAIS01.TXT'

# Número máximo de registros por arquivo
max_records_per_file = 50000  # Ajuste conforme necessário

# Contadores
file_counter = 1
record_counter = 0

# Abra o arquivo .dbf
dbf = DBF(dbf_path)

# Função para abrir um novo arquivo de saída
def open_new_output_file(counter):
    return open(f'{output_prefix}_{counter}.txt', 'w', encoding='utf-8')

# Abra o primeiro arquivo de saída
output_file = open_new_output_file(file_counter)

# Leia o arquivo .dbf e escreva os registros nos arquivos de saída
for record in dbf:
    if record_counter >= max_records_per_file:
        # Fecha o arquivo atual e abre um novo
        output_file.close()
        file_counter += 1
        record_counter = 0
        output_file = open_new_output_file(file_counter)
    
    # Escreve o registro no arquivo de saída atual
    output_file.write(str(record) + '\n')
    record_counter += 1

# Fecha o último arquivo de saída
output_file.close()

print(f'Dados extraídos para arquivos com prefixo {output_prefix}')
