retab

" delete everything north of main div (basically just the header)
execute "normal! /ma-main-container\<CR>"
normal 0dgg

" delete trailing whitespace
%s/\s\+$//g

" delete blank lines
g/^$/d

" delete the footer
execute "normal! /footer\<CR>"
normal! 0dG

" delete leading whitespace
%s/^\s*//g

" rewrite header and footer
normal gg
-r header.html
normal G$
execute "normal! i>\<CR></body></html"

" strip images to minimize bandwidth consumption
" (sometimes there are like, 75 images that need to be requested)
" g/src="http:\/\/memphisdrumshop/d
g/class="PlayVideoIcon"/normal 2dd

" delete comments (hundreds of lines' worth)
g/^<!--/d

" remove add to cart, add to wishlist, and add to compare texts"
g/add\sto\scart/normal 2dd
g/class="add-to-links"/normal 4dd

" Clean up redundant/useless info
g/class="old-price"/normal 5dd
g/Special\sPrice/d
%s/Model\s\#\s//g
" not a typo, it's really called bradcrumbs :)
execute "normal! /ma-bradcrumbs\<CR>"
normal 13dd
