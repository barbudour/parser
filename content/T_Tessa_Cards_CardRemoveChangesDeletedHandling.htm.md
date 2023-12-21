# CardRemoveChangesDeletedHandling - перечисление
Способ обработки удалённых строк, файлов и заданий при вызове метода карточки
[RemoveChanges(CardRemoveChangesDeletedHandling)](M_Tessa_Cards_Card_RemoveChanges.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public enum CardRemoveChangesDeletedHandling
VB __Копировать
     Public Enumeration CardRemoveChangesDeletedHandling
C++ __Копировать
     public enum class CardRemoveChangesDeletedHandling
F# __Копировать
     type CardRemoveChangesDeletedHandling
##  __Члены
ResetToNone| 0|  Состояния State, связанные с удалением данных (строк, файлов
или заданий) будут принудительно заменены на None.  
---|---|---  
KeepDeleted| 1|  Состояния State, связанные с удалением данных (строк, файлов
или заданий) не будут изменены, т.е. такие строки, файлы или задания останутся
в пакете карточки с тем же состоянием Deleted.  
Remove| 2|  Строки, файлы или задания, находящиеся в состоянии Deleted, будут
удалены из карточки.  
## __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
