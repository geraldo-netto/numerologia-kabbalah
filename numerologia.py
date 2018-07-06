#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

if len(sys.argv) < 2:
	print("Numerologia Cabalistica (c) 2018 Geraldo Netto")
	print("Uso: %s <nome de batismo>" % str(sys.argv[0]))
	print
	print("exemplo:")
	print("netto@besta01 ~/Desktop $ %s maria" % str(sys.argv[0]))
	print("M 4 (D ou M ou V)")
	print("A 1 (A ou J ou S)")
	print("R 9 (I ou R)")
	print("I 9 (I ou R)")
	print("A 1 (A ou J ou S)")
	print("total: 24")
	print("resultado: 6")
	sys.exit(0)


def somar_letras():
	acumulador = 0
	nome = ' '.join(sys.argv[1:]).upper()
	mapa = {
		1: ['A', 'J', 'S'],
		2: ['B', 'K', 'T'],
		3: ['C', 'L', 'U'],
		4: ['D', 'M', 'V'],
		5: ['E', 'N', 'W'],
		6: ['F', 'O', 'X'],
		7: ['G', 'P', 'Y'],
		8: ['H', 'Q', 'Z'],
		9: ['I', 'R'],
	}

	for caractere in range(len(nome)):
		for idx_numeros in range(len(mapa)):
			if nome[caractere] in mapa.values()[idx_numeros]:
				acumulador = acumulador + mapa.keys()[idx_numeros]
				# TODO reusar no formatar_lista()
				letras = '(' + ' '.join(mapa.values()[idx_numeros]).replace(' ', ' ou ') + ')'
				print("%s %d %s" % (nome[caractere], mapa.keys()[idx_numeros], letras))
				break

	return acumulador


def formatar_lista(lista):
	return '(' + ' '.join(lista).replace(' ', ', ') + ')'


def pegar_descricao(numero):
	sephiroth = {
		1: ['N/A', 'Cosme/Damiao', 'N/A'],
		2: ['Netuno', 'N/A', 'N/A'],
		3: ['Saturno', 'Xango', 'Capricornio/Aquario'],
		4: ['Jupiter', 'Oxossi', 'Sagitario/Peixes'],
		5: ['Marte', 'Ogum', 'Aries/Escorpiao'],
		6: ['Sol', 'Oxala', 'Leao'],
		7: ['Venus', 'Oxum', 'Touro/Libra'],
		8: ['Mercurio', 'Exu', 'Gemeos/Virgem'],
		9: ['Lua', 'Iemanja', 'Cancer'],
	}

	return sephiroth[numero]



def calcular_numero_magico(soma):
	numero_final = str(soma)
	tamanho_numero_final = len(numero_final)

	if tamanho_numero_final < 1:
		print("erro ao calcular numero")
		sys.exit(1)

	elif tamanho_numero_final == 1:
		return soma

	else:
		temp = 0
		for idx in range(len(numero_final)):
			temp = temp + int(numero_final[idx])

		return calcular_numero_magico(temp)


soma = somar_letras()
resultado = calcular_numero_magico(soma)
print("total: %s" % soma)
print("resultado: %d %s" % (resultado, formatar_lista(pegar_descricao(resultado))))

