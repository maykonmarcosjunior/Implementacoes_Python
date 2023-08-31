{-
Crie uma função que receba dois números x e y 
e retorne o mínimo múltiplo comum 
(DICA: use a função do máximo divisor comum já criada). 
Leia x e y do teclado.
-}


mdc :: Integer -> Integer -> Integer
mdc x 0 = x
mdc x y = (mdc y (x `mod` y))

mmc :: Integer -> Integer -> Integer
mmc x y = ((x*y) `div` (mdc x y))

main :: IO ()
main = do
    x <- readLn :: IO Integer
    y <- readLn :: IO Integer
    print(mmc x y)
