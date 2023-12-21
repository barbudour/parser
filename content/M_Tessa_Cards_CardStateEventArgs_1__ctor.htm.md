# CardStateEventArgs<TState> \- конструктор
Создаёт экземпляр класса с указанием предыдущего и текущего состояния.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected CardStateEventArgs(
    	TState oldState,
    	TState newState
    )
VB __Копировать
     Protected Sub New ( 
    	oldState As TState,
    	newState As TState
    )
C++ __Копировать
     protected:
    CardStateEventArgs(
    	TState oldState, 
    	TState newState
    )
F# __Копировать
     new : 
            oldState : 'TState * 
            newState : 'TState -> CardStateEventArgs
#### Параметры
oldState [TState](T_Tessa_Cards_CardStateEventArgs_1.htm)
    Предыдущее состояние.
newState [TState](T_Tessa_Cards_CardStateEventArgs_1.htm)
    Текущее состояние.
##  __См. также
#### Ссылки
[CardStateEventArgs<TState> \- ](T_Tessa_Cards_CardStateEventArgs_1.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
