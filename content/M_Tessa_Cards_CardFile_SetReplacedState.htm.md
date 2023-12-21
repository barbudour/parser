# CardFile.SetReplacedState - метод
Устанавливает состояние [Replaced](T_Tessa_Cards_CardFileState.htm), если файл
был в состоянии [None](T_Tessa_Cards_CardFileState.htm). Устанавливает
состояние [ModifiedAndReplaced](T_Tessa_Cards_CardFileState.htm), если файл
был в состоянии [Modified](T_Tessa_Cards_CardFileState.htm). В других случаях
не выполняет действий.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardFileReplacementResult SetReplacedState()
VB __Копировать
     Public Function SetReplacedState As CardFileReplacementResult
C++ __Копировать
     public:
    CardFileReplacementResult SetReplacedState()
F# __Копировать
     member SetReplacedState : unit -> CardFileReplacementResult 
#### Возвращаемое значение
[CardFileReplacementResult](T_Tessa_Cards_CardFileReplacementResult.htm)  
Результат изменения состояния.
## __См. также
#### Ссылки
[CardFile - ](T_Tessa_Cards_CardFile.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
