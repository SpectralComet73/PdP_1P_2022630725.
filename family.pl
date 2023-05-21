%Padilla Rodríguez Ethel
%Rendón Sierra Carlos Alexis

% Facts: parent(Child, Parent)
parent(john, mary).
parent(john, mike).

parent(mary, alice).
parent(mary, george).

parent(mike, lisa).
parent(mike, james).

parent(lisa, carol).
parent(lisa, paul).

%datos agregados
parent(paul, miranda).
parent(paul, jose).

parent(susan, alice).
parent(susan, george).

parent(james, karen).
parent(james, daniel).

%datos agregados
parent(nick, mary).
parent(nick, mike).

%datos agregados
parent(leah, susan).
parent(leah, juan).

% Rule: sibling(Person1, Person2)
sibling(Person1, Person2) :-
    parent(Person1, Parent),
    parent(Person2, Parent),
    Person1 \= Person2.

% Rule: cousin(Person1, Person2)
cousin(Person1, Person2) :-
    parent(Person1, Parent1),
    parent(Person2, Parent2),
    sibling(Parent1, Parent2).

% Rule: nephew(Nephew, UncleAunt)
nephew(Nephew, UncleAunt) :-
    cousin(Nephew, Parent),
    parent(Parent, UncleAunt).

% Rule: grandparent(Grandchild, Grandparent)
grandparent(Grandchild, Grandparent) :-
    parent(Grandchild, Parent),
    parent(Parent, Grandparent).

%Rule: greatgrandparent(X(child), Y(greatgrandparent))
greatGrandparent(X,Y):-
    parent(X,Z),
	parent(Z,W),
	parent(W,Y).

%Rule: greatgrandparent(X(child), Y(greatGreatgrandparent))
greatGreatgrandparent(X,Y):-
    parent(X,Z),
    parent(Z,W),
    parent(W,V),
    parent(V,Y).
