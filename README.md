# Poker-Hand-Checker
For this code, we will use your Raspberry Pi running Python 3.9.* and the Apache web server 2.4.* and create an HTML form (client) and a Python CGI (server) program that allows users to select 5 cards (from a deck of 52 cards) representing a "Poker" hand and determines whether the category of poker that poker hands ranked in order from lowest to highest: High card, 1 pair, 2 pair, 3 of a kind, straight, flush, full house, 4 of a kind, and straight flush.
Please refer to this wikipedia page for a complete description and explanation of poker hands: [http://en.wikipedia.org/wiki/Poker_hands](http://en.wikipedia.org/wiki/Poker_hands)
##
The html form MUST allow the user to select EXACTLY 5 UNIQUE cards from ALL 52 cards in the deck as a checkbox input type with card images displayed in place of the text (see below). The images used in the sample below (as well as all images for all the other cards) can be downloaded here: [cards](https://github.com/DhruvalShah199/Poker-Hand-Checker/tree/main/Poker_hand_checker_codes/cards)

![phpJiVAIL](https://user-images.githubusercontent.com/73520531/195380068-13d51348-710b-4a1d-a595-79922bcc49cb.jpeg)

If the user does not select exactly 5 cards, then your server program will send back an HTML reponse back to the client informing the user that they have made an error and instructs the user to hit the "BACK" button and select again!

Once 5 cards have been selected, your program MUST determine what poker hand the 5 cards
represent and sends back an HTML response consisting of the 5 cards (as images) selected
by the user (sorted in rank order from low to high) and a message indicating the hand category
(i.e. High card, 1 pair, 2 pair, 3 of a kind, etc).
