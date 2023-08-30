{--
B: Crie uma fun¸c˜ao com a seguinte assinatura: maioresQueElemento :: Arvore -> Int -> Int, a
qual recebe um n´umero e deve retornar a quantidade de n´umeros maiores que ele na ´arvore.
--}
{--
C: Crie uma fun¸c˜ao com a seguinte assinatura: mediaElementos :: Arvore -> Float, a qual deve
retornar a m´edia dos n´umeros na ´arvore. DICA: utilize a fun¸c˜ao fromIntegral para converter um
tipo inteiro para um tipo compat´ıvel com o operador de divis˜ao /
--}
{--
D: Crie uma fun¸c˜ao com a seguinte assinatura: quantidade :: Arvore -> Int, a qual deve retornar
a quantidade de elementos na ´arvore.
--}
{--
E: Crie uma fun¸c˜ao com a seguinte assinatura: elementos :: Arvore -> [Int], a qual deve retornar
uma lista com todos os elementos na ´arvore
--}
data Arvore = Null | No Int Arvore Arvore

minhaArvore :: Arvore
minhaArvore = No 52 (No 32 (No 12 Null Null) (No 35 Null Null)) (No 56 (No 55 Null Null) (No 64 Null Null))

somaElementos :: Arvore -> Int
somaElementos Null = 0
somaElementos (No n esq dir) = n + (somaElementos esq) + (somaElementos dir)

buscaElemento :: Arvore -> Int -> Bool
buscaElemento Null _ = False
buscaElemento (No n esq dir) x 
    | (n == x) = True                           
    | otherwise = (buscaElemento esq x) || (buscaElemento dir x)

limiteSup :: Int
limiteSup = 1000 --Define um limite superior para o maior número

minimo :: Int -> Int -> Int
minimo x y | (x < y) = x
           | otherwise = y

minimoElemento :: Arvore -> Int
minimoElemento Null = limiteSup 
minimoElemento (No n esq dir) = 
    minimo n (minimo (minimoElemento esq) (minimoElemento dir))
{--
A: Crie uma função com a seguinte assinatura: ocorrenciasElemento :: Arvore -> Int -> Int, a
qual recebe um n´umero e deve retornar a quantidade de ocorrências dele na árvore.
--}

equals :: Int -> Int -> Int
equals x y | (x == y) = 1
           | otherwise = 0

ocorrenciasElemento :: Arvore -> Int -> Int
ocorrenciasElemento Null _ = 0
ocorrenciasElemento (No n esq dir) num = 
    (equals n num) + (ocorrenciasElemento esq num) + (ocorrenciasElemento dir num)

{--
B: Crie uma função com a seguinte assinatura: maioresQueElemento :: Arvore -> Int -> Int, a
qual recebe um número e deve retornar a quantidade de números maiores que ele na árvore.
--}
isBigger :: Int -> Int -> Int
isBigger x y | (x > y) = 1
             | otherwise = 0
maioresQueElemento :: Arvore -> Int -> Int
maioresQueElemento Null _ = 0
maioresQueElemento (No n esq dir) num = 
    (isBigger n num) + (maioresQueElemento esq num) + (maioresQueElemento dir num)

{--
C: Crie uma função com a seguinte assinatura: mediaElementos :: Arvore -> Float,
a qual deve retornar a média dos números na árvore. DICA: utilize a função 
fromIntegral para converter um tipo inteiro para um tipo compatível com o
operador de divisão /
--}
rec_media :: Arvore -> (Int, Int)
rec_media Null = (0, 0)
rec_media (No n esq dir) = 
    let (dirS, dirN) = rec_media dir
        (esqS, esqN) = rec_media esq
    in ((n + dirS + esqS), (1 + dirN + esqN))

mediaElementos :: Arvore -> Float
mediaElementos Null = 0.0
mediaElementos a = 
    let (num, divi) = rec_media a
    in ((fromIntegral num) / (fromIntegral divi))

{--
D: Crie uma função com a seguinte assinatura: quantidade :: Arvore -> Int,
a qual deve retornar a quantidade de elementos na árvore.
--}
quantidade :: Arvore -> Int
quantidade Null = 0
quantidade (No n esq dir) = 1 + (quantidade esq) + (quantidade dir)

{--
E: Crie uma função com a seguinte assinatura: elementos :: Arvore -> [Int],
a qual deve retornar uma lista com todos os elementos na árvore
--}
elementos :: Arvore -> [Int]
elementos Null = []
elementos (No n esq dir) = [n] ++ (elementos esq) ++ (elementos dir)


main :: IO ()
main = do 
    putStrLn "A ="
    putStr "N de ocorrencias de 12 em minhaArvore = "
    print(ocorrenciasElemento minhaArvore 12)
    putStr "N de ocorrencias de 10 em minhaArvore = "
    print(ocorrenciasElemento minhaArvore 10)
    putStrLn "B ="
    putStr "N de elementos maiores que 10 em minhaArvore = "
    print(maioresQueElemento minhaArvore 10)
    putStr "N de elementos maiores que 20 em minhaArvore = "
    print(maioresQueElemento minhaArvore 20)
    putStrLn "C ="
    putStr "Media de elementos em minhaArvore = "
    print(mediaElementos minhaArvore)
    putStrLn "D ="
    putStr "N de elementos em minhaArvore = "
    print(quantidade minhaArvore)
    putStrLn "E ="
    putStr "Elementos em minhaArvore = "
    print(elementos minhaArvore)
