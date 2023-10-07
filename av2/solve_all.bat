@echo off

SET main_dir=%base_dir:~0,-1%
echo %main_dir%

FOR /L %%i IN (1, 1, 10) DO (
    python "%main_dir%" %%i -w
)