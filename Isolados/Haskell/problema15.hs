{-
Crie uma função que receba um número n 
e retorne a função totiente de Euler (φ(n)). 
A função totiente de Euler é dada pelo 
número de inteiros positivos r a partir de 1 
e menores que n, ou seja 1 <= r < n, 
que são coprimos de n. Por exemplo, se n = 10, 
então os coprimos de 10 de 1 até 10-1 são {1, 3, 7, 9} 
e a função deve retornar φ(n) = 4. Leia n do teclado.
-}

mdc :: Int -> Int -> Int
mdc x 0 = x
mdc x y = (mdc y (x `mod` y))

totiente :: Int -> Int
totiente 0 = 0
totiente n = length [x | x <- [1..n], (mdc x n) == 1]

main :: IO ()
main = do
    n <- readLn :: IO Int
    print(totiente n)
