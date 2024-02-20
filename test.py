import datetime
# lista_concursos = [{'Publicado em': '30/10/2023', 'Descrição': 'EDITAL Nº 27/APMT/PMSC/2023 - Contratação de ACTs para a Rede de Colégios da Polícia Militar do Estado de Santa Catarina.', 'Status': 'Em Andamento'}, {'Publicado em': '22/12/2023', 'Descrição': 'EDITAL Nº 32/APMT/PMSC/2023- Contratação de ACTs para a Rede de Colégios da Polícia Militar - Jaraguá do Sul.', 'Status': 'Em Andamento'}, {'Publicado em': '09/01/2024', 'Descrição': 'Edital Nº 01/APMT/PMSC/2024 - Processo Seletivo para contratação de ACTs para Rede de Colégios da Policia Militar de Santa Catarina (unidades Lages, Blumenau, Joinville e Laguna)', 'Status': 'Em Andamento'}]
#
#
# lista_str ='\n'.join([str(i) for i in lista_concursos])
#
# print(lista_str)

hoje = datetime.datetime.today().strftime('%d/%m/%Y')
print(hoje)
