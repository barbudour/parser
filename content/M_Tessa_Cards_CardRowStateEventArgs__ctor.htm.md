# CardRowStateEventArgs - конструктор
Создаёт экземпляр класса с указанием предыдущего и текущего состояния строки
коллекционной или древовидной секции.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardRowStateEventArgs(
    	CardRowState oldState,
    	CardRowState newState
    )
VB __Копировать
     Public Sub New ( 
    	oldState As CardRowState,
    	newState As CardRowState
    )
C++ __Копировать
     public:
    CardRowStateEventArgs(
    	CardRowState oldState, 
    	CardRowState newState
    )
F# __Копировать
     new : 
            oldState : CardRowState * 
            newState : CardRowState -> CardRowStateEventArgs
#### Параметры
oldState [CardRowState](T_Tessa_Cards_CardRowState.htm)
    Предыдущее состояние строки коллекционной или древовидной секции.
newState [CardRowState](T_Tessa_Cards_CardRowState.htm)
    Текущее состояние строки коллекционной или древовидной секции.
##  __См. также
#### Ссылки
[CardRowStateEventArgs - ](T_Tessa_Cards_CardRowStateEventArgs.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
