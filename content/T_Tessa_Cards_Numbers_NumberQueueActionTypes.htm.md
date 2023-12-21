# NumberQueueActionTypes - класс
Стандартные типы действий с номерами в очереди
[NumberQueue](T_Tessa_Cards_Numbers_NumberQueue.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class NumberQueueActionTypes
VB __Копировать
     Public NotInheritable Class NumberQueueActionTypes
C++ __Копировать
     public ref class NumberQueueActionTypes abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type NumberQueueActionTypes = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ NumberQueueActionTypes
##  __Методы
[IsKnown](M_Tessa_Cards_Numbers_NumberQueueActionTypes_IsKnown.htm)|
Возвращает признак того, что тип действия с номером в очереди
[NumberQueue](T_Tessa_Cards_Numbers_NumberQueue.htm) является известным для
стандартного API.  
---|---  
## __Поля
[Acquire](F_Tessa_Cards_Numbers_NumberQueueActionTypes_Acquire.htm)|
Выделение очередного номера из последовательности или заданного номера,
который был зарезервирован, если номер был указан.  
---|---  
[AcquireUnreserved](F_Tessa_Cards_Numbers_NumberQueueActionTypes_AcquireUnreserved.htm)|
Выделение заданного номера из последовательности, причём номер не был
зарезервирован.  
[All](F_Tessa_Cards_Numbers_NumberQueueActionTypes_All.htm)|  Список всех
типов действий с номерами в очереди
[NumberQueue](T_Tessa_Cards_Numbers_NumberQueue.htm), которые являются частью
стандартного API.  
[Dereserve](F_Tessa_Cards_Numbers_NumberQueueActionTypes_Dereserve.htm)|
Дерезервирование заданного номера. Если номер не был зарезервирован, то
действий с ним не выполняется.  
[Release](F_Tessa_Cards_Numbers_NumberQueueActionTypes_Release.htm)|
Освобождение заданного номера из последовательности. Указанный номер может
быть выделен или зарезервирован.  
[Reserve](F_Tessa_Cards_Numbers_NumberQueueActionTypes_Reserve.htm)|
Резервирование очередного номера из последовательности.  
[ReserveAcquired](F_Tessa_Cards_Numbers_NumberQueueActionTypes_ReserveAcquired.htm)|
Резервирует указанный номер, который ранее мог быть выделен. Не выполняет
действий, если номер уже был зарезервирован.  
## __См. также
#### Ссылки
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
