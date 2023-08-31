{-
Crie uma função que receba três notas de um aluno (a, b, c), 
calcule a média e retorne se o aluno foi aprovado ou reprovado. 
Para um aluno ser aprovado, ele deve possuir nota igual ou superior a 6.
Leia as notas dos alunos do teclado.
-}

aprovado :: Float -> Float -> Float -> String
aprovado n1 n2 n3 = if ((n1 + n2 + n3) / 3) >= 6 then
                        "Aprovado\n"
                    else
                        "Reprovado\n"

main = do
    n1 <- readLn :: IO Float
    n2 <- readLn :: IO Float
    n3 <- readLn :: IO Float
    putStrLn (aprovado n1 n2 n3)
