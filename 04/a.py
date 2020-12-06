#!/usr/bin/env python3

with open("input.txt") as f:
    passports = f.read().split("\n\n")

fields = "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"
print(sum(1 for passport in passports
          if all(field in passport for field in fields)))
