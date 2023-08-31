{-
Crie uma função que receba dois valores booleanos (x, y)
retorne o resultado do “ou exclusivo” (XOR) sobre eles. 
A função apenas deve usar os operadores &&, || e not. 
Leia os valores x e y do teclado.
-}


xor :: Bool -> Bool -> Bool
xor x y = ((x && not y) || (y && not x))

main = do
    x <- readLn
    y <- readLn
    print(xor x y)
