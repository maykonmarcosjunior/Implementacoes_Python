{-
Crie uma função que compute o n-ésimo
número de Fibonacci. Leia n do teclado.
-}

fibonacci_nrec :: Integer -> Integer
fibonacci_nrec n = 
    let raiz5 = (sqrt 5)
        phi = ((1 + raiz5) / 2)
        psi = ((1 - raiz5) / 2)
        num = ((phi ^ n) - (psi ^ n))
        x = (num / raiz5)
    in round x

fibonacci :: Integer -> Integer
fibonacci 1 = 1
fibonacci 2 = 1
fibonacci n = (fibonacci (n-1)) + (fibonacci (n-2))

main = do
    n <- readLn :: IO Integer
    print(fibonacci n)
