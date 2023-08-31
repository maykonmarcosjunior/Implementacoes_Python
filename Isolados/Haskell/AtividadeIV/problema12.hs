{-
Crie uma função que receba três números x, y e z 
e retorne o máximo divisor comum (DICA: apenas
modifique o algoritmo anterior). 
Leia x, y e z do teclado.
-}


mdc :: Integer -> Integer -> Integer
mdc x 0 = x
mdc x y = (mdc y (x `mod` y))

mdc3 :: Integer -> Integer -> Integer -> Integer
mdc3 x y z = (mdc (mdc x y) z)

main :: IO ()
main = do
    x <- readLn :: IO Integer
    y <- readLn :: IO Integer
    z <- readLn :: IO Integer
    print(mdc3 x y z)
