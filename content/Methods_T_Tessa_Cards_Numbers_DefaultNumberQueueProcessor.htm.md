# DefaultNumberQueueProcessor - методы
##  __Методы
[CanProcessAlwaysAsync](M_Tessa_Cards_Numbers_DefaultNumberQueueProcessor_CanProcessAlwaysAsync.htm)|
Функция, возвращающая признак того, что обработка действия с номером разрешена
для предиката [Tessa.Cards.Numbers.NumberQueuePredicateTypes.Always].  
---|---  
[CanProcessAsync](M_Tessa_Cards_Numbers_NumberQueueProcessor_CanProcessAsync.htm)|
Возвращает признак того, что предикат queuePredicateType по действию с номером
number разрешает выполнить это действие. Возвращает null, если для заданного
типа предиката получить действие не удалось.  
(Унаследован от
[NumberQueueProcessor](T_Tessa_Cards_Numbers_NumberQueueProcessor.htm))  
[CanProcessItemIsHandledAsync](M_Tessa_Cards_Numbers_DefaultNumberQueueProcessor_CanProcessItemIsHandledAsync.htm)|
Функция, возвращающая признак того, что обработка действия с номером разрешена
для предиката [Tessa.Cards.Numbers.NumberQueuePredicateTypes.ItemIsHandled].  
[CanProcessNumberIsEmptyAsync](M_Tessa_Cards_Numbers_DefaultNumberQueueProcessor_CanProcessNumberIsEmptyAsync.htm)|
Функция, возвращающая признак того, что обработка действия с номером разрешена
для предиката [Tessa.Cards.Numbers.NumberQueuePredicateTypes.NumberIsEmpty].  
[CanProcessNumberIsSequentialAsync](M_Tessa_Cards_Numbers_DefaultNumberQueueProcessor_CanProcessNumberIsSequentialAsync.htm)|
Функция, возвращающая признак того, что обработка действия с номером разрешена
для предиката
[Tessa.Cards.Numbers.NumberQueuePredicateTypes.NumberIsSequential].  
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
[ProcessAcquireAsync](M_Tessa_Cards_Numbers_DefaultNumberQueueProcessor_ProcessAcquireAsync.htm)|
Функция, выполняющая обработку действия с номером
[Tessa.Cards.Numbers.NumberQueueActionTypes.Reserve] и возвращающая признак
того, что обработка выполнена удачно.  
[ProcessAcquireUnreservedAsync](M_Tessa_Cards_Numbers_DefaultNumberQueueProcessor_ProcessAcquireUnreservedAsync.htm)|
Функция, выполняющая обработку действия с номером
[Tessa.Cards.Numbers.NumberQueueActionTypes.Reserve] и возвращающая признак
того, что обработка выполнена удачно.  
[ProcessAsync](M_Tessa_Cards_Numbers_NumberQueueProcessor_ProcessAsync.htm)|
Выполняет действия из заданной очереди [Tessa.Cards.Numbers.NumberQueue].
Возвращает признак того, что во всех выполненных действиях отсутствуют ошибки.
Действия, которые были успешно выполнены, удаляются из очереди.  
(Унаследован от
[NumberQueueProcessor](T_Tessa_Cards_Numbers_NumberQueueProcessor.htm))  
[ProcessCoreAsync](M_Tessa_Cards_Numbers_NumberQueueProcessor_ProcessCoreAsync.htm)|
Выполняет действия из заданной очереди [Tessa.Cards.Numbers.NumberQueue].
Возвращает признак того, что во всех выполненных действиях отсутствуют ошибки.
Действия, которые были успешно выполнены, удаляются из очереди.  
(Унаследован от
[NumberQueueProcessor](T_Tessa_Cards_Numbers_NumberQueueProcessor.htm))  
[ProcessDereserveAsync](M_Tessa_Cards_Numbers_DefaultNumberQueueProcessor_ProcessDereserveAsync.htm)|
Функция, выполняющая обработку действия с номером
[Tessa.Cards.Numbers.NumberQueueActionTypes.Dereserve] и возвращающая признак
того, что обработка выполнена удачно.  
[ProcessReleaseAsync](M_Tessa_Cards_Numbers_DefaultNumberQueueProcessor_ProcessReleaseAsync.htm)|
Функция, выполняющая обработку действия с номером
[Tessa.Cards.Numbers.NumberQueueActionTypes.Reserve] и возвращающая признак
того, что обработка выполнена удачно.  
[ProcessReserveAcquiredAsync](M_Tessa_Cards_Numbers_DefaultNumberQueueProcessor_ProcessReserveAcquiredAsync.htm)|
Функция, выполняющая обработку действия с номером
[Tessa.Cards.Numbers.NumberQueueActionTypes.ReserveAcquired] и возвращающая
признак того, что обработка выполнена удачно.  
[ProcessReserveAsync](M_Tessa_Cards_Numbers_DefaultNumberQueueProcessor_ProcessReserveAsync.htm)|
Функция, выполняющая обработку действия с номером
[Tessa.Cards.Numbers.NumberQueueActionTypes.Reserve] и возвращающая признак
того, что обработка выполнена удачно.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetProcessFuncAsync](M_Tessa_Cards_Numbers_NumberQueueProcessor_TryGetProcessFuncAsync.htm)|
Возвращает функцию, выполняющую обработку действия с номером в очереди, или
null, если такая функция неизвестна.  
(Унаследован от
[NumberQueueProcessor](T_Tessa_Cards_Numbers_NumberQueueProcessor.htm))  
##  __Методы расширения
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
[DefaultNumberQueueProcessor -
](T_Tessa_Cards_Numbers_DefaultNumberQueueProcessor.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
