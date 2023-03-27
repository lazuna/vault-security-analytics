### Step 1. Finding the Path Loss Exponent
#### 1.1 The Path Loss Exponent

#### 1.2 Straight line's equation is

```
| Equation

Y = -57.498 * log(X) - 22.448
```

#### 1.3 Variance of RSSI for the best fit line was approximately 6.

#### 1.4  Path of exponent

```
| Path of Exponent

Line's slop = -57.498
Path of exponent Abs(-57.498) / 10 = 5.75
```

### Step 2. Range Estimation
#### 2.1 Recorded dBm at distance d

```
| Equation

𝑑0 = 1𝑚 recorded average 𝑃𝑟(𝑑0)[𝑑𝐵𝑚] @1meter
n = 5.75

Equation to calculate recorded dBm at distance d
𝑃𝑟(𝑑)𝑑𝐵𝑚 = 𝑃𝑟(𝑑𝑜)[𝑑𝐵𝑚] - 10n * 𝑙𝑜𝑔10(𝑑/𝑑𝑜)
𝑃𝑟(𝑑)𝑑𝐵𝑚 = -26.73 - 10 * (5.75) * 𝑙𝑜𝑔10(𝑑/1)
         = -26.73 - 57.5 * 𝑙𝑜𝑔10(𝑑)
```

#### 2.2 Average Distance Error
##### 2.2.1 At distance 1.3

```
| At distance 1.3

d = 1.3
Avg RSSI = -39

𝑃𝑟(𝑑)𝑑𝐵𝑚 = 𝑃𝑟(𝑑𝑜)[𝑑𝐵𝑚] - 10n * 𝑙𝑜𝑔10(𝑑/𝑑𝑜)
-39 = -26.7 - 57.5log10(d)
d   = 10 ^ [(39 - 26.7) / 57.5]
    = 1.63

Distance error = 1.63 - 1.3
               = +0.3
```

##### 2.2.2 At distance 1.4

```
| At distance 2

d = 2
Avg RSSI = -36

𝑃𝑟(𝑑)𝑑𝐵𝑚 = 𝑃𝑟(𝑑𝑜)[𝑑𝐵𝑚] - 10n * 𝑙𝑜𝑔10(𝑑/𝑑𝑜)
-36 = -26.7 - 57.5log10(d)
d   = 10 ^ [(36 - 26.7) / 57.5]
    = 1.5

Distance error = 1.5 - 2
               = -.5
```

##### 2.2.3 At distance 3

```
| At distance 3

d = 3
Avg RSSI = -48

𝑃𝑟(𝑑)𝑑𝐵𝑚 = 𝑃𝑟(𝑑𝑜)[𝑑𝐵𝑚] - 10n * 𝑙𝑜𝑔10(𝑑/𝑑𝑜)
-48 = -26.7 - 57.5log10(d)
d   = 10 ^ [(48 - 26.7) / 57.5]
    = 2.4

Distance error = 2.4 - 3
               = -.6
```

##### 2.2.4 At distance 3.7

```
| At distance 3.7

d = 3.7
Avg RSSI = -61

𝑃𝑟(𝑑)𝑑𝐵𝑚 = 𝑃𝑟(𝑑𝑜)[𝑑𝐵𝑚] - 10n * 𝑙𝑜𝑔10(𝑑/𝑑𝑜)
-61 = -26.7 - 57.5log10(d)
d   = 10 ^ [(61 - 26.7) / 57.5]
    = 3.9

Distance error = 3.9 - 3.7
               = +.2
```

##### 2.2.5 At distance 5.4

```
| At distance 5.4

d = 5.4
Avg RSSI = -67

𝑃𝑟(𝑑)𝑑𝐵𝑚 = 𝑃𝑟(𝑑𝑜)[𝑑𝐵𝑚] - 10n * 𝑙𝑜𝑔10(𝑑/𝑑𝑜)
-67 = -26.7 - 57.5log10(d)
d   = 10 ^ [(67 - 26.7) / 57.5]
    = 5

Distance error = 5 - 5.4
               = -.4
```

##### 2.2.6 Average distance error

```
| Average distance error

Average distance error = Distance error1 + Distance error2 + Distance error3 + Distance error4 + Distance error5

Average distance error = (0.3 - 0.5 - 0.6 + 0.2 - 0.4)/5
                       = -0.2
```
