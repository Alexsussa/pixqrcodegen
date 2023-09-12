#!/usr/bin/python3
# -*- coding: utf-8 -*-

import crcmod
import qrcode
import os

class Payload:
    def __init__(self, nome, chavepix, valor, cidade, txtId, diretorio=''):
        self.nome = nome
        self.chavepix = chavepix
        self.valor = valor.replace(',', '.')
        self.cidade = cidade
        self.txtId = txtId
        self.diretorioQrCode = diretorio

        self.nome_tam = len(self.nome)
        self.chavepix_tam = len(self.chavepix)
        self.valor_tam = len(self.valor)
        self.cidade_tam = len(self.cidade)
        self.txtId_tam = len(self.txtId)

        self.merchantAccount_tam = '0014BR.GOV.BCB.PIX01' + str(self.chavepix_tam).zfill(2) + self.chavepix
        self.transactionAmount_tam = str(self.valor_tam).zfill(2) + f'{float(self.valor):.2f}'

        self.addDataField_tam = '05' + str(self.txtId_tam).zfill(2) + self.txtId

        self.nome_tam = str(self.nome_tam).zfill(2)
        self.cidade_tam = str(self.cidade_tam).zfill(2)

        self.payloadFormat = '000201'
        self.merchantAccount = '26' + str(len(self.merchantAccount_tam)).zfill(2) + self.merchantAccount_tam
        self.merchantCategCode = '52040000'
        self.transactionCurrency = '5303986'
        self.transactionAmount = '54' + self.transactionAmount_tam
        self.countryCode = '5802BR'
        self.merchantName = '59' + self.nome_tam + self.nome
        self.merchantCity = '60' + self.cidade_tam + self.cidade
        self.addDataField = '62' + str(len(self.addDataField_tam)).zfill(2) + self.addDataField_tam
        self.crc16 = '6304'

    def gerarPayload(self):
        self.payload = (
            f'{self.payloadFormat}{self.merchantAccount}{self.merchantCategCode}'
            f'{self.transactionCurrency}{self.transactionAmount}{self.countryCode}'
            f'{self.merchantName}{self.merchantCity}{self.addDataField}{self.crc16}'
        )

        self.gerarCrc16(self.payload)

    def gerarCrc16(self, payload):
        crc16 = crcmod.mkCrcFun(poly=0x11021, initCrc=0xFFFF, rev=False, xorOut=0x0000)
        self.crc16Code = hex(crc16(str(payload).encode('utf-8')))[2:].upper().zfill(4)
        self.payload_completa = f'{payload}{self.crc16Code}'
        self.gerarQrCode(self.payload_completa, self.diretorioQrCode)

    def gerarQrCode(self, payload, diretorio):
        dir = os.path.expanduser(diretorio)
        self.qrcode = qrcode.make(payload)
        self.qrcode.save(os.path.join(dir, 'pixqrcodegen.png'))
        print(payload)


if __name__ == '__main__':
    # 12345678900 seria o formato do CPF sem pontos e traços
    Payload('Nome Sobrenome', '12345678900', '1.00', 'Cidade Ficticia', 'LOJA01').gerarPayload()
