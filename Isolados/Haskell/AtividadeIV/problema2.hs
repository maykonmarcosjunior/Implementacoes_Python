{-
Crie uma função que receba um número x,
negativo ou positivo, e retorne seu valor absoluto.
Leia x do teclado.
-}

modulo :: Integer -> Integer
modulo x   | (x < 0) = -x
           | otherwise = x

main = do
    x <- readLn
    print(modulo x)
