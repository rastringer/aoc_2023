import Data.Char (isDigit)
import Control.Monad (guard)



readMatrix :: FilePath -> IO [String]
readMatrix filePath = lines <$> readFile filePath

type Matrix = [String]

main :: IO ()
main = do
  matrix <- readMatrix "input.txt"
  mapM_ putStrLn matrix
  putStrLn $ "Rows in matrix: " ++ show (length matrix)
  let symbols = ['*', '#', '@', '$', '%'] 
  let result = findAdjacent matrix symbols
  putStrLn $ "Numbers adjacent to " ++ show symbols ++ ": " ++ show result

isSymbol :: Char -> Bool 
isSymbol c = c /= '.' 

neighbours :: Matrix -> Int -> Int -> [Char]
neighbours matrix row col = do
    r <- [row - 1 .. row + 1]
    c <- [col - 1 .. row + 1]
      -- Check if the indices are valid and not equal to the current position

    guard (0 <= r && r < length matrix && 0 <= c && c < length (matrix !! r) && (r /= row || c /= col))
    return (matrix !! r !! c)

-- Function to find numbers adjacent to a symbol
findAdjacent :: Matrix -> [Char] -> [(Int, Int, Char)]
findAdjacent matrix symbols =
  [(r, c, matrix !! r !! c) | r <- [0 .. length matrix - 1], c <- [0 .. length (matrix !! r) - 1],
    isSymbol (matrix !! r !! c) && matrix !! r !! c /= '.',
    any isDigit (neighbours matrix r c),
    matrix !! r !! c `elem` symbols]