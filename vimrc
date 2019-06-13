
set number
"set colorcolumn=80
set tabstop=4
set sw=2
set expandtab
set listchars=tab:\|\
set list
set cursorcolumn
syntax on

colorscheme darkblue
highlight CursorColumn ctermbg=red

set nocompatible
" Initialisation de pathogen
call pathogen#infect()
call pathogen#helptags()

set number

filetype plugin indent on
syntax on
runtime! config/**/*.vim


set backspace=indent,eol,start

set cursorline
set cursorcolumn

fu! ToggleCurline ()
  if &cursorline && &cursorcolumn
    set nocursorline
    set nocursorcolumn
  else
    set cursorline
    set cursorcolumn
  endif
endfunction

map <silent><leader>cl :call ToggleCurline()<CR>

set pastetoggle=<F6>

autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif

