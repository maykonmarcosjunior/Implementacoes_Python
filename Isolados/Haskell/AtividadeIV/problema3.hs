{-
Crie uma função que receba a base e a altura de um triângulo
e calcule a área do mesmo. Leia a base e a altura do teclado.
-}


areaTri :: Float -> Float -> Float
areaTri base altura = ((base * altura) / 2)

main = do
    base <- readLn :: IO Float
    altura <- readLn :: IO Float
    print(areaTri base altura)
