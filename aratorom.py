def ArabictoRom(inputnum):
	result = ""
	integer_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
	roman_list = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
	if isinstance(inputnum, int) == False:
		print("invalid type of input:", type(inputnum),"please type a positive integer.")
		return -1;
	if (inputnum >= 4000) or (inputnum <= 0):
		print("invalid integer range: [1, 3999], your input is:", inputnum)
		return -2;

	for i in range(len(integer_list)):
		count = inputnum//(integer_list[i])
		roman_dig = roman_list[i]*count
		inputnum = inputnum - (count * integer_list[i])
		result += roman_dig

	return result

def main():
	print(ArabictoRom("sdfve"))

if __name__ == '__main__':
	main()