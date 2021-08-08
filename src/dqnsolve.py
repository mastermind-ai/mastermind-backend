from mastermind import *
from DeepQN import *

mastermind = Mastermind()
stateDim = len(mastermind.color_code)*len(mastermind.colors) + 3*len(mastermind.color_code)
actionDim = len(mastermind.colorPairs)
dqn = DQN(stateDim=stateDim,actionDim=actionDim)
maxAttempt = 20

def feebackToColors(feedback):
    feedbackList = []
    for value in feedback:
        if value == 0:
            feedbackList.append("default")
        elif value == 1:
            feedbackList.append("white")
        elif value == 2:
            feedbackList.append("black")
    return feedbackList


def dqn_start(answer):
    board, state = [],[]
    mastermind.reset()
    mastermind.color_code = answer

    guessedCode = random.sample(mastermind.colors,4) # Inital guess is randomized

    feedback = mastermind.guess(guessedCode)
    # print("AI guess:",guessedCode,"Feedback:",feedback)

    curState = mastermind.code2state(guessedCode, feedback)

    board.append(guessedCode)
    state.append(feebackToColors(feedback))

    while (not mastermind.win) and (mastermind.attempts <= maxAttempt):
        # make a guess
        action = dqn.chooseAction(curState, True)
        guessedCode = mastermind.colorPairs[action]
        # Get feedback based on the rules
        feedback = mastermind.guess(guessedCode)
        # print("AI guess:", guessedCode, "Feedback:", feedback)

        reward = np.sum(feedback)
        # Keep the current state of the game for the network
        nextState = mastermind.code2state(guessedCode, feedback)

        curState = nextState

        board.append(guessedCode)
        state.append(feebackToColors(feedback))

    # print("Game over,AI attempted %d times"%mastermind.attempts)

    if (not mastermind.win):
        board, state = dqn_start(answer)

    return board, state

if __name__ == "__main__":
    answer = random.sample(mastermind.colors,4)
    print(f'Target: {answer}')
    board, state = dqn_start(answer)
    for index, board_value in enumerate(board):
        print(f'iteration: {index} guess: {board_value} feedback: {state[index]}')

