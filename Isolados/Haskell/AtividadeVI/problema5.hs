{--
Pesquise o que o newtype. Qual é a diferença dele para o type e para o data?
Faça um pequeno exemplo de aplicação e explique seu funcionamento.
--}

-- dessa forma garante que não sejam usados
-- de forma intercambiável
newtype USD = USD Double
newtype BRL = BRL Double

convertToBRL :: USD -> BRL
convertToBRL (USD amount) = BRL (amount * 5.0)
convertToUSD :: BRL -> USD
convertToUSD (BRL amount) = USD (amount * 0.2)

-- Funções para somar valores de USD e BRL
addUSD :: USD -> USD -> USD
addUSD (USD a) (USD b) = USD (a + b)
addBRL :: BRL -> BRL -> BRL
addBRL (BRL a) (BRL b) = BRL (a + b)

instance Show USD where
    show (USD x) = show x
instance Show BRL where
    show (BRL x) = show x

main = do
    let dolar = (USD 1)
    let real = (BRL 1)
    putStr "Valor em reais = "
    print (addBRL real (convertToBRL dolar))
    putStr "Valor em dolares = "
    print (addUSD dolar (convertToUSD real))
