# CardFile.RevertReplacedState - метод
Устанавливает состояние [None](T_Tessa_Cards_CardFileState.htm), если файл был
в состоянии [Replaced](T_Tessa_Cards_CardFileState.htm). Устанавливает
состояние [Modified](T_Tessa_Cards_CardFileState.htm), если файл был в
состоянии [ModifiedAndReplaced](T_Tessa_Cards_CardFileState.htm). В других
случаях не выполняет действий. Возвращает
[WasReplaced](T_Tessa_Cards_CardFileReplacementResult.htm), если состояние
было изменено, и
[WasIncompatible](T_Tessa_Cards_CardFileReplacementResult.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardFileReplacementResult RevertReplacedState()
VB __Копировать
     Public Function RevertReplacedState As CardFileReplacementResult
C++ __Копировать
     public:
    CardFileReplacementResult RevertReplacedState()
F# __Копировать
     member RevertReplacedState : unit -> CardFileReplacementResult 
#### Возвращаемое значение
[CardFileReplacementResult](T_Tessa_Cards_CardFileReplacementResult.htm)  
Результат изменения состояния.
## __См. также
#### Ссылки
[CardFile - ](T_Tessa_Cards_CardFile.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
