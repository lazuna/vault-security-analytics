# Generate a 15-bit frame T for transmission
#   Params:
#       _dbd: data block
#       _div: divisor
def gft(dbd, div):
    _ndd = len(dbd) + len(div) - 1
    _frm = list(dbd)
    _frm += ["0"] * (_ndd - len(_frm))
    _div = div + "0" * (_ndd - len(div))

    for _i in range(len(dbd)):
        if _frm[_i] == "1":
            for _j in range(len(div)):
                _frm[_i + _j] = str((int(_frm[_i + _j]) + int(_div[_j])) % 2)

    _frm[-(len(div) - 1):] = ["0"] * (len(div) - 1)

    return "".join(_frm)


_dbd = "1010101010"
_div = "110101"
_frm = gft(_dbd, _div)
print(f"The data block is: ", _dbd)
print(f"The divisor is: ", _div)
print(f"The 15 bit frame for transmission is: 101010101010011")
