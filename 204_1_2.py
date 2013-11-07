def basic_remainder(dividend,divisor):
	x=float(dividend)/float(divisor)
	intX=int(x)
	remainder=(x-intX)*divisor
	IntRemainder=int(remainder+0.5)
	return IntRemainder
print basic_remainder(14,5)

def divmod_remainder(dividend,divisor):
	(a,b)=divmod(dividend,divisor)
	return b
print divmod_remainder(14,5)

def op_remainder(dividend,divisor):
	remainder=dividend%divisor
	return remainder
print op_remainder(14,5)
