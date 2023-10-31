import xmltodict
import os
import pandas as pd

def info_xml(xml, valores):
    with open(f"xmls/{xml}", "rb") as arquivo_xml:  # Abrindo o xml para armazenar na variavel os dados;
        dic_xml = xmltodict.parse(arquivo_xml)  # Convertendo o XML para o dicionário XML Python;

    # Dados solicitados que serão exportados para a planilha;
    if "NFe" in dic_xml:
        infos_xml = dic_xml["NFe"]["infNFe"]  # Armazenando na variavel os grupos das tags;
    else:
        infos_xml = dic_xml["nfeProc"]["NFe"]["infNFe"]  # Armazenando na variavel os grupos das tags;

    numero_NFe = infos_xml["ide"]["nNF"]
    cnpj_emissor = infos_xml["emit"]["CNPJ"]
    emissor_NFe = infos_xml["emit"]["xNome"]
    cliente_NFe = infos_xml["dest"]["xNome"]
    endereco_cliente = infos_xml["dest"]["enderDest"]

    if "vol" in infos_xml["transp"]:
        peso_bruto = infos_xml["transp"]["vol"]["pesoB"]
    else:
        peso_bruto = "Não informado!"

    # Dados solicitados que serão exportados para a planilha;
    valores.append([numero_NFe, emissor_NFe, cnpj_emissor, cliente_NFe, endereco_cliente, peso_bruto])

colunas = ["NFe", "Emissor", "cnpj_emissor", "Cliente", "Endereco", "Peso Bruto"]
valores = []
lista_xmls = os.listdir("xmls")

for xml in lista_xmls:
    info_xml(xml, valores)

tabela = pd.DataFrame(columns=colunas, data=valores)
tabela.to_excel("NotasFiscais.xlsx", index=False)    
