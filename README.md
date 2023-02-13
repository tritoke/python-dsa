# python-dsa
A toy implementation of DSA in python based on my university lectures.

**NOTE: NEVER USE THIS FOR ANYTHING EVER, IT IS CREATED SOLELY FOR LEARNING**

## Usage

```py
message = b"Wow I sure do love messages!!!!"
r, s = sign(message)
print(message, r, s)
assert verify(message, r, s)
print("Signature verified")
```

```
b'Wow I sure do love messages!!!!' 6061955943091960750606269410899422162778686269940406451729110863324 9002110537813590762643638905372234926102399324119379816214567116573
Signature verified
```
