{--
1. Crie um tipo de dados Aluno, usando type, assim como criamos um tipo de dados Pessoa. O tipo Aluno
deve possuir um campo para o nome, outro para a disciplina e outros trˆes campos para notas. Agora,
execute os passos abaixo:
A: Crie uma fun¸c˜ao no mesmo estilo que a fun¸c˜ao pessoa, vista em sala e dispon´ıvel nos slides no Moodle,
ou seja, que receba um inteiro e retorne um Aluno correspondente ao valor inteiro.
B: Crie alguns alunos de exemplo, assim como tamb´em feito no exemplo da pessoa.
C: No main, imprima o primeiro nome de um aluno, portanto crie uma fun¸c˜ao para obter o primeiro
nome.
D: Crie uma fun¸c˜ao que receba um Int e retorne a m´edia do aluno correspondente.
E: Crie uma fun¸c˜ao que calcule a m´edia da turma, ou seja, considerando todos os alunos. DICA: crie
uma fun¸c˜ao recursiva que receba o primeiro identificador de aluno e incremente o identificador a cada
chamada recursiva, at´e chegar no ´ultimo aluno. N˜ao use listas!
--}
type Nome = String
type Disciplina = String
type Notas = Float
type Aluno = (Nome, Disciplina, Notas, Notas, Notas)

aluno :: Int -> Aluno
aluno 0 = ("Joao0", "Mat0", 0.0, 0.0, 0.0)
aluno 1 = ("Joao1", "Mat1", 1.0, 1.5, 3.0)
aluno 2 = ("Joao2", "Mat2", 1.0, 2.5, 4.0)
aluno n = (("Joao" ++ (show n)),
            ("Mat" ++ (show n)),
            (fromIntegral n),
            (fromIntegral (n-2)),
            (fromIntegral (n+3))
        )

getNome :: Aluno -> Nome
getNome (n, _, _, _, _) = n

getMedia :: Aluno -> Notas
getMedia (_, _, n1, n2, n3) = (n1 + n2 + n3) / 3

rec_getMediaTurma :: Int -> Float
rec_getMediaTurma 0 = 0.0
rec_getMediaTurma n = ((getMedia (aluno n)) + (rec_getMediaTurma (n-1)))
getMediaTurma :: Int -> Float
getMediaTurma n = ((rec_getMediaTurma n)) / (fromIntegral n)

main :: IO ()
main = do
    let ex0 = (aluno 0)
    let ex1 = (aluno 1)
    let ex2 = (aluno 2)
    let ex3 = (aluno 5)
    print(ex0)
    print(ex1)
    print(ex2)
    putStrLn (getNome ex0)
    print(getMedia ex0)
    print(getMedia ex1)
    print(getMedia ex2)
    print(getMedia (aluno 8))
    print(getMedia (aluno 7))
    print(getMedia (aluno 6))
    print(getMedia (aluno 5))
    putStrLn "Média da turma com 8 alunos:"
    print(getMediaTurma 8)
