{-
A conjetura de Goldbach diz que todo número inteiro par
maior que 2 pode ser expressado como a soma de dois números primos.
Embora ela nunca foi provada ser verdadeira, ela funciona para números grandes.
Por exemplo, podemos escrever o número 14 como a soma de 7 e 7, ou 18 como a soma de 5 e 13. 
Implemente uma função que receba um número n como parâmetro e retorne um dos números primos que
fazem parte da soma. Ex: retorne 5 ou 13 para o caso do número 18. Leia n do teclado.
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

sub_suss :: Int -> Int -> Int
sub_suss x y
    | ((ehprimo x) && (ehprimo y)) = x
    | otherwise = sub_suss (x - 1) (y + 1)

goldbach :: Int -> Int
goldbach n = (sub_suss (n-3) 3)

main :: IO ()
main = do
    n <- readLn :: IO Int
    print (goldbach n)
