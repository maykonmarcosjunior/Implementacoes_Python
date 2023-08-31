{-
Crie uma função que receba um número n 
e retorne se o mesmo é primo. 
Leia n do teclado.
-}

div_suss :: Int -> Int -> Bool
div_suss n 1 = True
div_suss n i =
    if (n `mod` i) == 0 then
        False
    else
        div_suss n (i - 1)

ehprimo :: Int -> Bool
ehprimo n = div_suss n (floor (sqrt (fromIntegral n)))

main :: IO ()
main = do
    n <- readLn :: IO Int
    print (ehprimo n)
