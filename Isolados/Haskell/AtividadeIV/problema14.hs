{-
Crie uma função que receba dois números x e y 
e determine se eles são coprimos. 
Dois números são ditos coprimos se o máximo divisor 
comum entre eles é 1. Leia x e y do teclado.
-}

mdc :: Integer -> Integer -> Integer
mdc x 0 = x
mdc x y = (mdc y (x `mod` y))

coprimos :: Integer -> Integer -> Bool
coprimos x y = ((mdc x y) == 1)

main :: IO ()
main = do
    x <- readLn :: IO Integer
    y <- readLn :: IO Integer
    print(coprimos x y)

