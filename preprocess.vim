retab

" delete everything north of 3964
3964
execute "normal! dgg"

" delete trailing whitespace
%s/\s\+$//g

" delete blank lines
g/^$/d

" delete the footer
execute "normal! /footer\<CR>"
execute "normal! 0dG"

" delete leading whitespace
%s/^\s*//g
