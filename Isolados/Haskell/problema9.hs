{-
Crie uma função que dados dois pontos no espaço 3D, 
(x1, y1, z1) e (x2, y2, z2), compute a distância entre eles. 
Leia as posições dos pontos do teclado.
-}

deltaD :: Floating a => (a, a, a) -> (a, a, a) -> a
deltaD x1 y1 z1 x2 y2 z2 = 
    let dx = (x2 - x1)
        dy = (y2 - y1)
        dz = (z2 - z1)
    in (sqrt ((dx ** 2) + (dy ** 2) + (dz ** 2)))

main = do
    x1 <- readLn :: IO Float
    y1 <- readLn :: IO Float
    z1 <- readLn :: IO Float
    x2 <- readLn :: IO Float
    y2 <- readLn :: IO Float
    z2 <- readLn :: IO Float
    print(deltaD x1 y1 z1 x2 y2 z2)
