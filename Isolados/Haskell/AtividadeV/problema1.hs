{-
 Crie uma função com assinatura soma :: [Int] -> Int, a qual recebe uma lista de Int e retorna a soma
de todos os elementos da lista. Retorne 0 caso a lista for vazia. Não utilize nenhuma função pronta do
Haskell para realizar esta tarefa.
-}

soma :: [Int] -> Int
soma [] = 0
soma (cabeca:cauda) = cabeca + (soma cauda)

readlist :: [String] -> [Int]
readlist [] = []
readlist (x:xs) = read x : readlist xs

main :: IO ()
main = do
    input <- getLine
    let lista = readlist (words input)
    print (soma lista)
