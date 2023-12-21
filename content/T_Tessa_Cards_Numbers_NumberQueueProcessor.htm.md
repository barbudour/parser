# NumberQueueProcessor - класс
Базовый класс для объекта, выполняющего обработку действий в очереди с
номерами.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class NumberQueueProcessor : INumberQueueProcessor
VB __Копировать
     Public MustInherit Class NumberQueueProcessor
    	Implements INumberQueueProcessor
C++ __Копировать
     public ref class NumberQueueProcessor abstract : INumberQueueProcessor
F# __Копировать
     [<AbstractClassAttribute>]
    type NumberQueueProcessor = 
        class
            interface INumberQueueProcessor
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ NumberQueueProcessor
Derived
[Tessa.Cards.Numbers.DefaultNumberQueueProcessor](T_Tessa_Cards_Numbers_DefaultNumberQueueProcessor.htm)
Implements
    [INumberQueueProcessor](T_Tessa_Cards_Numbers_INumberQueueProcessor.htm)
##  __Конструкторы
[NumberQueueProcessor](M_Tessa_Cards_Numbers_NumberQueueProcessor__ctor.htm)|
Инициализирует новый экземпляр класса NumberQueueProcessor  
---|---  
##  __Свойства
[PredicateByType](P_Tessa_Cards_Numbers_NumberQueueProcessor_PredicateByType.htm)|
Хеш-таблица, задающая отношение между типом предиката
[NumberQueuePredicateType](T_Tessa_Cards_Numbers_NumberQueuePredicateType.htm)
и функцией, обрабатывающей предикат
[NumberQueuePredicateFuncAsync](T_Tessa_Cards_Numbers_NumberQueuePredicateFuncAsync.htm).
Используется в реализации [CanProcessAsync(INumberObject, INumberContext,
NumberQueue, NumberQueueItem, NumberQueueActionType, NumberQueuePredicateType,
CancellationToken)](M_Tessa_Cards_Numbers_NumberQueueProcessor_CanProcessAsync.htm)
по умолчанию.  
---|---  
[ProcessFuncByActionType](P_Tessa_Cards_Numbers_NumberQueueProcessor_ProcessFuncByActionType.htm)|
Хеш-таблица, задающая отношение между типом действия в очереди
[NumberQueueActionType](T_Tessa_Cards_Numbers_NumberQueueActionType.htm) и
функцией, обрабатывающей действие
[NumberQueueProcessFuncAsync](T_Tessa_Cards_Numbers_NumberQueueProcessFuncAsync.htm).
Используется в реализации [TryGetProcessFuncAsync(NumberQueueActionType,
INumberContext, NumberQueue, NumberQueueItem,
NumberQueueEventType)](M_Tessa_Cards_Numbers_NumberQueueProcessor_TryGetProcessFuncAsync.htm)
по умолчанию.  
## __Методы
[CanProcessAsync](M_Tessa_Cards_Numbers_NumberQueueProcessor_CanProcessAsync.htm)|
Возвращает признак того, что предикат queuePredicateType по действию с номером
number разрешает выполнить это действие. Возвращает null, если для заданного
типа предиката получить действие не удалось.  
---|---  
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
[ProcessAsync](M_Tessa_Cards_Numbers_NumberQueueProcessor_ProcessAsync.htm)|
Выполняет действия из заданной очереди [Tessa.Cards.Numbers.NumberQueue].
Возвращает признак того, что во всех выполненных действиях отсутствуют ошибки.
Действия, которые были успешно выполнены, удаляются из очереди.  
[ProcessCoreAsync](M_Tessa_Cards_Numbers_NumberQueueProcessor_ProcessCoreAsync.htm)|
Выполняет действия из заданной очереди [Tessa.Cards.Numbers.NumberQueue].
Возвращает признак того, что во всех выполненных действиях отсутствуют ошибки.
Действия, которые были успешно выполнены, удаляются из очереди.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetProcessFuncAsync](M_Tessa_Cards_Numbers_NumberQueueProcessor_TryGetProcessFuncAsync.htm)|
Возвращает функцию, выполняющую обработку действия с номером в очереди, или
null, если такая функция неизвестна.  
## __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
