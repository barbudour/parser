# INumberBuilder - интерфейс
Объект, осуществляющий низкоуровневые действия с номерами, которые зависят от
бизнес-логики.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface INumberBuilder : INumberObjectManager, 
    	INumberLocationManager, INumberQueueContainer
VB __Копировать
     Public Interface INumberBuilder
    	Inherits INumberObjectManager, INumberLocationManager, INumberQueueContainer
C++ __Копировать
     public interface class INumberBuilder : INumberObjectManager, 
    	INumberLocationManager, INumberQueueContainer
F# __Копировать
     type INumberBuilder = 
        interface
            interface INumberObjectManager
            interface INumberLocationManager
            interface INumberQueueContainer
        end
Implements
    [INumberLocationManager](T_Tessa_Cards_Numbers_INumberLocationManager.htm), [INumberObjectManager](T_Tessa_Cards_Numbers_INumberObjectManager.htm), [INumberQueueContainer](T_Tessa_Cards_Numbers_INumberQueueContainer.htm)
##  __Свойства
[Dependencies](P_Tessa_Cards_Numbers_INumberBuilder_Dependencies.htm)| Объект,
содержащий внешние зависимости API номеров.  
---|---  
##  __Методы
[CreateEmptyNumberAsync](M_Tessa_Cards_Numbers_INumberBuilder_CreateEmptyNumberAsync.htm)|
Создаёт объект, описывающий пустой номер заданного типа. Возвращённое значение
не может быть равно null.  
---|---  
[CreateNumberAsync](M_Tessa_Cards_Numbers_INumberBuilder_CreateNumberAsync.htm)|
Создаёт объект, описывающий номер с заданными параметрами. Номер может быть
пустым или не пустым в зависимости от параметров. Возвращённое значение не
может быть равно null.  
[GetAsync<T>](M_Tessa_Cards_Numbers_INumberBuilder_GetAsync__1.htm)|
Возвращает типизированные данные для контекста события, происходящего с
номером.  
[GetFullNumberAsync](M_Tessa_Cards_Numbers_INumberBuilder_GetFullNumberAsync.htm)|
Возвращает текстовое представление номера по числовому представлению для
заданного действия с номером.  
[GetNumberAsync](M_Tessa_Cards_Numbers_INumberLocationManager_GetNumberAsync.htm)|
Возвращает номер, расположенный в заданных местоположении и контексте или
пустой номер, если он не был найден. Метод не возвращает null.  
(Унаследован от
[INumberLocationManager](T_Tessa_Cards_Numbers_INumberLocationManager.htm))  
[RemoveNumberQueueAsync](M_Tessa_Cards_Numbers_INumberQueueContainer_RemoveNumberQueueAsync.htm)|
Удаляет очередь действий с номерами для заданного контекста. Возвращает
признак того, что очередь была найдена и удалена. Возвращает false, если
очередь не была найдена.  
(Унаследован от
[INumberQueueContainer](T_Tessa_Cards_Numbers_INumberQueueContainer.htm))  
[StoreNumberAsync(INumberContext, INumberObject, NumberStoreMode,
CancellationToken)](M_Tessa_Cards_Numbers_INumberObjectManager_StoreNumberAsync.htm)|
Сохраняет объект с номером в контексте и по местоположению, определяемому его
типом.  
(Унаследован от
[INumberObjectManager](T_Tessa_Cards_Numbers_INumberObjectManager.htm))  
[StoreNumberAsync(INumberContext, INumberObject, INumberLocation,
NumberStoreMode,
CancellationToken)](M_Tessa_Cards_Numbers_INumberLocationManager_StoreNumberAsync.htm)|
Сохраняет объект с номером в заданном местоположении и контексте.  
(Унаследован от
[INumberLocationManager](T_Tessa_Cards_Numbers_INumberLocationManager.htm))  
[TryGetNumberEffectiveLocationAsync](M_Tessa_Cards_Numbers_INumberBuilder_TryGetNumberEffectiveLocationAsync.htm)|
Возвращает эффективное местоположение номера по его заданному местоположению
или null, если эффективное местоположение недоступно и следует использовать
заданное местоположение location. Например, местоположение
[Tessa.Cards.Numbers.NumberLocationTypes.Primary] может соответствовать
определённым полям в карточке, задаваемым эффективным местоположением типа
[Tessa.Cards.Numbers.CardNumberLocation].  
[TryGetNumberLocationAsync](M_Tessa_Cards_Numbers_INumberBuilder_TryGetNumberLocationAsync.htm)|
Возвращает местоположение номера для заданного типа или null, если
местоположение не определено и действие с номером следует отменить.  
[TryGetNumberQueueAsync](M_Tessa_Cards_Numbers_INumberQueueContainer_TryGetNumberQueueAsync.htm)|
Возвращает очередь действий с номерами для заданного контекста или null, если
очередь недоступна.  
(Унаследован от
[INumberQueueContainer](T_Tessa_Cards_Numbers_INumberQueueContainer.htm))  
[TryGetSequenceNameAsync](M_Tessa_Cards_Numbers_INumberBuilder_TryGetSequenceNameAsync.htm)|
Возвращает имя последовательности, подходящее для заданного события,
происходящего с номером, или null, если последовательность недоступна и
операция будет считаться невыполненной.  
## __Методы расширения
[DereserveWhenTabIsClosedOrRefreshedAsync](M_Tessa_Cards_Numbers_NumberExtensions_DereserveWhenTabIsClosedOrRefreshedAsync.htm)|
Добавляет запись в очередь действий с номерами, которая вызовет
дерезервирование заданного номера number при закрытии вкладки карточки или при
её переоткрытии (например, в процессе сохранения).  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
---|---  
[GetNumberAsync](M_Tessa_Cards_Numbers_NumberExtensions_GetNumberAsync_1.htm)|
Возвращает номер, расположенный в заданных местоположении и контексте или
пустой номер, если он не был найден. Метод не возвращает null.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
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
