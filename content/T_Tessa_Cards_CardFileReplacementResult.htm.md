# CardFileReplacementResult - перечисление
Результат изменения состояния файла методом
[SetReplacedState()](M_Tessa_Cards_CardFile_SetReplacedState.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public enum CardFileReplacementResult
VB __Копировать
     Public Enumeration CardFileReplacementResult
C++ __Копировать
     public enum class CardFileReplacementResult
F# __Копировать
     type CardFileReplacementResult
##  __Члены
SetReplaced| 0|  Состояние было равно [None](T_Tessa_Cards_CardFileState.htm)
или [Replaced](T_Tessa_Cards_CardFileState.htm), после чего было изменено на
[Modified](T_Tessa_Cards_CardFileState.htm) или
[ModifiedAndReplaced](T_Tessa_Cards_CardFileState.htm) соответственно.  
---|---|---  
WasReplaced| 1|  Состояние не было изменено, т.к. оно уже было равно
[Modified](T_Tessa_Cards_CardFileState.htm) или
[ModifiedAndReplaced](T_Tessa_Cards_CardFileState.htm).  
WasIncompatible| 2|  Состояние было несовместимо с изменением, т.е. равно
[Inserted](T_Tessa_Cards_CardFileState.htm) или
[Deleted](T_Tessa_Cards_CardFileState.htm).  
## __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
