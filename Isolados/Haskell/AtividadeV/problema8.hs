{-
 Crie uma fun¸c˜ao com assinatura inverte :: [t] -> [t], a qual recebe uma lista como parˆametro e
deve retornar a mesma invertida. N˜ao utilize nenhuma fun¸c˜ao pronta do Haskell para realizar esta tarefa.
-}

inverte :: [t] -> [t]
inverte [] = []
inverte (a:b) = (inverte b ++ [a]) 

readlist :: [String] -> [Int]
readlist [] = []
readlist (x:xs) = read x : readlist xs

main :: IO ()
main = do
    input <- getLine
    let lista = readlist (words input)
    print (inverte lista)
