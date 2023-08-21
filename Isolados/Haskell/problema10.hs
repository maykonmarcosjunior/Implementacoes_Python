{-
Crie uma função que receba 3 valores numéricos (a, b, c) 
e retorne o maior deles. Não utilize nenhuma forma de ordenação. 
Leia os valores a, b, c do teclado
-}

maior :: Ord x => x -> x -> x -> x
maior a b c
    | (a >= b && a >= c) = a
    | (b >= a && b >= c) = b
    | otherwise = c

main = do
    a <- readLn :: IO Integer
    b <- readLn :: IO Integer
    c <- readLn :: IO Integer
    print(maior a b c)
