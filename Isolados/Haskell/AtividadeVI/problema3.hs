{--
Crie um novo tipo Ponto, usando data, que pode ser
um ponto 2D ou um ponto 3D. Depois, crie uma função 
que receba dois pontos (necessariamente ambos sendo 2D
ou ambos sendo 3D), e retorne a distância entre eles.
--}

data Ponto = D2 Float Float | D3 Float Float Float

distancia :: Ponto -> Ponto -> Float
distancia (D2 x1 y1) (D2 x2 y2) = sqrt (((x1 - x2)**2) + ((y1 - y2)**2))
distancia (D3 x1 y1 z1) (D3 x2 y2 z2) = sqrt (((x1 - x2)**2) + ((y1 - y2)**2) + ((z1 - z2)**2))



main :: IO ()
main = do
    let p1 = (D2 0.0 0.0)
    let p2 = (D2 1.0 2.0)
    let p3 = (D3 0.0 0.0 0.0)
    let p4 = (D3 1.0 1.0 2.0)
    print (distancia p1 p2)
    print (distancia p3 p4)
