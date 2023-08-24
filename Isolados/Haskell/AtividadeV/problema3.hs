{-
 Crie uma função com assinatura menor :: [Int] -> Int, a qual recebe uma lista de Int e retorna o
menor elemento da lista. Retorne 0 caso a lista for vazia. N˜ao utilize nenhuma fun¸c˜ao pronta do Haskell
para realizar esta tarefa.
-}

menor :: [Int] -> Int
menor [] = 0
menor [a] = a
menor (a:b) = 
    let c = (menor b)
    in 
    if c < a then
        c
    else
        a

readlist :: [String] -> [Int]
readlist [] = []
readlist (x:xs) = read x : readlist xs

main :: IO ()
main = do
    input <- getLine
    let lista = readlist (words input)
    print (menor lista)
