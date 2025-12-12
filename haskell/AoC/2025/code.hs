import Data.List
import System.IO

main10 :: IO ()
main10 = do 
    content <- readFile "haskell\\AoC\\2025\\input1.txt"
    let ls = lines content
    let inst = map convertLR ls 
    let dial = applie inst []
    let sol = countZeros dial
    print sol

convertLR :: [Char] -> Int
convertLR ('R':xs) = read xs :: Int
convertLR ('L':xs) = (read xs :: Int) * (-1)

applie :: [Int] -> [Int] -> [Int]
applie [] ys = reverse ys
applie xs [] = applie xs [50]
applie (x:xs) (y:ys) = applie xs (modAdd x y :(y:ys))

modAdd :: Int -> Int -> Int
modAdd x y = mod (x + y) 100

countZeros :: [Int] -> Int
countZeros = sum.(map findZero)

findZero :: Int -> Int
findZero 0 = 1
findZero _ = 0


main11 :: IO ()
main11 = do 
    content <- readFile "haskell\\AoC\\2025\\input1.txt"
    let ls = lines content
    let inst = map convertLR_ ls 
    let dial = applie_ inst []
    let sol = snd $ last dial
    print sol

convertLR_ :: [Char] -> (Int,Int)
convertLR_ ('R':xs) = (1,read xs :: Int)
convertLR_ ('L':xs) = ((-1),read xs :: Int)

countRot :: (Int, Int) -> (Int, Int) -> (Int, Int)
countRot tu (s, 0)     = tu
countRot (0, i) (s, n) = countRot (s, i+1) (s, n-1)
countRot (c, i) (s, n) = countRot (mod (c+s) 100, i) (s, n-1)

applie_ :: [(Int, Int)] -> [(Int, Int)] -> [(Int, Int)]
applie_ [] ys = reverse ys
applie_ xs [] = applie_ xs [(50, 0)]
applie_ (x:xs) (y:ys) = applie_ xs (countRot y x :(y:ys))



main20 :: IO ()
main20 = do
    content <- readFile "haskell\\AoC\\2025\\input2.txt"
    let ls = splitString content []
    let interval = concat (map makeInterval ls)
    let filtered = map check11 interval
    let sol = sum filtered
    print sol

strTup :: ([Char], [Char]) -> [Char] -> ([Char], [Char])
strTup (ys,_) ('-':xs) = (ys,xs)
strTup (ys,_) (x:xs)   = strTup (ys ++ [x],[]) (xs)

convertInt :: ([Char], [Char]) -> (Int, Int)
convertInt (xs, ys) = (read xs :: Int, read ys :: Int)

makeInt :: [Char] -> (Int, Int)
makeInt = convertInt.(strTup ("",""))

makeList :: (Int, Int) -> [Int]
makeList (x,y) = [x..y]

makeInterval :: [Char] -> [Int]
makeInterval = makeList.makeInt

check11 :: Int -> Int
check11 n = let text = show n
                len  = length text
            in case even len of 
                False -> 0
                True  -> let l = div len 2
                             x = read (take l text) :: Int
                             y = read (drop l text :: [Char]) :: Int
                         in case x == y of
                            False -> 0
                            True  -> n

splitString :: [Char] -> [Char] -> [[Char]]
splitString [] ys = [ys]
splitString (',':xs) ys = ys : splitString xs []
splitString (x:xs) ys   = splitString xs (ys++[x]) 


main21 :: IO ()
main21 = do
    content <- readFile "haskell\\AoC\\2025\\input2.txt"
    let ls = splitString content []
    let interval = concat (map makeInterval ls)
    let filtered = filter (\x -> let y = show x in findReps (removeImp (getAlt y)) y) interval
    let sol = sum filtered
    print sol

split :: [Char] -> [[Char]]
split [] = []
split (x:xs) = [[x]] ++ split xs

getAlt :: [Char] -> [[Char]]
getAlt xs = let l = length xs 
            in map (\x -> concat (take x (split xs))) [1..l]

removeImp :: [[Char]] -> [[Char]]
removeImp xs = let l = length xs
               in init (filter (\x -> (rem l (length x)) == 0) xs)

findRep :: [Char] -> [Char] -> Bool
findRep xs [] = True
findRep xs ys = let l = length xs
                in case (take l ys) == xs of
                    True  -> findRep xs (drop l ys)
                    False -> False

findReps :: [[Char]] -> [Char] -> Bool
findReps [] y = False
findReps (x:xs) y = or (findRep x y : [findReps xs y])



main30 :: IO ()
main30 = do
    content <- readFile "haskell\\AoC\\2025\\input3_test.txt"
    let ls = lines content 
    let lsInt = map strToInt ls
    print lsInt

strToInt :: [Char] -> [Int]
strToInt [] = []
strToInt (x:xs) = (read [x] :: Int) : strToInt xs

firstNumber :: [Int] -> Int
firstNumber = head.reverse.sort.init
