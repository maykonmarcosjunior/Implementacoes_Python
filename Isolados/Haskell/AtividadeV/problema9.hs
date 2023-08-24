{-
Crie uma fun¸c˜ao com assinatura mapear :: (t -> y) -> [t] -> [y], a qual recebe uma fun¸c˜ao, uma
lista e retorna uma lista. Esta fun¸c˜ao mapear far´a o mesmo que a fun¸c˜ao map, ou seja, aplicar a fun¸c˜ao
recebida como parˆametro sobre cada elemento da lista e retornar a lista resultante. N˜ao utilize map ou
filter para esta tarefa.
-}

mapear :: (t -> y) -> [t] -> [y]
mapear _ [] = [] 
mapear func (a:b) = func a : (mapear func b)

readlist :: [String] -> [Int]
readlist [] = []
readlist (x:xs) = read x : readlist xs

main :: IO ()
main = do
    input <- getLine
    let lista = readlist (words input)
    print (mapear (* 2) lista)
