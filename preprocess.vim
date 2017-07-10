retab

" delete everything north of main div (basically just the header)
execute "normal! /ma-main-container\<CR>"
execute "normal! 0dgg"

" delete trailing whitespace
%s/\s\+$//g

" delete blank lines
g/^$/d

" delete the footer
execute "normal! /footer\<CR>"
execute "normal! 0dG"

" delete leading whitespace
%s/^\s*//g

" at least make a passing attempt at standards conformance
execute "normal! ggi<html>\<CR><body>\<CR>"
execute "normal! G$i></body>\<CR></html>\<ESC>x"

" strip images to minimize bandwidth consumption
" (sometimes there are like, 75 images that need to be requested)
g/src="http:\/\/memphisdrumshop/d
