@echo off

FOR /L %%i IN (1, 1, 10) DO (
    python . %%i -w -v
)
