from utils import DataClassCard


def main():
    queen_of_hearts = DataClassCard('Q', 'Hearts')
    print(queen_of_hearts.rank)
    print(queen_of_hearts)


if __name__ == "__main__":
    main()
