#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import sys

if len(sys.argv) > 2:
    entrada = sys.argv[1]
    saida = sys.argv[2]
else:
    print('\n\nFaltando os parâmetros de arquivo de entrada e arquivo de saída!\n\nTente novamente enviando os parâmetros adequadamente!\n\n')
    quit()

#print('\n'.join(sys.argv))
#print(len(sys.argv))

colunas = ['concessionaria','cod_agente_arrecadador','nome_agente_arrecadador','nome_grupo_loja','uf_cef','cidade_cef','uf_ag_nao_financeiro','mes_transacao','status','bu_description','estado','profit_center','cod_area','dat_tra','data_venda','midia','valor_face','qtde_recargas','valor_total','val_tarifa','val_tarifa_total']

colunas_ajustadas = colunas

#entrada = '.\\input\\fechamento_atm_mes_geral_202410.csv'
entrada = sys.argv[1]

#saida = '.\\output\\base_saida.csv'
saida = sys.argv[2]

print('*'*80)
print('*      PROCESSO DE IMPORTAÇÃO, TRATAMENTO E EXPORTAÇÃO DE BASE DE SELLIN       *')
print('*'*80)
print(f'Arquivo de entrada: {entrada}\nArquivo de saída: {saida}'.format(entrada, saida))

df = pd.read_csv(entrada , encoding='iso-8859-1', on_bad_lines='skip', sep=';', usecols=colunas)
df.columns = colunas_ajustadas
df.to_csv(saida, sep=';', index = False)
print('\n\nprocesso finalizado!\n\n')
print('*'*80)