{-
Motifique o arquivo alunos.hs (dispon´ıvel no Moodle) de forma a adicionar novas fun¸c˜oes:
A: Crie uma fun¸c˜ao com a seguinte assinatura: aprovados :: [(Int, String, Float)] -> [String],
a qual recebe uma lista de alunos e retorna uma lista com o nome dos alunos aprovados. Um aluno
est´a aprovado se a sua m´edia ´e maior ou igual a 6. Utilize map e filter para resolver esta quest˜ao.

B: Crie uma fun¸c˜ao com a seguinte assinatura: aprovados2 :: [(Int, String, Float)] -> [String],
a qual recebe uma lista de alunos e retorna uma lista com o nome dos alunos aprovados. Um aluno
est´a aprovado se a sua m´edia ´e maior ou igual a 6. N˜ao utilize map e filter para resolver esta
quest˜ao. Utilize o conceito de list comprehension.

C: Utilize (e modifique, se necess´ario) a fun¸c˜ao gerarPares vista em aula e dispon´ıvel no arquivo
alunos.hs para formar duplas de alunos. Note que um aluno n˜ao pode fazer dupla consigo mesmo.
-}

alunos :: [(Int, String, Float)]
alunos = [(1, "Ana", 3.4), (2, "Bob", 6.7), (3, "Tom", 7.6)]

getNome :: (Int, String, Float) -> String
getNome (a,b,c) = b

getPrimeiroAluno :: [(Int, String, Float)] -> (Int, String, Float)
getPrimeiroAluno (a:_) = a

gerarPares :: [(Int, String, Float)] -> [(Int, String, Float)] -> [((Int, String, Float),(Int, String, Float))] 
gerarPares l1 l2 = [(a,b) | a <- l1, b <- l2, (a /= b)]

aprovado_al :: (Int, String, Float) -> Bool
aprovado_al (_, _, nota) = (nota >= 6.0)

aprovados :: [(Int, String, Float)] -> [String]
aprovados lista = (map getNome (filter (aprovado_al) lista))

aprovados2 :: [(Int, String, Float)] -> [String]
aprovados2 lista = [(getNome a) | a <- lista, (aprovado_al a)]

aprovados3 :: [(Int, String, Float)] -> [String]
aprovados3 [] = []
aprovados3 (a:b) =
    if (aprovado_al a) then
        [(getNome a)] ++ (aprovados3 b)
    else
        (aprovados3 b)

main :: IO ()
main = do
    print (aprovados alunos)
    print (aprovados2 alunos)
    print (gerarPares alunos alunos)
