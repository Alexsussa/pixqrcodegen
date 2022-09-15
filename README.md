# PIXQRCODEGEN

## Módulo em Python

Este módulo foi criado para Python com compatiblidade para diversas chaves Pix para gerar a Paylod do Pix.

## O que é Pix?

Pix é um meio de pagamento eletrônico instantâneo e gratuito oferecido pelo [Banco Central do Brasil](https://www.bcb.gov.br/estabilidadefinanceira/pix) a pessoas físicas e jurídicas, sendo o mais recente meio de pagamento do Sistema de Pagamentos Brasileiro.

## O que é Pix Payload?

A Payload do Pix nada mais é que um conjunto de informações necessárias para pagamentos e transferências bancárias que necessita seguir as regras e estar bem formatada para ter sucesso no pagamento ou transferência.

Nesta [API](https://www.bcb.gov.br/content/estabilidadefinanceira/pix/Regulamento_Pix/II_ManualdePadroesparaIniciacaodoPix.pdf), do próprio [Banco Centra do Brasil](https://www.bcb.gov.br/), você poderá olhar com mais detalhes como funciona uma Payload Pix.

# Modo de uso

```
# Importando o módulo
from pixqrcodegen import Payload

# Parâmetros necessários
payload = Payload(nome, chavepix, valor, cidade, txtxId)

# Chamando a função responsável para gerar a Payload Pix e o QR Code
payload.gerarPayload()

#####################################################################

"""Exemplo com dados fictícios"""

payload = Payload('Nome Sobrenome', '12345678900', '1.00', 'Cidade Ficticia', 'LOJA01')

payload.gerarPayload()

"""Resultado"""

00020126330014BR.GOV.BCB.PIX01111234567890052040000530398654041.005802BR5914Nome Sobrenome6015Cidade Ficticia62100506LOJA016304C8E4

"""Observação"""

QR Code é gerado após a criação da Payload do Pix e salvo no diretório de desenvolvimento.

```
# Importante

Nenhum dos dados podem ter caracteres especiais como acentos ou "ç" e os valores monetários devem ser dividos por ponto (.) e não vírgula (,).

Exemplo:

Valor incorreto: 50,00 

Valor correto: 50.00

