{-
 Crie uma função com assinatura ocorrencias :: [Int] -> Int -> Int, a qual recebe uma lista de
Int e um Int e retorna o número de vezes em que o elemento está presente na lista. Não utilize nenhuma
função pronta do Haskell para realizar esta tarefa.
-}
ocorrencias :: [Int] -> Int -> Int
ocorrencias [] _ = 0
ocorrencias (a:b) c
    | (a == c) = 1 + (ocorrencias b c)
    | otherwise = 0 + (ocorrencias b c)


readlist :: [String] -> [Int]
readlist [] = []
readlist (x:xs) = read x : readlist xs

main :: IO ()
main = do
    input <- getLine
    c <- readLn :: IO Int
    let lista = readlist (words input)
    print (ocorrencias lista c)
