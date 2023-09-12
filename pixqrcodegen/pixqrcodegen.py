#!/usr/bin/python3
# -*- coding: utf-8 -*-

import crcmod
import qrcode
import os


class Payload:
    def __init__(self, nome, chavepix, valor, cidade, txt_id, diretorio=''):
        self.nome = nome
        self.chavepix = chavepix
        if ',' in valor or '.' in valor:
            self.valor = valor.replace(',', '.')
            self.valor = f'{self.valor.split(".")[0]}.{self.valor.split(".")[1].ljust(2, "0")}'
        else:
            self.valor = f'{valor}'
        self.cidade = cidade
        self.txt_id = txt_id
        self.diretorio_qrcode = diretorio

        self.nome_tam = str(len(self.nome)).zfill(2)
        self.chavepix_tam = str(len(self.chavepix)).zfill(2)
        self.valor_tam = str(len(self.valor)).zfill(2)
        self.cidade_tam = str(len(self.cidade)).zfill(2)
        self.txt_id_tam = str(len(self.txt_id)).zfill(2)

        self.merchant_account_tam = f'0014br.gov.bcb.pix01{self.chavepix_tam}{self.chavepix}'
        self.transaction_amount_tam = f'{self.valor_tam}{self.valor}'
        self.add_data_field_tam = f'05{self.txt_id_tam}{self.txt_id}'
        self.merchant_account = f'26{str(len(self.merchant_account_tam))}{self.merchant_account_tam}'
        self.transaction_amount = f'{self.transaction_amount_tam}'
        self.merchant_name = f'59{self.nome_tam}{self.nome}'
        self.merchant_city = f'60{self.cidade_tam}{self.cidade}'
        self.add_data_field = f'{str(len(self.add_data_field_tam)).zfill(2)}{self.add_data_field_tam}'

    def gerar_payload(self):
        payload = (f'000201'  # Payload Format Indicator
                   f'{self.merchant_account}'
                   f'52{self.transaction_amount}'  # Merchant Category Code
                   f'5303986'  # Currency Code and Transaction Amount
                   f'5802BR'  # Country Code
                   f'{self.merchant_name}'
                   f'{self.merchant_city}'
                   f'62{self.add_data_field}'
                   f'6304')  # CRC16

        crc16_code_formatado = hex(crcmod.mkCrcFun(poly=0x11021, initCrc=0xFFFF, rev=False, xorOut=0x0000)
                                   (payload.encode('utf-8'))).lstrip('0x').upper().zfill(4)

        payload_completa = f'{payload}{crc16_code_formatado}'

        directory = os.path.expanduser(self.diretorio_qrcode)
        qrcode1 = qrcode.make(payload_completa)
        qrcode1.save(os.path.join(directory, 'pixqrcodegen.png'))
        print(payload_completa)


if __name__ == '__main__':
    # 12345678900 seria o formato do CPF sem pontos e traços
    Payload('Fulano de Tal',
            '123e4567-e12b-12d1-a456-426655440000',
            '0000', 'BRASILIA', '***').gerar_payload()


#  Saída esperada: "00020126580014br.gov.bcb.pix0136123e4567-e12b-12d1-a456-4266554400005204000053039865802BR5913
#                   Fulano de Tal6008BRASILIA62070503***63041D3D"
#  Valores conforme exemplo do manual do Banco Central do Brasil
