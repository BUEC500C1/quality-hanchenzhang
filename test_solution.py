from aratorom import ArabictoRom

def test_small_int():
	assert ArabictoRom(1) == "I"
	assert ArabictoRom(10) == "X"
	assert ArabictoRom(100) == "C"
	assert ArabictoRom(49) == "XLIX"
	assert ArabictoRom(143) == "CXLIII"
	assert ArabictoRom(99) == "XCIX"

def test_big_int():
	assert ArabictoRom(1000) == "M"
	assert ArabictoRom(2019) == "MMXIX"
	assert ArabictoRom(3999) == "MMMCMXCIX"

def test_badtype():
	assert ArabictoRom("A") == -1
	assert ArabictoRom(1.2) == -1
	assert ArabictoRom([1,2,3]) == -1
	assert ArabictoRom(-213.2) == -1

def test_bad_int():
	assert ArabictoRom(-1) == -2
	assert ArabictoRom(5674) == -2
	assert ArabictoRom(-50897) == -2