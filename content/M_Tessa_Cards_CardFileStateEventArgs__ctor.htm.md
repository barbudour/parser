# CardFileStateEventArgs - конструктор
Создаёт экземпляр класса с указанием предыдущего и текущего состояния файла.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardFileStateEventArgs(
    	CardFileState oldState,
    	CardFileState newState
    )
VB __Копировать
     Public Sub New ( 
    	oldState As CardFileState,
    	newState As CardFileState
    )
C++ __Копировать
     public:
    CardFileStateEventArgs(
    	CardFileState oldState, 
    	CardFileState newState
    )
F# __Копировать
     new : 
            oldState : CardFileState * 
            newState : CardFileState -> CardFileStateEventArgs
#### Параметры
oldState [CardFileState](T_Tessa_Cards_CardFileState.htm)
    Предыдущее состояние файла.
newState [CardFileState](T_Tessa_Cards_CardFileState.htm)
    Текущее состояние файла.
##  __См. также
#### Ссылки
[CardFileStateEventArgs - ](T_Tessa_Cards_CardFileStateEventArgs.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
