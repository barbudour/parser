# CardFileState - перечисление
Состояние файла [CardFile](T_Tessa_Cards_CardFile.htm) в карточке
[Card](T_Tessa_Cards_Card.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public enum CardFileState
VB __Копировать
     Public Enumeration CardFileState
C++ __Копировать
     public enum class CardFileState
F# __Копировать
     type CardFileState
##  __Члены
None| 0|  Файл не был изменён.  
---|---|---  
Modified| 1|  Свойства файла были изменены, но контент не изменился.  
Replaced| 2|  Контент файла был заменён, но свойства не изменились.  
ModifiedAndReplaced| 3|  Свойства файла были изменены, а контент был заменён.  
Inserted| 4|  Файл был добавлен.  
Deleted| 5|  Файл был удалён.  
## __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
