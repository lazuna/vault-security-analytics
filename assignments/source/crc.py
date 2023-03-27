# Apply CRC to received frame if frame should be accepted or rejected
_pcd = "110101" # CRC divisor
_frm = "101110101011011"
_frp = _frm + "0" * (len(_pcd) - 1) # Frame padding with added zeros to the lengh of CRC divisor

# CRC calculation
_rmd = ""
for _i in range(len(_pcd)):
    _rmd += _frp[_i]

for _i in range(len(_pcd), len(_frp)):
    if _rmd[0] == "1":
        _tmp = "" # Temporary value
        for _j in range(len(_pcd)):
            _tmp += str(int(_rmd[_j]) ^ int(_pcd[_j]))
        _rmd = _tmp[1:] + _frp[_i]
    else:
        _rmd = _rmd[1:] + _frp[_i]

if _rmd == "0" * len(_pcd):
    print("Frame will be accepted!")
else:
    print("Frame will be discarded!")
