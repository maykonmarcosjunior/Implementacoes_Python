{- 
Crie uma função que receba dois números
x e y e retorne xy. Leia x e y do teclado.
-}
potencia :: Integer -> Integer -> Integer
potencia x y = (x ^ y)

main = do
    x <- readLn
    y <- readLn
    print(potencia x y)
