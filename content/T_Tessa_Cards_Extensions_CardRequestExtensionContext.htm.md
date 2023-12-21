# CardRequestExtensionContext - класс
Контекст универсального взаимодействия с сервисом карточек.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardRequestExtensionContext : CardExtensionContext, 
    	ICardRequestExtensionContext, ICardRequestExtensionContext<CardRequest, CardResponse>, ICardExtensionContext, 
    	ICardTypeExtensionContext, IExtensionContext, ITraceableExtensionContext
VB __Копировать
     Public NotInheritable Class CardRequestExtensionContext
    	Inherits CardExtensionContext
    	Implements ICardRequestExtensionContext, ICardRequestExtensionContext(Of CardRequest, CardResponse), 
    	ICardExtensionContext, ICardTypeExtensionContext, IExtensionContext, ITraceableExtensionContext
C++ __Копировать
     public ref class CardRequestExtensionContext sealed : public CardExtensionContext, 
    	ICardRequestExtensionContext, ICardRequestExtensionContext<CardRequest^, CardResponse^>, ICardExtensionContext, 
    	ICardTypeExtensionContext, IExtensionContext, ITraceableExtensionContext
F# __Копировать
     [<SealedAttribute>]
    type CardRequestExtensionContext = 
        class
            inherit CardExtensionContext
            interface ICardRequestExtensionContext
            interface ICardRequestExtensionContext<CardRequest, CardResponse>
            interface ICardExtensionContext
            interface ICardTypeExtensionContext
            interface IExtensionContext
            interface ITraceableExtensionContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[CardExtensionContext](T_Tessa_Cards_Extensions_CardExtensionContext.htm) __ CardRequestExtensionContext
Implements
    [ICardExtensionContext](T_Tessa_Cards_Extensions_ICardExtensionContext.htm), [ICardRequestExtensionContext](T_Tessa_Cards_Extensions_ICardRequestExtensionContext.htm), [ICardRequestExtensionContext](T_Tessa_Cards_Extensions_ICardRequestExtensionContext_2.htm)<[CardRequest](T_Tessa_Cards_CardRequest.htm), [CardResponse](T_Tessa_Cards_CardResponse.htm)>, [ICardTypeExtensionContext](T_Tessa_Cards_Extensions_ICardTypeExtensionContext.htm), [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm), [ITraceableExtensionContext](T_Tessa_Extensions_ITraceableExtensionContext.htm)
##  __Конструкторы
[CardRequestExtensionContext](M_Tessa_Cards_Extensions_CardRequestExtensionContext__ctor.htm)|
Создаёт экземпляр класса с указанием запроса на универсальное взаимодействие с
сервисом карточек, информации о типе запроса, о карточке, файле и задании,
метаинформации по типам карточек и сессии пользователя, выполняющего операцию.  
---|---  
## __Свойства
[CancellationToken](P_Tessa_Cards_Extensions_CardExtensionContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
(Унаследован от
[CardExtensionContext](T_Tessa_Cards_Extensions_CardExtensionContext.htm))  
---|---  
[CardMetadata](P_Tessa_Cards_Extensions_CardExtensionContext_CardMetadata.htm)|
Метаинформация по типам карточек, известным в системе.  
(Унаследован от
[CardExtensionContext](T_Tessa_Cards_Extensions_CardExtensionContext.htm))  
[CardType](P_Tessa_Cards_Extensions_CardExtensionContext_CardType.htm)|  Тип
карточки или null, если тип карточки неизвестен.  
(Унаследован от
[CardExtensionContext](T_Tessa_Cards_Extensions_CardExtensionContext.htm))  
[CardTypeName](P_Tessa_Cards_Extensions_CardExtensionContext_CardTypeName.htm)|
Уникальное имя типа карточки или null, если тип карточки неизвестен. Имя может
не соответствовать действительному типу в метаинформации.  
(Унаследован от
[CardExtensionContext](T_Tessa_Cards_Extensions_CardExtensionContext.htm))  
[DbScope](P_Tessa_Cards_Extensions_CardExtensionContext_DbScope.htm)|  Объект,
обеспечивающий взаимодействие с базой данных. Значение равно null на клиенте и
не равно null на сервере.  
(Унаследован от
[CardExtensionContext](T_Tessa_Cards_Extensions_CardExtensionContext.htm))  
[EnableTracing](P_Tessa_Cards_Extensions_CardExtensionContext_EnableTracing.htm)|
Признак того, что для текущего метода расширений разрешена запись сообщения
трассировки при включённой в системе трассировке. Установка значения равным
false позволяет запретить запись сообщения, например, для реализации метода,
которая по умолчанию не выполняет полезной работы. При отключённой сортировке
значение равно false.  
(Унаследован от
[CardExtensionContext](T_Tessa_Cards_Extensions_CardExtensionContext.htm))  
[FileType](P_Tessa_Cards_Extensions_CardRequestExtensionContext_FileType.htm)|
Тип файла или null, если тип файла неизвестен.  
[FileTypeName](P_Tessa_Cards_Extensions_CardRequestExtensionContext_FileTypeName.htm)|
Имя типа файла или null, если имя типа неизвестно. Имя может быть задано для
несуществующего типа файла.  
[Info](P_Tessa_Cards_Extensions_CardExtensionContext_Info.htm)|  Информация,
передаваемая между расширениями в процессе взаимодействия с карточкой.  
(Унаследован от
[CardExtensionContext](T_Tessa_Cards_Extensions_CardExtensionContext.htm))  
[Request](P_Tessa_Cards_Extensions_CardRequestExtensionContext_Request.htm)|
Запрос на взаимодействие с карточкой.  
[RequestIsSuccessful](P_Tessa_Cards_Extensions_CardExtensionContext_RequestIsSuccessful.htm)|
Признак того, что процесс взаимодействия с карточкой завершился успешно. Можно
использовать в расширениях, выполняющихся после запроса к сервису.  
(Унаследован от
[CardExtensionContext](T_Tessa_Cards_Extensions_CardExtensionContext.htm))  
[RequestType](P_Tessa_Cards_Extensions_CardRequestExtensionContext_RequestType.htm)|
Идентификатор типа универсального запроса к сервису карточек. Соответствует
конкретной операции, которую требуется выполнить.  
[Response](P_Tessa_Cards_Extensions_CardRequestExtensionContext_Response.htm)|
Ответ на запрос по взаимодействию с карточкой. Если свойство установлено перед
выполнением взаимодействия с карточкой стандартными средствами, то такое
взаимодействие не производится.  
[Session](P_Tessa_Cards_Extensions_CardExtensionContext_Session.htm)| Сессия
пользователя, для которого выполняется процесс взаимодействия с карточкой.  
(Унаследован от
[CardExtensionContext](T_Tessa_Cards_Extensions_CardExtensionContext.htm))  
[TaskType](P_Tessa_Cards_Extensions_CardRequestExtensionContext_TaskType.htm)|
Тип задания или null, если тип задания неизвестен.  
[TaskTypeName](P_Tessa_Cards_Extensions_CardRequestExtensionContext_TaskTypeName.htm)|
Имя типа задания или null, если имя типа неизвестно. Имя может быть задано для
несуществующего типа задания.  
[ValidationResult](P_Tessa_Cards_Extensions_CardExtensionContext_ValidationResult.htm)|
Объект, выполняющий построение результата валидации. Может использоваться для
того, чтобы запретить выполнение процесса стандартными средствами.  
(Унаследован от
[CardExtensionContext](T_Tessa_Cards_Extensions_CardExtensionContext.htm))  
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
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
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[AddInvalidateCompletedCacheNames](M_Tessa_Cards_CardRequestExtensions_AddInvalidateCompletedCacheNames.htm)|
Добавляет имена фактически сброшенных кэшей в контексте запроса
[InvalidateCache](F_Tessa_Cards_CardRequestTypes_InvalidateCache.htm).
Значение null и пустой список идентичны. Пустой список означает, что сброс
кэшей не выполняется.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
---|---  
[CardTypeIs](M_Tessa_Cards_Extensions_CardExtensionContextExtensions_CardTypeIs_2.htm)|
Возвращает признак того, что идентификатор типа карточки равен заданному
значению.  
(Определяется
[CardExtensionContextExtensions](T_Tessa_Cards_Extensions_CardExtensionContextExtensions.htm))  
[CardTypeIs](M_Tessa_Cards_Extensions_CardExtensionContextExtensions_CardTypeIs_6.htm)|
Возвращает признак того, что идентификатор типа карточки равен одному из
заданных значений.  
(Определяется
[CardExtensionContextExtensions](T_Tessa_Cards_Extensions_CardExtensionContextExtensions.htm))  
[CardTypeIs](M_Tessa_Cards_Extensions_CardExtensionContextExtensions_CardTypeIs.htm)|
Возвращает признак того, что идентификатор типа карточки равен одному из
заданных значений.  
(Определяется
[CardExtensionContextExtensions](T_Tessa_Cards_Extensions_CardExtensionContextExtensions.htm))  
[CardTypeIs](M_Tessa_Cards_Extensions_CardExtensionContextExtensions_CardTypeIs_1.htm)|
Возвращает признак того, что имя типа карточки равно одному из заданных
значений.  
(Определяется
[CardExtensionContextExtensions](T_Tessa_Cards_Extensions_CardExtensionContextExtensions.htm))  
[CardTypeIs](M_Tessa_Cards_Extensions_CardExtensionContextExtensions_CardTypeIs_7.htm)|
Возвращает признак того, что имя типа карточки равно заданному значению.  
(Определяется
[CardExtensionContextExtensions](T_Tessa_Cards_Extensions_CardExtensionContextExtensions.htm))  
[CardTypeIs](M_Tessa_Cards_Extensions_CardExtensionContextExtensions_CardTypeIs_11.htm)|
Возвращает признак того, что имя типа карточки равно одному из заданных
значений.  
(Определяется
[CardExtensionContextExtensions](T_Tessa_Cards_Extensions_CardExtensionContextExtensions.htm))  
[CardTypeIs](M_Tessa_Cards_Extensions_CardExtensionContextExtensions_CardTypeIs_3.htm)|
Возвращает признак того, что идентификатор типа карточки равен одному из
заданных значений.  
(Определяется
[CardExtensionContextExtensions](T_Tessa_Cards_Extensions_CardExtensionContextExtensions.htm))  
[CardTypeIs](M_Tessa_Cards_Extensions_CardExtensionContextExtensions_CardTypeIs_8.htm)|
Возвращает признак того, что имя типа карточки равно одному из заданных
значений.  
(Определяется
[CardExtensionContextExtensions](T_Tessa_Cards_Extensions_CardExtensionContextExtensions.htm))  
[CardTypeIs](M_Tessa_Cards_Extensions_CardExtensionContextExtensions_CardTypeIs_4.htm)|
Возвращает признак того, что идентификатор типа карточки равен одному из
заданных значений.  
(Определяется
[CardExtensionContextExtensions](T_Tessa_Cards_Extensions_CardExtensionContextExtensions.htm))  
[CardTypeIs](M_Tessa_Cards_Extensions_CardExtensionContextExtensions_CardTypeIs_9.htm)|
Возвращает признак того, что имя типа карточки равно одному из заданных
значений.  
(Определяется
[CardExtensionContextExtensions](T_Tessa_Cards_Extensions_CardExtensionContextExtensions.htm))  
[CardTypeIs](M_Tessa_Cards_Extensions_CardExtensionContextExtensions_CardTypeIs_5.htm)|
Возвращает признак того, что идентификатор типа карточки равен одному из
заданных значений.  
(Определяется
[CardExtensionContextExtensions](T_Tessa_Cards_Extensions_CardExtensionContextExtensions.htm))  
[CardTypeIs](M_Tessa_Cards_Extensions_CardExtensionContextExtensions_CardTypeIs_10.htm)|
Возвращает признак того, что имя типа карточки равно одному из заданных
значений.  
(Определяется
[CardExtensionContextExtensions](T_Tessa_Cards_Extensions_CardExtensionContextExtensions.htm))  
[ClearInvalidateCompletedCacheNames](M_Tessa_Cards_CardRequestExtensions_ClearInvalidateCompletedCacheNames.htm)|
Очищает имена фактически сброшенных кэшей в контексте запроса
[InvalidateCache](F_Tessa_Cards_CardRequestTypes_InvalidateCache.htm).  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
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
[IsInvalidatingAllCaches](M_Tessa_Cards_CardRequestExtensions_IsInvalidatingAllCaches.htm)|
Возвращает признак того, что запрошен сброс всех кэшей в контексте запроса
[InvalidateCache](F_Tessa_Cards_CardRequestTypes_InvalidateCache.htm).  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[RemoveInvalidateCompletedCacheNames](M_Tessa_Cards_CardRequestExtensions_RemoveInvalidateCompletedCacheNames.htm)|
Удаляет имена фактически сброшенных кэшей в контексте запроса
[InvalidateCache](F_Tessa_Cards_CardRequestTypes_InvalidateCache.htm).
Значение null и пустой список идентичны. Пустой список означает, что сброс
кэшей не выполняется.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[SetActionHistoryRowID](M_Tessa_Cards_CardRequestExtensions_SetActionHistoryRowID.htm)|
Устанавливает идентификатор записи в историю действий, которая была записана в
процессе обработки запроса, или null, если требуется удалить предыдущий
идентификатор.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[SetCardAccessAsync](M_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionExtensions_SetCardAccessAsync.htm)|  
(Определяется
[KrPermissionExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionExtensions.htm))  
[SetCardAccessAsync](M_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionExtensions_SetCardAccessAsync_1.htm)|  
(Определяется
[KrPermissionExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionExtensions.htm))  
[SetContextData](M_Tessa_Cards_CardRequestExtensions_SetContextData.htm)|
Устанавливает данные в контексте цепочки расширений для заданного объекта-
отправителя sender. Данные существует в пределах цепочки расширений.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[SetInvalidateCacheNames](M_Tessa_Cards_CardRequestExtensions_SetInvalidateCacheNames_1.htm)|
Устанавливает имена сбрасываемых кэшей в контексте запроса
[InvalidateCache](F_Tessa_Cards_CardRequestTypes_InvalidateCache.htm).
Значение null определяет, что выполняется сброс всех кэшей. Пустой список
означает, что сброс кэшей не выполняется.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[ShouldInvalidateCache](M_Tessa_Cards_CardRequestExtensions_ShouldInvalidateCache.htm)|
Проверяет необходимость сброса кэша в контексте запроса
[InvalidateCache](F_Tessa_Cards_CardRequestTypes_InvalidateCache.htm).
Возвращает true, если был запрошен сброс указанного кэша или всех кэшей.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[TryGetActionHistoryRowID](M_Tessa_Cards_CardRequestExtensions_TryGetActionHistoryRowID.htm)|
Возвращает идентификатор записи в историю действий, которая была записана в
процессе обработки запроса, или null, если записи в истории действий не было
сделано.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[TryGetContextData<T>](M_Tessa_Cards_CardRequestExtensions_TryGetContextData__1.htm)|
Возвращает данные, записанные методом [SetContextData(ICardExtensionContext,
Object, Object)](M_Tessa_Cards_CardRequestExtensions_SetContextData.htm) в
контекст цепочки расширений для заданного объекта-отправителя sender. Данные
существует в пределах цепочки расширений. Возвращает null, если данные не
найдены или были установлены как null.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[TryGetInvalidateCacheNames](M_Tessa_Cards_CardRequestExtensions_TryGetInvalidateCacheNames_1.htm)|
Возвращает имена сбрасываемых кэшей в контексте запроса
[InvalidateCache](F_Tessa_Cards_CardRequestTypes_InvalidateCache.htm) или
null, если имена не заданы, в этом случае инвалидация выполняется для всех
кэшей.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[TryGetInvalidateCompletedCacheNames](M_Tessa_Cards_CardRequestExtensions_TryGetInvalidateCompletedCacheNames.htm)|
Возвращает имена сбрасываемых кэшей в контексте запроса
[InvalidateCache](F_Tessa_Cards_CardRequestTypes_InvalidateCache.htm) или
null, если имена не заданы, в этом случае инвалидация выполняется для всех
кэшей.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
