"""
通过扑克游戏来枚举
"""
from enum import Enum
import random

class Suite(Enum):
    SPADE, HEART, CLUB, DIAMOND = range(4)

# 测试枚举
for suite in Suite:
    print(f"{suite}:{suite.value}")

class Card:
    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def __repr__(self):
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        suites = '♠♥♣♦'
        return f"{suites[self.suite.value]}{faces[self.face]}"

    def __lt__(self, other):
        if self.suite == other.suite:
            return self.face < other.face
        return self.suite.value < other.suite.value

# 测试单张牌
card1 = Card(Suite.SPADE, 5)
card2 = Card(Suite.HEART, 13)
print(card1)
print(card2)

class Poker:
    def __init__(self):
        # 初始化一副牌
        self.cards = [Card(suite, face) for suite in Suite for face in range(1, 14)]
        self.current = 0

    def shuffle(self):
        """洗牌"""
        self.current = 0
        random.shuffle(self.cards)

    def deal(self):
        """发牌"""
        if not self.has_next:
            raise ValueError("没有更多的牌了")
        card = self.cards[self.current]
        self.current += 1
        return card

    @property
    def has_next(self):
        """是否还有牌"""
        return self.current < len(self.cards)

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_one(self, card):
        """获得一张牌"""
        self.cards.append(card)

    def arrange(self):
        """整理手牌"""
        self.cards.sort()

    def show_cards(self):
        """展示手牌"""
        return " ".join(str(card) for card in self.cards)

# 测试游戏流程
def main():
    # 初始化扑克和玩家
    poker = Poker()
    poker.shuffle()

    players = [
        Player("东邪"),
        Player("西毒"),
        Player("南帝"),
        Player("北丐")
    ]

    # 发牌（每人13张）
    for _ in range(13):
        for player in players:
            if poker.has_next:
                player.get_one(poker.deal())

    # 展示手牌
    for player in players:
        player.arrange()
        print(f"{player.name}: {player.show_cards()}")

if __name__ == "__main__":
    main()