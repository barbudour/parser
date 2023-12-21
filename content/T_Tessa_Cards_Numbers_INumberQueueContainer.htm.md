# INumberQueueContainer - интерфейс
Объект, предоставляющий доступ к очереди действий с номерами.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface INumberQueueContainer
VB __Копировать
     Public Interface INumberQueueContainer
C++ __Копировать
     public interface class INumberQueueContainer
F# __Копировать
     type INumberQueueContainer = interface end
##  __Методы
[RemoveNumberQueueAsync](M_Tessa_Cards_Numbers_INumberQueueContainer_RemoveNumberQueueAsync.htm)|
Удаляет очередь действий с номерами для заданного контекста. Возвращает
признак того, что очередь была найдена и удалена. Возвращает false, если
очередь не была найдена.  
---|---  
[TryGetNumberQueueAsync](M_Tessa_Cards_Numbers_INumberQueueContainer_TryGetNumberQueueAsync.htm)|
Возвращает очередь действий с номерами для заданного контекста или null, если
очередь недоступна.  
## __Методы расширения
[DereserveWhenTabIsClosedOrRefreshedAsync](M_Tessa_Cards_Numbers_NumberExtensions_DereserveWhenTabIsClosedOrRefreshedAsync.htm)|
Добавляет запись в очередь действий с номерами, которая вызовет
дерезервирование заданного номера number при закрытии вкладки карточки или при
её переоткрытии (например, в процессе сохранения).  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
---|---  
[ReleaseAndCommitAtServerAsync](M_Tessa_Cards_Numbers_NumberExtensions_ReleaseAndCommitAtServerAsync.htm)|
Добавляет запись в очередь действий с номерами, которая вызовет освобождение
заданного номера number при сохранении карточки. Вторым параметром возвращает
действие, выполняемое для отмены операции по освобождению номера, или null,
если отсутствуют действия для отмены.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
[ReserveAndCommitAtServerAsync](M_Tessa_Cards_Numbers_NumberExtensions_ReserveAndCommitAtServerAsync.htm)|
Резервирует номер заданного типа и добавляет запись в очередь действий с
номерами, которая вызовет выделение номера при сохранении карточки. Возвращает
зарезервированный номер или пустой номер, если зарезервировать номер не
удалось или в процессе выполнения произошли ошибки.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
