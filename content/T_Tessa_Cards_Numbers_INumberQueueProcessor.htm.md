# INumberQueueProcessor - интерфейс
Объект, выполняющий обработку действий в очереди с номерами.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface INumberQueueProcessor
VB __Копировать
     Public Interface INumberQueueProcessor
C++ __Копировать
     public interface class INumberQueueProcessor
F# __Копировать
     type INumberQueueProcessor = interface end
##  __Методы
[ProcessAsync](M_Tessa_Cards_Numbers_INumberQueueProcessor_ProcessAsync.htm)|
Выполняет действия из заданной очереди [Tessa.Cards.Numbers.NumberQueue].
Возвращает признак того, что во всех выполненных действиях отсутствуют ошибки.
Действия, которые были успешно выполнены, удаляются из очереди.  
---|---  
## __См. также
#### Ссылки
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
