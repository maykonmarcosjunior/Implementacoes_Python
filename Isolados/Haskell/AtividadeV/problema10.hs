{-
 Crie uma fun¸c˜ao com assinatura filtrar :: (t -> Bool) -> [t] -> [t], a qual recebe uma fun¸c˜ao,
uma lista e retorna uma nova lista. Esta fun¸c˜ao aplica a fun¸c˜ao recebida como parˆametro sobre cada
elemento da lista e caso o retorno da fun¸c˜ao for verdadeiro, ent˜ao o elemento far´a parte da nova lista, caso
contr´ario n˜ao. Para esta tarefa, utilize o conceito de list comprehension.
-}

filtrar :: (t -> Bool) -> [t] -> [t]
filtrar func lista = [x | x <- lista, (func x)]

readlist :: [String] -> [Int]
readlist [] = []
readlist (x:xs) = read x : readlist xs

main :: IO ()
main = do
    input <- getLine
    let lista = readlist (words input)
    print (filtrar (> 2) lista)
