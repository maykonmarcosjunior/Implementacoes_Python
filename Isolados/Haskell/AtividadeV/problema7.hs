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


main :: IO ()
main = do

