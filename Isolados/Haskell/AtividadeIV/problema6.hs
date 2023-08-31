{-
Crie uma função que receba três inteiros x, y e z 
e retorne se havendo varetas com esses valores em 
comprimento pode-se construir um triângulo. 
Exemplo, com varetas de comprimento 4, 8 e 9
posso construir um triângulo, porém 
com varetas de comprimento 10, 5 e 4
não posso construir um triângulo.
Leia x, y e z do teclado.
-}

tribool :: Integer -> Integer -> Integer -> String
tribool l1 l2 l3 = if (l1 < (l2 + l3)) && (l2 < (l1 + l3)) && (l3 < (l2 + l1)) then
                    "Possível"
                   else
                    "Impossível"

main = do
    l1 <- readLn
    l2 <- readLn
    l3 <- readLn
    putStrLn (tribool l1 l2 l3)
