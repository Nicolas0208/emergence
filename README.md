# emergence
Clone of the game "[Discovery](https://www.discovery-game.com/)" focused on the evolution of peer production.

## 🚀 Quick Start

**Play online now:**
1. Go to [PlayingCards.io](https://playingcards.io/)
2. Create a new room and select “Custom Deck”
3. Import `cards.csv` from this repository
4. Invite 2-4 players and start playing!

**Print the deck:**
1. Open `cards.tex` in [Overleaf](https://www.overleaf.com)
2. Compile the PDF
3. Print double-sided on card stock

## 📚 Table of Contents
- [Quick Start](#-quick-start)
- [Game Rules](#-game-rules--discovery)
- [How to Play](#-how-to-play-discovery-explore--basic-rules)
- [Card Dependency Tree](#-card-dependency-tree)
- [Contributing](#contributing)


The card deck for the game is specified in the file [cards.csv](https://github.com/mdbesten/emergence/blob/main/cards.csv). To play the game online you can load this deck on a site like [PlayingCards.io](https://playingcards.io/). 
For offline use, create a pdf of the deck with LaTeX with help of the CTAN packages [flashcards](https://ctan.org/pkg/flashcards) and [datatool](https://ctan.org/pkg/datatool) on a site such as [Overleaf](https://www.overleaf.com). See [cards.tex](https://github.com/mdbesten/emergence/blob/main/cards.tex).

🧠 Game Rules – Discovery
The Emergence project is inspired by the card game Discovery, which explores the evolution of humanity through key innovations. Each card represents a "discovery" (e.g., Fire, Toolmaking, Agriculture), and the goal is to build a tree of discoveries by playing cards that logically depend on one another.

🔗 Basic Principles
Each discovery card may have one or more prerequisites, which must already be played before the card can be placed.

Cards are grouped by era (1 to 6) and by family (e.g., Tools, Movement, Society).

A card like Fire may be required to play Cooking or Metal. Without Fire, Cooking cannot be played.

Cards without prerequisites (e.g., Gathering) are "starting cards" and can be played freely.

🃏 How to Play (Discovery Explore – Basic Rules)
Each player starts with 5 cards in hand.

On your turn, you may place a card if all its prerequisites are already on the table.

When you place a card, you gain points:

1 point for the first card in a sequence,

2 for the second,

3 for the third, etc.

Cards can be played from:

Your hand,

The shared reserve (5 visible cards for all),

Another player's discard pile (but not your own).

If you can’t or don’t want to play a card, you discard one and draw a new one.

The game ends when all players have emptied their hands. The player with the most points wins.

🎯 Objective
Score the most points by building long, logical sequences of discoveries.

For more game variants (like Discovery Bluff, Select, Connect, etc.), or advanced rules, please refer to the official rules PDF here or view the tutorial video:

https://www.youtube.com/watch?v=PKB_brKQ4HM
