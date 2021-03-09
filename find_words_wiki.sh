#!/bin/bash

function count_de {
    # I made a python script to get the html page from wikipedia and I
    # removed most of the html that does not contain information about
    # de RUG.

    cat wikipedia_text.txt | grep -E -o '\w+' | grep -cw 'de'
    
}

function display_tokens {
    cat used_output.txt | grep -E -o '\w+'
}


count_de
display_tokens
