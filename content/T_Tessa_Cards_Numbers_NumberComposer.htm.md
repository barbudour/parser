# NumberComposer - класс
Объект, обрабатывающий логику выделения и изменения номеров карточек, с
реализацией по умолчанию.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class NumberComposer : NumberExtendable, 
    	INumberComposer, INumberExtendable
VB __Копировать
     Public Class NumberComposer
    	Inherits NumberExtendable
    	Implements INumberComposer, INumberExtendable
C++ __Копировать
     public ref class NumberComposer : public NumberExtendable, 
    	INumberComposer, INumberExtendable
F# __Копировать
     type NumberComposer = 
        class
            inherit NumberExtendable
            interface INumberComposer
            interface INumberExtendable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[NumberExtendable](T_Tessa_Cards_Numbers_NumberExtendable.htm) __ NumberComposer
Implements
    [INumberComposer](T_Tessa_Cards_Numbers_INumberComposer.htm), [INumberExtendable](T_Tessa_Cards_Numbers_INumberExtendable.htm)
##  __Конструкторы
[NumberComposer](M_Tessa_Cards_Numbers_NumberComposer__ctor.htm)|  Создаёт
экземпляр класса с указанием его зависимостей.  
---|---  
## __Свойства
[Dependencies](P_Tessa_Cards_Numbers_NumberComposer_Dependencies.htm)|
Объект, содержащий стандартные зависимости текущего объекта.  
---|---  
## __Методы
[AcquireNumberAsync](M_Tessa_Cards_Numbers_NumberComposer_AcquireNumberAsync.htm)|
Выделяет и возвращает очередной номер заданного типа без предварительного
резервирования для контекста события, происходящего с номером. Возвращает
пустой номер, если действие не удалось выполнить. Возвращённое значение не
может быть равно null.  
---|---  
[AcquireNumberCoreAsync](M_Tessa_Cards_Numbers_NumberComposer_AcquireNumberCoreAsync.htm)|
Выделяет и возвращает очередной номер заданного типа без предварительного
резервирования для контекста события, происходящего с номером. Возвращает
пустой номер, если действие не удалось выполнить. Возвращённое значение не
может быть равно null.  
[AcquireReservedNumberAsync](M_Tessa_Cards_Numbers_NumberComposer_AcquireReservedNumberAsync.htm)|
Выделяет заданный зарезервированный номер для контекста события, происходящего
с номером. Возвращает признак того, что выделение номера успешно выполнено.  
[AcquireReservedNumberCoreAsync](M_Tessa_Cards_Numbers_NumberComposer_AcquireReservedNumberCoreAsync.htm)|
Выделяет заданный зарезервированный номер для контекста события, происходящего
с номером. Возвращает признак того, что выделение номера успешно выполнено.  
[AcquireUnreservedNumberAsync](M_Tessa_Cards_Numbers_NumberComposer_AcquireUnreservedNumberAsync.htm)|
Выделяет заданный номер без предварительного резервирования для контекста
события, происходящего с номером. Возвращает признак того, что выделение
номера успешно выполнено.  
[AcquireUnreservedNumberCoreAsync](M_Tessa_Cards_Numbers_NumberComposer_AcquireUnreservedNumberCoreAsync.htm)|
Выделяет заданный номер без предварительного резервирования для контекста
события, происходящего с номером. Возвращает признак того, что выделение
номера успешно выполнено.  
[DereserveNumberAsync](M_Tessa_Cards_Numbers_NumberComposer_DereserveNumberAsync.htm)|
Дерезервирует заданный номер для контекста события, происходящего с номером.
Возвращает признак того, что дерезервирование номера успешно выполнено.  
[DereserveNumberCoreAsync](M_Tessa_Cards_Numbers_NumberComposer_DereserveNumberCoreAsync.htm)|
Дерезервирует заданный номер для контекста события, происходящего с номером.
Возвращает признак того, что дерезервирование номера успешно выполнено.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetNumberAsync](M_Tessa_Cards_Numbers_NumberComposer_GetNumberAsync.htm)|
Возвращает номер заданного типа для контекста события, происходящего с
номером. Например, загружает номер из определённой позиции в карточке.
Возвращает пустой номер, если выполнить действие не удалось. Возвращённое
значение не может быть равно null.  
[GetSequenceProvider](M_Tessa_Cards_Numbers_NumberComposer_GetSequenceProvider.htm)|
Возвращает объект [Tessa.Sequences.ISequenceProvider], подходящий для
заданного события, происходящего с номером.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MethodReturnedNull](M_Tessa_Cards_Numbers_NumberExtendable_MethodReturnedNull.htm)|
Создаёт и возвращает исключение, которое вызывается в случае, когда
перегруженный виртуальный метод вернул null, хотя он не должен был возвращать
null.  
(Унаследован от
[NumberExtendable](T_Tessa_Cards_Numbers_NumberExtendable.htm))  
[NotifyAfterEventAsync](M_Tessa_Cards_Numbers_NumberExtendable_NotifyAfterEventAsync.htm)|
Выполняет постобработку события, происходящего с номером. Это предоставляет
возможность изменить результат обработанного события или сохранить результат
во внешнем хранилище.  
(Унаследован от
[NumberExtendable](T_Tessa_Cards_Numbers_NumberExtendable.htm))  
[NotifyAfterEventCoreAsync](M_Tessa_Cards_Numbers_NumberExtendable_NotifyAfterEventCoreAsync.htm)|
Выполняет постобработку события, происходящего с номером. Это предоставляет
возможность изменить результат обработанного события или сохранить результат
во внешнем хранилище.  
(Унаследован от
[NumberExtendable](T_Tessa_Cards_Numbers_NumberExtendable.htm))  
[NotifyBeforeEventAsync](M_Tessa_Cards_Numbers_NumberExtendable_NotifyBeforeEventAsync.htm)|
Выполняет предварительную обработку события, происходящего с номером. Это
предоставляет возможность полностью заместить или отменить стандартную
обработку.  
(Унаследован от
[NumberExtendable](T_Tessa_Cards_Numbers_NumberExtendable.htm))  
[NotifyBeforeEventCoreAsync](M_Tessa_Cards_Numbers_NumberExtendable_NotifyBeforeEventCoreAsync.htm)|
Выполняет предварительную обработку события, происходящего с номером. Это
предоставляет возможность полностью заместить или отменить стандартную
обработку.  
(Унаследован от
[NumberExtendable](T_Tessa_Cards_Numbers_NumberExtendable.htm))  
[ReleaseNumberAsync](M_Tessa_Cards_Numbers_NumberComposer_ReleaseNumberAsync.htm)|
Освобождает заданный выделенный или зарезервированный номер для контекста
события, происходящего с номером. Возвращает признак того, что освобождение
номера успешно выполнено.  
[ReleaseNumberCoreAsync](M_Tessa_Cards_Numbers_NumberComposer_ReleaseNumberCoreAsync.htm)|
Освобождает заданный выделенный или зарезервированный номер для контекста
события, происходящего с номером. Возвращает признак того, что освобождение
номера успешно выполнено.  
[ReserveAcquiredNumberAsync](M_Tessa_Cards_Numbers_NumberComposer_ReserveAcquiredNumberAsync.htm)|
Резервирует номер, который ранее мог быть выделен, для контекста события,
происходящего с номером. Возвращает признак того, что выделение номера успешно
выполнено.  
[ReserveAcquiredNumberCoreAsync](M_Tessa_Cards_Numbers_NumberComposer_ReserveAcquiredNumberCoreAsync.htm)|
Резервирует номер, который ранее мог быть выделен, для контекста события,
происходящего с номером. Возвращает признак того, что выделение номера успешно
выполнено.  
[ReserveNumberAsync](M_Tessa_Cards_Numbers_NumberComposer_ReserveNumberAsync.htm)|
Резервирует и возвращает номер заданного типа для контекста события,
происходящего с номером. Возвращает пустой номер, если действие не удалось
выполнить. Возвращённое значение не может быть равно null.  
[ReserveNumberCoreAsync](M_Tessa_Cards_Numbers_NumberComposer_ReserveNumberCoreAsync.htm)|
Резервирует и возвращает номер заданного типа для контекста события,
происходящего с номером. Возвращает пустой номер, если действие не удалось
выполнить. Возвращённое значение не может быть равно null.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryCreateNewDbScope](M_Tessa_Cards_Numbers_NumberComposer_TryCreateNewDbScope.htm)|
Открывает новое соединение с базой данных, если этого требует режим выполнения
транзакций и выполнение происходит на сервере. В противном случае возвращает
null.  
## __События
[AfterEvent](E_Tessa_Cards_Numbers_NumberExtendable_AfterEvent.htm)|  Событие,
выполняемое в процессе постобработки события, происходящего с номером. Это
предоставляет возможность изменить результат обработанного события или
сохранить результат во внешнем хранилище.  
(Унаследован от
[NumberExtendable](T_Tessa_Cards_Numbers_NumberExtendable.htm))  
---|---  
[BeforeEvent](E_Tessa_Cards_Numbers_NumberExtendable_BeforeEvent.htm)|
Событие, выполняемое в процессе предварительной обработки события,
происходящего с номером. Это предоставляет возможность полностью заместить или
отменить стандартную обработку.  
(Унаследован от
[NumberExtendable](T_Tessa_Cards_Numbers_NumberExtendable.htm))  
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
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[ReserveAcquiredNumberAsync](M_Tessa_Cards_Numbers_NumberExtensions_ReserveAcquiredNumberAsync.htm)|
Резервирует номер, который ранее мог быть выделен и который указан в объекте
context.[NumberObject](P_Tessa_Cards_Numbers_INumberContext_NumberObject.htm).
Возвращает признак того, что номер успешно зарезервирован.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
