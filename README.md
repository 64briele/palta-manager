# PaltaManager
PaltaManager is a rudimentary tool for managing a Magic: the Gathering collection sorted by set. It manages to do so by loading the cards in a set using the set's code and giving the option to quickly mark which and how many cards of said set are in one's collection. The word "palta" indicates a term used to define sludge, something with low value and present in big quantities, hence the name of this little script with its gui.
## Future implementations
Being something that was quickly thrown together that's more similar to a prototype than anything else, the program currently loads each set very slowly, which could be greatly optimized. It currently uses CustomTkinter for the graphical interface and pandas to manage data inside a single csv file, downloaded from mtgjson.com. Future versions may use totally different tools to achieve the idea behind this small test.
