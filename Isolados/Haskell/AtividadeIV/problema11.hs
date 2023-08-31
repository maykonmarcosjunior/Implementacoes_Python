{-
Crie uma função que receba dois números x e y 
e retorne o máximo divisor comum 
(DICA: pesquise sobre o Algoritmo de Euclides). 
Leia x e y do teclado.
-}

mdc :: Integer -> Integer -> Integer
mdc x 0 = x
mdc x y = (mdc y (x `mod` y))

main :: IO ()
main = do
    x <- readLn :: IO Integer
    y <- readLn :: IO Integer
    print(mdc x y)
