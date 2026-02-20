from card_shuffling.card_shuffling import example as card_example
from coin_toss.coin_toss import example as coin_example
from page_rank.page_rank import example as page_example
from random_walk.random_walk import example as walk_example
from text_prediction.text_prediction import example as text_example

def main():
    while True:
        print("\nStem Sims")
        print("1. Card Shuffling")
        print("2. Coin Toss")
        print("3. Page Rank")
        print("4. Random Walk")
        print("5. Text Prediction")
        print("0. Exit")

        choice = input("Choose a simulation: ")

        if choice == "1":
            card_example()
        elif choice == "2":
            coin_example()
        elif choice == "3":
            page_example()
        elif choice == "4":
            walk_example()
        elif choice == "5":
            text_example()
        elif choice == "0":
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()
