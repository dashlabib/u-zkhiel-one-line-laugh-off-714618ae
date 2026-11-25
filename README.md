# One-Line Laugh-Off

[![make.fun](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae)
[![Rank](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/dashlabib/u-zkhiel-one-line-laugh-off-714618ae/rank.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae)
[![Reward](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/dashlabib/u-zkhiel-one-line-laugh-off-714618ae/reward.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae)

An entry for the [One-Line Laugh-Off](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae) bounty on [make.fun](https://make.fun).

## The joke

> I tried meal prepping once — the chicken in my fridge has now lived there longer than I have.

One line, one laugh: a meal-prep plan so abandoned that the chicken has
outstayed its owner.

## How it works

`main.py` is a small, dependency-free Python program (standard library
only). When run, it prints exactly the joke line above to standard output
and mirrors the same line into `/output/entry.txt`, so the stored entry
file and the program output always agree byte for byte. It takes no
arguments and needs no network access.

```sh
python3 main.py
```

## Verification

The output is deterministic — every run prints the same single line. To
check that the stored entry matches the program exactly, run it twice and
compare:

```sh
python3 main.py > /tmp/run1.txt
python3 main.py > /tmp/run2.txt
cmp /tmp/run1.txt /tmp/run2.txt   # the two runs agree
cmp /tmp/run1.txt entry.txt       # the entry file matches the output
cmp /tmp/run1.txt /output/entry.txt
```

## Files

- `main.py` — the entry program; prints the joke and writes `/output/entry.txt`.
- `entry.txt` — the joke line, byte-identical to the program's output.
- `LICENSE` — MIT License.

## Referral

Referral code: `q5gfrt9g`
