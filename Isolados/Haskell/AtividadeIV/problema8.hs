{-
Crie uma função que resolva uma equação de segundo grau 
da forma ax2 + bx + c utilizando a fórmula de Bhaskara. 
Leia os coeficientes a, b e c do teclado.
-}

bhaskara :: Float -> Float -> Float -> (Float, Float)
bhaskara a b c = 
    let delta = (sqrt ((b*b) - (4*a*c)))
        x1 = (-b + delta) / (2*a)
        x2 = (-b - delta) / (2*a)
    in (x1, x2)

main = do
    a <- readLn :: IO Float
    b <- readLn :: IO Float
    c <- readLn :: IO Float
    let (x1, x2) = (bhaskara a b c)
    putStrLn "x1 = "
    print(x1)
    putStrLn "x2 = "
    print(x2)
