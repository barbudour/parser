# CardTaskExtensionContext - класс
Контекст процесса взаимодействия с заданием.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class CardTaskExtensionContext : CardExtensionContext, 
    	ICardTaskExtensionContext, ICardExtensionContext, ICardTypeExtensionContext, IExtensionContext, ITraceableExtensionContext
VB __Копировать
     Public MustInherit Class CardTaskExtensionContext
    	Inherits CardExtensionContext
    	Implements ICardTaskExtensionContext, ICardExtensionContext, ICardTypeExtensionContext, IExtensionContext, 
    	ITraceableExtensionContext
C++ __Копировать
     public ref class CardTaskExtensionContext abstract : public CardExtensionContext, 
    	ICardTaskExtensionContext, ICardExtensionContext, ICardTypeExtensionContext, IExtensionContext, ITraceableExtensionContext
F# __Копировать
     [<AbstractClassAttribute>]
    type CardTaskExtensionContext = 
        class
            inherit CardExtensionContext
            interface ICardTaskExtensionContext
            interface ICardExtensionContext
            interface ICardTypeExtensionContext
            interface IExtensionContext
            interface ITraceableExtensionContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[CardExtensionContext](T_Tessa_Cards_Extensions_CardExtensionContext.htm) __ CardTaskExtensionContext
Derived
[Tessa.Cards.Extensions.CardStoreTaskExtensionContext](T_Tessa_Cards_Extensions_CardStoreTaskExtensionContext.htm)
Implements
    [ICardExtensionContext](T_Tessa_Cards_Extensions_ICardExtensionContext.htm), [ICardTaskExtensionContext](T_Tessa_Cards_Extensions_ICardTaskExtensionContext.htm), [ICardTypeExtensionContext](T_Tessa_Cards_Extensions_ICardTypeExtensionContext.htm), [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm), [ITraceableExtensionContext](T_Tessa_Extensions_ITraceableExtensionContext.htm)
##  __Конструкторы
[CardTaskExtensionContext](M_Tessa_Cards_Extensions_CardTaskExtensionContext__ctor.htm)|
Создаёт экземпляр класса с указанием типа сохраняемой карточки, сохраняемого
задания и его типа, метаинформации по типам карточек и сессии пользователя,
выполняющего операцию.  
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
[Info](P_Tessa_Cards_Extensions_CardExtensionContext_Info.htm)|  Информация,
передаваемая между расширениями в процессе взаимодействия с карточкой.  
(Унаследован от
[CardExtensionContext](T_Tessa_Cards_Extensions_CardExtensionContext.htm))  
[RequestIsSuccessful](P_Tessa_Cards_Extensions_CardExtensionContext_RequestIsSuccessful.htm)|
Признак того, что процесс взаимодействия с карточкой завершился успешно. Можно
использовать в расширениях, выполняющихся после запроса к сервису.  
(Унаследован от
[CardExtensionContext](T_Tessa_Cards_Extensions_CardExtensionContext.htm))  
[Session](P_Tessa_Cards_Extensions_CardExtensionContext_Session.htm)| Сессия
пользователя, для которого выполняется процесс взаимодействия с карточкой.  
(Унаследован от
[CardExtensionContext](T_Tessa_Cards_Extensions_CardExtensionContext.htm))  
[Task](P_Tessa_Cards_Extensions_CardTaskExtensionContext_Task.htm)| Задание,
для которого выполняется расширение.  
[TaskType](P_Tessa_Cards_Extensions_CardTaskExtensionContext_TaskType.htm)|
Тип завершаемого задания.  
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
[CardTypeIs](M_Tessa_Cards_Extensions_CardExtensionContextExtensions_CardTypeIs_2.htm)|
Возвращает признак того, что идентификатор типа карточки равен заданному
значению.  
(Определяется
[CardExtensionContextExtensions](T_Tessa_Cards_Extensions_CardExtensionContextExtensions.htm))  
---|---  
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
##  __См. также
#### Ссылки
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
