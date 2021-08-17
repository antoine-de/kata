# https://codingdojo.org/kata/Anagram/

## Problem Description

Write a program that generates all two-word anagrams of the string “documenting”. 

Here’s a word list you might want to use: https://gist.githubusercontent.com/calvinmetcalf/084ab003b295ee70c8fc/raw/314abfdc74b50f45f3dbbfa169892eff08f940f2/wordlist.txt.


## basic solution

build a map with char -> nb occurence, and compare it to the main word

## basis solution

build a basis

basis = nb chars in base word: 11

val = first position in base word (eg: 'd' = 1, 'o' = 2, 'c' = 3, ...)