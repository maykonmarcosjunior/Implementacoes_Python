{-
Crie uma função que receba dois números x e y 
e retorne se x é divisível por y. Leia x e y do teclado.
-}

divide :: Int -> Int -> Bool
divide _ 0 = False
divide 0 _ = False
divide x y = ((x `mod` y) == 0)

main :: IO ()
main = do
    x <- readLn :: IO Int
    y <- readLn :: IO Int
    print(divide x y)
