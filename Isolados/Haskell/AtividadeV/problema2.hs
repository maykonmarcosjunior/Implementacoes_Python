{-
Crie uma função com assinatura media :: [Int] -> Float, a qual recebe uma lista de Int e retorna
a média de todos os elementos da lista. Retorne 0 caso a lista for vazia. N˜ao utilize nenhuma fun¸c˜ao
pronta do Haskell para realizar esta tarefa. DICA: utilize a fun¸c˜ao fromIntegral para converter um tipo
inteiro para um tipo compat´ıvel com o operador de divis˜ao /
-}

rec_med :: [Int] -> (Int, Int)
rec_med [] = (0, 0)
rec_med (a:b) = 
    let (newA, cont) = (rec_med b) 
    in ((a + newA), (cont + 1))

media :: [Int] -> Float
media [] = 0
media (cab:cau) = 
    let (num, den) = (rec_med (cab:cau))
    in ((fromIntegral num) / (fromIntegral den))

readlist :: [String] -> [Int]
readlist [] = []
readlist (x:xs) = read x : readlist xs

main :: IO ()
main = do
    input <- getLine
    let lista = readlist (words input)
    print (media lista)
