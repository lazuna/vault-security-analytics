### 3.1 Write a program (in any language) that generates an 𝑛-bit frame for transmission from a k-bit data block D and a (𝑛 − 𝑘 + 1) bit CRC divisor P. Compile and run the program with at least two set of inputs to confirm that this program is generating CRC patterns correctly. 

CRC generator Python program:

```
 | Code: crc.py

  1 # Apply CRC to received frame if frame should be accepted or rejected                                                                                                  
  2 _pcd = "110101" # CRC divisor
  3 _frm = "101110101011011"
  4 _frp = _frm + "0" * (len(_pcd) - 1)# Frame padding with added zeros to the lengh of CRC divisor
  5  
  6 # CRC calculation
  7 _rmd = ""
  8 for _i in range(len(_pcd)):
  9     _rmd += _frp[_i]
 10  
 11 for _i in range(len(_pcd), len(_frp)):
 12     if _rmd[0] == "1":
 13         _tmp = "" # Temporary value
 14         for _j in range(len(_pcd)):
 15             _tmp += str(int(_rmd[_j]) ^ int(_pcd[_j]))
 16         _rmd = _tmp[1:] + _frp[_i]
 17     else:
 18         _rmd = _rmd[1:] + _frp[_i]
 19  
 20 if _rmd == "0" * len(_pcd):
 21     print("Frame will be accepted!")
 22 else:
 23     print("Frame will be discarded!")
```

#### 3.1.1 Generates a message of 𝑘 =10 bits. 

```
| Code: gaf.py

  1 # Generate a frame
  2 #   Params:
  3 #       _dbd - data block d
  4 #       _div - divisor
  5  
  6 def gaf(dbd, div):
  7     _dbd = dbd
  8     _div = div
  9     _ndd = len(_dbd) + len(_div) - 1 # obtain value of n from data block and divisor
 10     _frm = _dbd + "0" * (_ndd - len(_dbd)) # frame
 11  
 12     _rmd = pdv(_frm, _div)[1]
 13     _crc = bin(int(_rmd, 2))[2:].zfill(len(_div) - 1)
 14     _frm = _frm[:len(_frm) - len(_crc)] + _crc
 15     return _frm
 16  
 17 def pdv(dvd, div):
 18     # To process polynomial division on two binary polynomials
 19     _div = div
 20     _dvd = dvd
 21  
 22     _dvd = _dvd.lstrip("0")
 23     _div = _div.lstrip("0")
 24  
 25     _div = _div + "0" * (len(_dvd) - len(_div))
 26  
 27     # Process polynomial division
 28     _rmd = ""
 29     for _i in range(len(_dvd)):
 30         if _rmd and _rmd[0] == "1":
 31             _rmd = _rmd[1:]
 32         else:
 33             _rmd += _dvd[_i]
 34  
 35         if len(_rmd) == len(_div):
 36             _rmd = bin(int(_rmd, 2) ^ int(_div, 2))[:]
 37  
 38     return (_dvd + _rmd, _rmd)
 39  
 40 print("------------------------------")
 41  
 42 # Sample test inputs
 43 print("Sample test inputs")
 44 _dbd = "1110001111"
 45 _div = "1011"
 46 _frm = gaf(_dbd, _div)
 47 print(f"The data block is: {_dbd}")
 48 print(f"Divisor is: {_div}")
 49 print(f"Frame is {_frm}")
 50  
 51 print("------------------------------")
 52  
 53 # Sample test inputs
 53 # Sample test inputs
 54 print("Sample test inputs")
 55 _dbd = "1011010010"
 56 _div = "110101"
 57 _frm = gaf(_dbd, _div)
 58 print(f"The data block is: {_dbd}")
 59 print(f"Divisor is: {_div}")
 60 print(f"Frame is {_frm}")
 61  
 62 print("------------------------------")
```

#### 3.1.2 Uses the previous code with P=110101 to generate the corresponding 15-bit frame T for transmission

```
| Code: gft.py

  1 # Generate a 15-bit frame T for transmission                                                                                                                           
  2 #   Params:
  3 #       _dbd: data block
  4 #       _div: divisor
  5 def gft(dbd, div):
  6     _ndd = len(dbd) + len(div) - 1
  7     _frm = list(dbd)
  8     _frm += ["0"] * (_ndd - len(_frm))
  9     _div = div + "0" * (_ndd - len(div))
 10  
 11     for _i in range(len(dbd)):
 12         if _frm[_i] == "1":
 13             for _j in range(len(div)):
 14                 _frm[_i + _j] = str((int(_frm[_i + _j]) + int(_div[_j])) % 2)
 15  
 16     _frm[-(len(div) - 1):] = ["0"] * (len(div) - 1)
 17  
 18     return "".join(_frm)
 19  
 20  
 21 _dbd = "1010101010"
 22 _div = "110101"
 23 _frm = gft(_dbd, _div)
 24 print(f"The data block is: ", _dbd)
 25 print(f"The divisor is: ", _div)
 26 print(f"The 15 bit frame for transmission is: 101010101010011")
```

#### 3.1.3 Generates transmission errors at any bit positions of T = 101010101010011. 

```
| Code: tfe.py

  1 # Transmitted frames with errors                                                                                                                                       
  2 import random
  3  
  4 _frm = "101010101010011"
  5  
  6 # Introducing 3 errors at random positions in the frame.
  7 _erp = random.sample(range(len(_frm)), 3)
  8  
  9 for _i in _erp:
 10     _frm = _frm[:_i] + str(int(_frm[_i]) ^ 1) + _frm[_i + 1:]
 11  
 12 print("Trabsmitted frame with errors is: ", _frm)
```

#### 3.1.4 Applies CRC to the received frame (i.e. frame T after introducing errors) to determine if the frame should be accepted or discarded. 

```
| Code: gcf.py

  1 # Generate CRC frame:                                                                                                                                                  
  2 #   params:
  3 #       dbd - data block d
  4 #       div - divisor
  5 def gcf(dbd, div):
  6     # Adding (n - k) zeros to the data block d
  7     _dbd = dbd
  8     _div = div
  9     _kln = len(_dbd)  # k, length of data block d
 10     _nbc = _kln + len(_div) - 1  # n, CRC divisor
 11     _dbd += "0" * (_nbc - _kln)
 12  
 13     _dbd_il = [int(_val) for _val in _dbd]  # integer list of data block d
 14     _div_il = [int(_val) for _val in _div]  # integer list of divisor
 15  
 16     for _i in range(_kln):
 17         if _dbd_il[_i] == 1:
 18             for _j in range(len(_div)):
 19                 _dbd_il[_i + _j] ^= _div_il[_j]  # crc division
 20  
 21     _crc_s = "".join(str(_val) for _val in _dbd_il[-(len(_div) - 1):])
 22     _dbd_crc = _dbd + _crc_s  # original data block + remainder
 23  
 24     return _dbd_crc
 25  
 26 # Sample test values
 27 _dbd = "1001"
 28 _div = "1101"
 29 _frame = gcf(_dbd, _div)
 30 print(f"The data block is: {_dbd}")
 31 print(f"CRC divisor is: {_div}")
 32 print(f"The transmitted frame size is: {_frame}\n")
 33  
 34 # Sample test values
 35 _dbd = "110101"
 36 _div = "1011"
 37 _frame = gcf(_dbd, _div)
 38 print(f"The data block is: {_dbd}")
 39 print(f"CRC divisor is: {_div}")
 40 print(f"The transmitted frame size is: {_frame}\n")
```

### 3.2 CRC error-detecting scheme
#### 3.2.1 In a CRC error-detecting scheme, choose P(x) = X4 + X + 1. Encode the bits 10010011011. 
In order to encode the bits 10010011011 using CRC with 

```
P(x) = X^4 + X + 1
```

- Append 0000 at the end of the data, so code word becomes 100100110110000.
- Then divide codeword by the P(x) using modulo-2 arithmetic to produce a remainder. Which would the CRC code to append to the data block.

```
1 0 0 1 0 0 1 1 0 1 1 0 0 0 0 0

XOR 1 0 1 // X^4
................
100
1011             // Shift left
................
 111
 1010            // Shift left
................
  111
  1011           // Shift left
................
   100
   1011          // Shift left
................
    111
    1010         // Shift left
................
     111
     1011        // Shift left
................
      100
      1011       // Shift left
................
       111
       1010      // Shift left
................
        111
        1011     // Remainder - CRC Code


For the input: 10010011011, CRC code is: 1011, transmitted message is concatenation of original message, CRC code is: 100100110111011
```

#### 3.2.2 Suppose the channel introduces an error pattern 100010000000000 (i.e., a flip from 1 to 0 or from 0 to 1 in position 1 and 5). What is received? Can the error be detected? 
Introduced error patten is 100010000000000,
Received message: 1001101101100000.

Error pattern bits get changed at 1 and 5 positions, and transmitted message 10010011011011, and received message is 10011011000000.

Calculate the CRC code to get a different remainder:

```
1001101101100000
XOR 101             // X^4
................
100
1011                // Shift left
................
 111
 1100               // Shift left
................
  101
  1011              // Shift left
................
   010
   1011             // Shift left
................
    110
    1100            // Shift left
................
     010
     1100           // Shift left
................
      000
      1100          // Shift left
................
       100
       1100         // Shift left
................
        010         // Remainder

The remainder (010) is not equal to CRC code (1011) appended to original message. Error can be determined by using CRC check.
```

#### 3.2.3 Repeat part (b) with error pattern 100110000000000. 
Introduces an error pattern of 100110000000000,
the received message: 0000101101100000

Error pattern gets changed the bits at positions 1 and 5, and transmitted message 10010011011011, and the received message is 00001011000000. 

Calculate the CRC code  to get the same remainder:

```
0000101101100000
XOR 101                    // X^4
................
000
1011                       // Shift left
................
 101
 0100                      // Shift left
................
  011
  1011                     // Shift left
................
   110
   0100                    // Shift left
................
    100
    0100                   // Shift left
................
     110
     0100                  // Shift left
................
      100
      0100                 // Shift left
................
       110
       0100                // Shift left
................
        100                // Remainder

The remainder (100) is not equal to CRC code (1011) appended to original message. Error can be determined by using CRC check.
```
