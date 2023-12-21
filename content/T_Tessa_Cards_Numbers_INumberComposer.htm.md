# INumberComposer - интерфейс
Объект, обрабатывающий логику выделения и изменения номеров карточек.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface INumberComposer : INumberExtendable
VB __Копировать
     Public Interface INumberComposer
    	Inherits INumberExtendable
C++ __Копировать
     public interface class INumberComposer : INumberExtendable
F# __Копировать
     type INumberComposer = 
        interface
            interface INumberExtendable
        end
Implements
    [INumberExtendable](T_Tessa_Cards_Numbers_INumberExtendable.htm)
##  __Методы
[AcquireNumberAsync](M_Tessa_Cards_Numbers_INumberComposer_AcquireNumberAsync.htm)|
Выделяет и возвращает очередной номер заданного типа без предварительного
резервирования для контекста события, происходящего с номером. Возвращает
пустой номер, если действие не удалось выполнить. Возвращённое значение не
может быть равно null.  
---|---  
[AcquireReservedNumberAsync](M_Tessa_Cards_Numbers_INumberComposer_AcquireReservedNumberAsync.htm)|
Выделяет заданный зарезервированный номер для контекста события, происходящего
с номером. Возвращает признак того, что выделение номера успешно выполнено.  
[AcquireUnreservedNumberAsync](M_Tessa_Cards_Numbers_INumberComposer_AcquireUnreservedNumberAsync.htm)|
Выделяет заданный номер без предварительного резервирования для контекста
события, происходящего с номером. Возвращает признак того, что выделение
номера успешно выполнено.  
[DereserveNumberAsync](M_Tessa_Cards_Numbers_INumberComposer_DereserveNumberAsync.htm)|
Дерезервирует заданный номер для контекста события, происходящего с номером.
Возвращает признак того, что дерезервирование номера успешно выполнено.  
[GetNumberAsync](M_Tessa_Cards_Numbers_INumberComposer_GetNumberAsync.htm)|
Возвращает номер заданного типа для контекста события, происходящего с
номером. Например, загружает номер из определённой позиции в карточке.
Возвращает пустой номер, если выполнить действие не удалось. Возвращённое
значение не может быть равно null.  
[NotifyAfterEventAsync](M_Tessa_Cards_Numbers_INumberExtendable_NotifyAfterEventAsync.htm)|
Выполняет постобработку события, происходящего с номером. Это предоставляет
возможность изменить результат обработанного события или сохранить результат
во внешнем хранилище.  
(Унаследован от
[INumberExtendable](T_Tessa_Cards_Numbers_INumberExtendable.htm))  
[NotifyBeforeEventAsync](M_Tessa_Cards_Numbers_INumberExtendable_NotifyBeforeEventAsync.htm)|
Выполняет предварительную обработку события, происходящего с номером. Это
предоставляет возможность полностью заместить или отменить стандартную
обработку.  
(Унаследован от
[INumberExtendable](T_Tessa_Cards_Numbers_INumberExtendable.htm))  
[ReleaseNumberAsync](M_Tessa_Cards_Numbers_INumberComposer_ReleaseNumberAsync.htm)|
Освобождает заданный выделенный или зарезервированный номер для контекста
события, происходящего с номером. Возвращает признак того, что освобождение
номера успешно выполнено.  
[ReserveAcquiredNumberAsync](M_Tessa_Cards_Numbers_INumberComposer_ReserveAcquiredNumberAsync.htm)|
Резервирует номер, который ранее мог быть выделен, для контекста события,
происходящего с номером. Возвращает признак того, что выделение номера успешно
выполнено.  
[ReserveNumberAsync](M_Tessa_Cards_Numbers_INumberComposer_ReserveNumberAsync.htm)|
Резервирует и возвращает номер заданного типа для контекста события,
происходящего с номером. Возвращает пустой номер, если действие не удалось
выполнить. Возвращённое значение не может быть равно null.  
## __События
[AfterEvent](E_Tessa_Cards_Numbers_INumberExtendable_AfterEvent.htm)|
Событие, выполняемое в процессе постобработки события, происходящего с
номером. Это предоставляет возможность изменить результат обработанного
события или сохранить результат во внешнем хранилище.  
(Унаследован от
[INumberExtendable](T_Tessa_Cards_Numbers_INumberExtendable.htm))  
---|---  
[BeforeEvent](E_Tessa_Cards_Numbers_INumberExtendable_BeforeEvent.htm)|
Событие, выполняемое в процессе предварительной обработки события,
происходящего с номером. Это предоставляет возможность полностью заместить или
отменить стандартную обработку.  
(Унаследован от
[INumberExtendable](T_Tessa_Cards_Numbers_INumberExtendable.htm))  
##  __Методы расширения
[AcquireNumberByTypeAsync](M_Tessa_Cards_Numbers_NumberExtensions_AcquireNumberByTypeAsync.htm)|
Выделяет и возвращает номер, тип которого указан в объекте
context.[NumberObject](P_Tessa_Cards_Numbers_INumberContext_NumberObject.htm).
Возвращённое значение не равно null, но может быть пустым в случае ошибки.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
---|---  
[AcquireReservedNumberAsync](M_Tessa_Cards_Numbers_NumberExtensions_AcquireReservedNumberAsync.htm)|
Выделяет зарезервированный ранее номер, который указан в объекте
context.[NumberObject](P_Tessa_Cards_Numbers_INumberContext_NumberObject.htm).
Возвращает признак того, что номер успешно выделен.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
[CreateContext](M_Tessa_Cards_Numbers_NumberExtensions_CreateContext.htm)|
Создаёт контекст операции с номером для объекта
[INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm) с заданным номером
и другими параметрами. После создания контекста номер нельзя изменить.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
[ReserveAcquiredNumberAsync](M_Tessa_Cards_Numbers_NumberExtensions_ReserveAcquiredNumberAsync.htm)|
Резервирует номер, который ранее мог быть выделен и который указан в объекте
context.[NumberObject](P_Tessa_Cards_Numbers_INumberContext_NumberObject.htm).
Возвращает признак того, что номер успешно зарезервирован.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
