# Generate CRC frame:
#   params:
#       dbd - data block d
#       div - divisor
def gcf(dbd, div):
    # Adding (n - k) zeros to the data block d
    _dbd = dbd
    _div = div
    _kln = len(_dbd)  # k, length of data block d
    _nbc = _kln + len(_div) - 1  # n, CRC divisor
    _dbd += "0" * (_nbc - _kln)

    _dbd_il = [int(_val) for _val in _dbd]  # integer list of data block d
    _div_il = [int(_val) for _val in _div]  # integer list of divisor

    for _i in range(_kln):
        if _dbd_il[_i] == 1:
            for _j in range(len(_div)):
                _dbd_il[_i + _j] ^= _div_il[_j]  # crc division

    _crc_s = "".join(str(_val) for _val in _dbd_il[-(len(_div) - 1):])
    _dbd_crc = _dbd + _crc_s  # original data block + remainder

    return _dbd_crc

# Sample test values
_dbd = "1001"
_div = "1101"
_frame = gcf(_dbd, _div)
print(f"The data block is: {_dbd}")
print(f"CRC divisor is: {_div}")
print(f"The transmitted frame size is: {_frame}\n")

# Sample test values
_dbd = "110101"
_div = "1011"
_frame = gcf(_dbd, _div)
print(f"The data block is: {_dbd}")
print(f"CRC divisor is: {_div}")
print(f"The transmitted frame size is: {_frame}\n")
