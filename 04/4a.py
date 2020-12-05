#!/usr/bin/env python3
import re

with open("input.txt") as f:
    inputs = f.read()

passports = inputs.split("\n\n")
fields = "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"
print(len([passport for passport in passports
          if all(field in passport for field in fields)]))
