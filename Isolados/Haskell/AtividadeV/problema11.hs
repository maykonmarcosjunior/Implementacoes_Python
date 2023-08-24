{-
Crie uma fun¸c˜ao com assinatura primeiros :: Int -> [t] -> [t], a qual recebe um n´umero de elementos, uma lista, e retorna uma lista. Esta fun¸c˜ao deve retornar uma lista com os n primeiros elementos
informados no primeiro parˆametro. N˜ao utilize nenhuma fun¸c˜ao pronta to Haskell para esta tarefa.
-}

primeiros :: Int -> [t] -> [t]
primeiros 0 _ = []
primeiros n (a:b) = a : (primeiros (n-1) b)

readlist :: [String] -> [Int]
readlist [] = []
readlist (x:xs) = read x : readlist xs

main :: IO ()
main = do
    input <- getLine
    let lista = readlist (words input)
    print (primeiros 2 lista)
