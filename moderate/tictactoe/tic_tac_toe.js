function getWinner(board, n){
  let diagonalWinner = getDiagonalWinner(board, n)
  if (diagonalWinner)
    return diagonalWinner

  let horizontalWinner = getHorizontalWinner(board, n)

  if (horizontalWinner)
    return horizontalWinner

  let verticalWinner = getVerticalWinner(board, n)
  return verticalWinner
}

function getDiagonalWinner(board, n) {
  let topLeftDiagonal = []
  for (let i=0; i<n; i++)
    topLeftDiagonal.push(board[i][i])

  let winner = getLineWinner(topLeftDiagonal, n)

  if (winner)
    return winner

  let topRightDiagonal = []
  for (let i = n-1; i >= 0; --i)
    topRightDiagonal.push(board[i][i])

  return getLineWinner(topRightDiagonal, n)
}

function getHorizontalWinner(board, n) {
  for (let rowIndex = 0; rowIndex < n; ++rowIndex) {
    var winner = getLineWinner(board[rowIndex], n)
    if (winner)
      return winner
  }

  return null
}

function getVerticalWinner(board, n) {
  for (let columnIndex = 0; columnIndex < n; ++columnIndex) {
    var line = []
    for(let rowIndex = 0; rowIndex < n; ++rowIndex)
      line.push(board[columnIndex][rowIndex])

    var winner = getLineWinner(line, n)
    if (winner)
      return winner
  }

  return null
}

function getLineWinner(line, n) {
  let winnerCandidate = line[0]

  for (let i = 1; i < n; i++) {
    if (winnerCandidate != line[i])
      return null
  }

  return winnerCandidate
}

function assertEqual(got, expected) {
  if (got == expected)
    console.log('GOOD')
  else
    console.log(`BAD got: ${got}, expected ${expected}`)
}

// test with n = 3
var board = []
board[0] = ['x', 'o', 'o']
board[1] = ['o', 'x', 'x']
board[2] = ['o', 'o', 'o']
assertEqual(getDiagonalWinner(board, 3), null)

var line = ['x', 'o', 'x']
assertEqual(getLineWinner(line, 3), null)

var line = ['o', 'o', 'o']
assertEqual(getLineWinner(line, 3), 'o')

var line = ['o', 'o', 'x']
assertEqual(getLineWinner(line, 3), null)

var line = ['x', 'x', 'o']
assertEqual(getLineWinner(line, 3), null)

var board = []
board[0] = ['x', 'o', 'x']
board[1] = ['x', 'x', 'x']
board[2] = ['o', 'x', 'o']
assertEqual(getWinner(board, 3), 'x')

var board = []
board[0] = ['o', 'o', 'o']
board[1] = ['o', 'x', 'x']
board[2] = ['x', 'o', 'o']
assertEqual(getWinner(board, 3), 'o')

var board = []
board[0] = ['x', 'o', 'o']
board[1] = ['o', 'x', 'x']
board[2] = ['x', 'o', 'o']
assertEqual(getWinner(board, 3), null)

var board = []
board[0] = ['x', 'o', 'x']
board[1] = ['o', 'x', 'x']
board[2] = ['x', 'o', 'o']
assertEqual(getWinner(board, 3), 'x')



// tests with n=4
var board = []
board[0] = ['x', 'o', 'x', 'o']
board[1] = ['x', 'x', 'x', 'o']
board[2] = ['o', 'o', 'x', 'o']
board[3] = ['x', 'o', 'x', 'x']
assertEqual(getWinner(board, 4), 'x')

var board = []
board[0] = ['o', 'o', 'o', 'o']
board[1] = ['o', 'x', 'x', 'o']
board[2] = ['o', 'o', 'o', 'o']
board[3] = ['o', 'o', 'x', 'o']
assertEqual(getWinner(board, 4), 'o')

var board = []
board[0] = ['x', 'o', 'o', 'o']
board[1] = ['o', 'x', 'x', 'o']
board[2] = ['x', 'o', 'o', 'o']
board[3] = ['x', 'o', 'x', 'o']
assertEqual(getWinner(board, 4), null)