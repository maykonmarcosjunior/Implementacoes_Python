{-
Crie uma função que receba três parâmetros 
Operador, x e y, e retorne o resultado 
da operação matemática x Operador y. 
Os operadores possíveis de informar são 
+, -, *, /. Leia o Operador, x e y do teclado.
-}

operacao :: String -> Float -> Float -> Float
operacao operador x y
    | (operador == "+") = (x + y)
    | (operador == "-") = (x - y)
    | (operador == "*") = (x * y)
    | (operador == "/") = (x / y)

main :: IO ()
main = do
    operador <- getLine
    x <- readLn :: IO Float
    y <- readLn :: IO Float
    print(operacao operador x y)
