{-
Crie uma função com assinatura busca :: [Int] -> Int -> Bool, a qual recebe uma lista de Int e um
Int e retorna se o elemento passado como parâmetro encontra-se na lista ou não. Não utilize nenhuma
função pronta do Haskell para realizar esta tarefa.
-}
busca :: [Int] -> Int -> Bool
busca [] _ = False
busca (a:b) c
    | (a == c) = True
    | otherwise = (busca b c)

readlist :: [String] -> [Int]
readlist [] = []
readlist (x:xs) = read x : readlist xs

main :: IO ()
main = do
    input <- getLine
    c <- readLn :: IO Int
    let lista = readlist (words input)
    print (busca lista c)

