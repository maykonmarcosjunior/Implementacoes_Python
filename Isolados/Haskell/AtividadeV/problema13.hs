{-
Crie uma fun¸c˜ao com assinatura apagarEnquanto :: (t -> Bool) -> [t] -> [t], a qual recebe uma
fun¸c˜ao como parˆametro e uma lista, e retorna uma lista. Esta fun¸c˜ao deve aplicar a fun¸c˜ao passada como
parˆametro a cada elemento da lista, at´e que algum elemento da lista retorne False na aplica¸c˜ao da fun¸c˜ao.
Os elementos da lista resultante s˜ao ent˜ao todos os elementos a partir do elemento em que a fun¸c˜ao passada
como parˆametro retornou False. Por exemplo a chamada (apagarEnquanto par [2,4,1,2,3,4,5])
deve retornar [1,2,3,4,5], visto que ao testar o elemento 1, a fun¸c˜ao par retorna False. N˜ao utilize
nenhuma fun¸c˜ao pronta to Haskell para esta tarefa.
-}

apagarEnquanto :: (t -> Bool) -> [t] -> [t]
apagarEnquanto _ [] = []
apagarEnquanto func (a:b) = 
    if (func a) then
        a : (apagarEnquanto func b)
    else
        []

readlist :: [String] -> [Int]
readlist [] = []
readlist (x:xs) = read x : readlist xs

main :: IO ()
main = do
    input <- getLine
    let lista = readlist (words input)
    print (apagarEnquanto (< 4) lista)
