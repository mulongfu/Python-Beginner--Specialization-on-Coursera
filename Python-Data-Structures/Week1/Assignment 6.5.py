text = "X-DSPAM-Confidence:    0.8475"
new = text.find('0')
output = float(text[23:300])
print(output)