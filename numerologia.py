#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from string import ascii_uppercase as letters

if len(sys.argv) < 2:
	print("Kabbalah Numerology (c) 2018 Geraldo Netto"
			"\nUso:"
			"\n$ %s ana"
			"\nA: 1"
			"\nN: 5"
			"\nA: 1"
			"\ntotal: 7 [Venus, Oxum, Touro/Libra]" % str(sys.argv[0]))
	sys.exit(0)


def char_to_number():
	names	 = ' '.join(sys.argv[1:]).upper()

	total = 0
	for name in names:
		value = 0

		if name in letters:
			for char in name:
				char_index = letters.index(char) + 1
				if char_index % 9 == 0:
					value += 9

				else:
					value += char_index % 9

			total += value
			print("%s: %d" % (name, value))

	return total


def calculate_magick_number(total):
	try:
		total_str = str(total)
		total_len = len(total_str)
		if total_len == 0:
			# the exception already contains the message
			raise ValueError("")

		if total_len == 1:
			return total

		else:
			acc = 0
			for idx in range(total_len):
				acc += int(total_str[idx])

			return calculate_magick_number(acc)

	except ValueError as ex:
		print("erro ao calcular numero %s" % total)
		sys.exit(1)


def get_sephiroth(number):
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

	return str(sephiroth[number]).replace("'", "")


number = calculate_magick_number(char_to_number())
print("total: %d %s" % (number, get_sephiroth(number)))

