{-
Crie uma fun¸c˜ao com assinatura diferencaMaiorMenor :: [Int] -> Int, 
a qual recebe uma lista de Int e retorna a diferen¸ca entre o maior e
o menor elemento da lista. Retorne 0 caso a lista for vazia. Não
utilize nenhuma função pronta do Haskell para realizar esta tarefa.
-}

maior_menor :: [Int] -> (Int, Int)
maior_menor [] = (0, 0)
maior_menor [a] = (a, a)
maior_menor (a:b) = 
    let (maior, menor) = maior_menor b
    in
    if a > maior then
        let maior' = a
            menor' = menor
        in (maior', menor')
    else if a < menor then
        let maior' = maior
            menor' = a
        in (maior', menor')
    else
        (maior, menor)


diferencaMaiorMenor :: [Int] -> Int
diferencaMaiorMenor lista = 
    let (maior, menor) = maior_menor lista
    in (maior - menor)

readlist :: [String] -> [Int]
readlist [] = []
readlist (x:xs) = read x : readlist xs

main :: IO ()
main = do
    input <- getLine
    let lista = readlist (words input)
    print (diferencaMaiorMenor lista)
