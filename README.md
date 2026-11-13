# CS5700 Programming Assignment 2

**Submitted by:** Bipin Bhusal Chhetri

## Repository Layout

- `main.py`: contains all the code
- `output.txt`: contains the actual output from a test run, which was redirected from the terminal to the text file using the redirect operator (`>`).

## Requirement

- `Python 3.9` or later
- No external dependencies required.

## Running the program

`python <path/to/main.py>`

OR

`python3 <path/to/main.py>`

Use `python` or `python3` depending on how Python is installed and configured on your system.

## Output

**Ciphertext:**`OhVTChwGUxEBFhIYUwcbGgBTEBoDGxYBBxYLB19TGgdTHhYSHQBTBxsSB1MKHAZTEgEWUxIRHxZTBxxTEQEWEhhTAAYRAAcaBwYHGhwdUxAaAxsWAQBTBgAaHRRTFQEWAgYWHRAKUxIdEh8KABoAXVMkFh8fUzccHRZS`

**Plaintext:** `If you break this ciphertext, it means that you are able to break substitution ciphers using frequency analysis. Well Done!`

**Key:** `115` or `s`

## Strategy used to break the ciphertext

Initially, I was not paying attention to how the ciphertext was encrypted and jumped straight to using the statistical analysis as shown in the lecture slide. After multiple failed attempts, I realized that the statistical analysis used in the lecture slide was applied on a ciphertext encrypted using the Caesar Cipher. However, the ciphertext given for this assignment was encrypted using the version of Stream Cipher. So, I adjusted the formula given in the lecture slide from `P(c-i)` to `P(x \xor i)`. Also, the formula used in the lecture slide has 26 possible keys due the Caesar Cipher. However, each character of the ciphertext given for this assignment was encrypted using the same key and stored in a bytearray, which stores each item as a byte (8 bits). So, in this scenario there are 256 possible keys (2^8). This was another adjustment that I applied to the formula in the lecture slide.

Furthermore, I decoded the ciphertext before using the statistical analysis because it was encoded as base64, and used the default value of `0` for any character that was not in the unigram table for english (taken from the lecture slide).

## Keys and Correlation Table (sorted in descending order based on correlation)

| Key | Correlation |
| ----- | ------------- |
| 115 | 0.0507 |
| 116 | 0.0385 |
| 117 | 0.0376 |
| 111 | 0.0354 |
| 114 | 0.0343 |
| 098 | 0.0337 |
| 110 | 0.0331 |
| 104 | 0.0309 |
| 105 | 0.0307 |
| 119 | 0.0300 |
| 126 | 0.0294 |
| 101 | 0.0287 |
| 127 | 0.0283 |
| 121 | 0.0283 |
| 100 | 0.0270 |
| 120 | 0.0260 |
| 099 | 0.0239 |
| 102 | 0.0232 |
| 054 | 0.0210 |
| 112 | 0.0202 |
| 122 | 0.0196 |
| 123 | 0.0194 |
| 113 | 0.0187 |
| 125 | 0.0175 |
| 097 | 0.0164 |
| 124 | 0.0164 |
| 107 | 0.0164 |
| 118 | 0.0154 |
| 039 | 0.0142 |
| 096 | 0.0141 |
| 060 | 0.0138 |
| 103 | 0.0136 |
| 108 | 0.0136 |
| 050 | 0.0133 |
| 106 | 0.0126 |
| 109 | 0.0124 |
| 058 | 0.0117 |
| 061 | 0.0116 |
| 033 | 0.0105 |
| 059 | 0.0103 |
| 032 | 0.0098 |
| 055 | 0.0078 |
| 062 | 0.0058 |
| 063 | 0.0058 |
| 048 | 0.0057 |
| 038 | 0.0055 |
| 053 | 0.0037 |
| 042 | 0.0035 |
| 049 | 0.0034 |
| 035 | 0.0031 |
| 052 | 0.0030 |
| 036 | 0.0026 |
| 056 | 0.0020 |
| 043 | 0.0017 |
| 037 | 0.0017 |
| 082 | 0.0016 |
| 095 | 0.0015 |
| 051 | 0.0015 |
| 086 | 0.0015 |
| 057 | 0.0013 |
| 069 | 0.0012 |
| 065 | 0.0011 |
| 041 | 0.0011 |
| 067 | 0.0010 |
| 083 | 0.0010 |
| 084 | 0.0010 |
| 091 | 0.0009 |
| 078 | 0.0009 |
| 080 | 0.0009 |
| 094 | 0.0009 |
| 072 | 0.0008 |
| 089 | 0.0008 |
| 085 | 0.0008 |
| 088 | 0.0008 |
| 073 | 0.0007 |
| 074 | 0.0007 |
| 087 | 0.0007 |
| 045 | 0.0007 |
| 047 | 0.0007 |
| 075 | 0.0007 |
| 077 | 0.0007 |
| 076 | 0.0006 |
| 044 | 0.0005 |
| 046 | 0.0005 |
| 068 | 0.0005 |
| 034 | 0.0005 |
| 064 | 0.0005 |
| 081 | 0.0004 |
| 066 | 0.0004 |
| 071 | 0.0004 |
| 040 | 0.0004 |
| 079 | 0.0003 |
| 093 | 0.0003 |
| 090 | 0.0002 |
| 092 | 0.0002 |
| 070 | 0.0001 |
| 000 | 0.0000 |
| 001 | 0.0000 |
| 002 | 0.0000 |
| 003 | 0.0000 |
| 004 | 0.0000 |
| 005 | 0.0000 |
| 006 | 0.0000 |
| 007 | 0.0000 |
| 008 | 0.0000 |
| 009 | 0.0000 |
| 010 | 0.0000 |
| 011 | 0.0000 |
| 012 | 0.0000 |
| 013 | 0.0000 |
| 014 | 0.0000 |
| 015 | 0.0000 |
| 016 | 0.0000 |
| 017 | 0.0000 |
| 018 | 0.0000 |
| 019 | 0.0000 |
| 020 | 0.0000 |
| 021 | 0.0000 |
| 022 | 0.0000 |
| 023 | 0.0000 |
| 024 | 0.0000 |
| 025 | 0.0000 |
| 026 | 0.0000 |
| 027 | 0.0000 |
| 028 | 0.0000 |
| 029 | 0.0000 |
| 030 | 0.0000 |
| 031 | 0.0000 |
| 128 | 0.0000 |
| 129 | 0.0000 |
| 130 | 0.0000 |
| 131 | 0.0000 |
| 132 | 0.0000 |
| 133 | 0.0000 |
| 134 | 0.0000 |
| 135 | 0.0000 |
| 136 | 0.0000 |
| 137 | 0.0000 |
| 138 | 0.0000 |
| 139 | 0.0000 |
| 140 | 0.0000 |
| 141 | 0.0000 |
| 142 | 0.0000 |
| 143 | 0.0000 |
| 144 | 0.0000 |
| 145 | 0.0000 |
| 146 | 0.0000 |
| 147 | 0.0000 |
| 148 | 0.0000 |
| 149 | 0.0000 |
| 150 | 0.0000 |
| 151 | 0.0000 |
| 152 | 0.0000 |
| 153 | 0.0000 |
| 154 | 0.0000 |
| 155 | 0.0000 |
| 156 | 0.0000 |
| 157 | 0.0000 |
| 158 | 0.0000 |
| 159 | 0.0000 |
| 160 | 0.0000 |
| 161 | 0.0000 |
| 162 | 0.0000 |
| 163 | 0.0000 |
| 164 | 0.0000 |
| 165 | 0.0000 |
| 166 | 0.0000 |
| 167 | 0.0000 |
| 168 | 0.0000 |
| 169 | 0.0000 |
| 170 | 0.0000 |
| 171 | 0.0000 |
| 172 | 0.0000 |
| 173 | 0.0000 |
| 174 | 0.0000 |
| 175 | 0.0000 |
| 176 | 0.0000 |
| 177 | 0.0000 |
| 178 | 0.0000 |
| 179 | 0.0000 |
| 180 | 0.0000 |
| 181 | 0.0000 |
| 182 | 0.0000 |
| 183 | 0.0000 |
| 184 | 0.0000 |
| 185 | 0.0000 |
| 186 | 0.0000 |
| 187 | 0.0000 |
| 188 | 0.0000 |
| 189 | 0.0000 |
| 190 | 0.0000 |
| 191 | 0.0000 |
| 192 | 0.0000 |
| 193 | 0.0000 |
| 194 | 0.0000 |
| 195 | 0.0000 |
| 196 | 0.0000 |
| 197 | 0.0000 |
| 198 | 0.0000 |
| 199 | 0.0000 |
| 200 | 0.0000 |
| 201 | 0.0000 |
| 202 | 0.0000 |
| 203 | 0.0000 |
| 204 | 0.0000 |
| 205 | 0.0000 |
| 206 | 0.0000 |
| 207 | 0.0000 |
| 208 | 0.0000 |
| 209 | 0.0000 |
| 210 | 0.0000 |
| 211 | 0.0000 |
| 212 | 0.0000 |
| 213 | 0.0000 |
| 214 | 0.0000 |
| 215 | 0.0000 |
| 216 | 0.0000 |
| 217 | 0.0000 |
| 218 | 0.0000 |
| 219 | 0.0000 |
| 220 | 0.0000 |
| 221 | 0.0000 |
| 222 | 0.0000 |
| 223 | 0.0000 |
| 224 | 0.0000 |
| 225 | 0.0000 |
| 226 | 0.0000 |
| 227 | 0.0000 |
| 228 | 0.0000 |
| 229 | 0.0000 |
| 230 | 0.0000 |
| 231 | 0.0000 |
| 232 | 0.0000 |
| 233 | 0.0000 |
| 234 | 0.0000 |
| 235 | 0.0000 |
| 236 | 0.0000 |
| 237 | 0.0000 |
| 238 | 0.0000 |
| 239 | 0.0000 |
| 240 | 0.0000 |
| 241 | 0.0000 |
| 242 | 0.0000 |
| 243 | 0.0000 |
| 244 | 0.0000 |
| 245 | 0.0000 |
| 246 | 0.0000 |
| 247 | 0.0000 |
| 248 | 0.0000 |
| 249 | 0.0000 |
| 250 | 0.0000 |
| 251 | 0.0000 |
| 252 | 0.0000 |
| 253 | 0.0000 |
| 254 | 0.0000 |
| 255 | 0.0000 |
