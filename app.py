from src.scoreCard import scoreCard

def main():
    input_scoreCard = input('Write the score of your bowling game: \n')
    inputed_scoreCard = scoreCard(input_scoreCard)
    final_score = scoreCard(input_scoreCard).finalScore()
    
    if inputed_scoreCard:
        print(f'Final score is: {final_score}')
    else:
        print('Error: empty score of your bowling game.')


if __name__ == "__main__":
    main()