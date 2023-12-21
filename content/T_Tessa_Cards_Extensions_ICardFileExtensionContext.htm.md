# ICardFileExtensionContext - интерфейс
Контекст процесса взаимодействия с файлом карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardFileExtensionContext : ICardExtensionContext, 
    	ICardTypeExtensionContext, IExtensionContext, ITraceableExtensionContext
VB __Копировать
     Public Interface ICardFileExtensionContext
    	Inherits ICardExtensionContext, ICardTypeExtensionContext, IExtensionContext, ITraceableExtensionContext
C++ __Копировать
     public interface class ICardFileExtensionContext : ICardExtensionContext, 
    	ICardTypeExtensionContext, IExtensionContext, ITraceableExtensionContext
F# __Копировать
     type ICardFileExtensionContext = 
        interface
            interface ICardExtensionContext
            interface ICardTypeExtensionContext
            interface IExtensionContext
            interface ITraceableExtensionContext
        end
Implements
    [ICardExtensionContext](T_Tessa_Cards_Extensions_ICardExtensionContext.htm), [ICardTypeExtensionContext](T_Tessa_Cards_Extensions_ICardTypeExtensionContext.htm), [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm), [ITraceableExtensionContext](T_Tessa_Extensions_ITraceableExtensionContext.htm)
##  __Свойства
[CancellationToken](P_Tessa_Extensions_IExtensionContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
(Унаследован от [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm))  
---|---  
[CardMetadata](P_Tessa_Cards_Extensions_ICardExtensionContext_CardMetadata.htm)|
Метаинформация по типам карточек, известным в системе.  
(Унаследован от
[ICardExtensionContext](T_Tessa_Cards_Extensions_ICardExtensionContext.htm))  
[CardType](P_Tessa_Cards_Extensions_ICardTypeExtensionContext_CardType.htm)|
Тип карточки или null, если тип карточки неизвестен.  
(Унаследован от
[ICardTypeExtensionContext](T_Tessa_Cards_Extensions_ICardTypeExtensionContext.htm))  
[CardTypeName](P_Tessa_Cards_Extensions_ICardTypeExtensionContext_CardTypeName.htm)|
Уникальное имя типа карточки или null, если тип карточки неизвестен. Имя может
не соответствовать действительному типу в метаинформации.  
(Унаследован от
[ICardTypeExtensionContext](T_Tessa_Cards_Extensions_ICardTypeExtensionContext.htm))  
[DbScope](P_Tessa_Cards_Extensions_ICardExtensionContext_DbScope.htm)|
Объект, обеспечивающий взаимодействие с базой данных. Значение равно null на
клиенте и не равно null на сервере.  
(Унаследован от
[ICardExtensionContext](T_Tessa_Cards_Extensions_ICardExtensionContext.htm))  
[EnableTracing](P_Tessa_Extensions_ITraceableExtensionContext_EnableTracing.htm)|
Признак того, что для текущего метода расширений разрешена запись сообщения
трассировки при включённой в системе трассировке. Установка значения равным
false позволяет запретить запись сообщения, например, для реализации метода,
которая по умолчанию не выполняет полезной работы. При отключённой сортировке
значение равно false.  
(Унаследован от
[ITraceableExtensionContext](T_Tessa_Extensions_ITraceableExtensionContext.htm))  
[FileType](P_Tessa_Cards_Extensions_ICardFileExtensionContext_FileType.htm)|
Тип файла или null, если тип файла неизвестен.  
[FileTypeName](P_Tessa_Cards_Extensions_ICardFileExtensionContext_FileTypeName.htm)|
Имя типа файла или null, если имя типа неизвестно. Имя может быть задано для
несуществующего типа файла.  
[Info](P_Tessa_Cards_Extensions_ICardExtensionContext_Info.htm)|  Информация,
передаваемая между расширениями в процессе взаимодействия с карточкой.  
(Унаследован от
[ICardExtensionContext](T_Tessa_Cards_Extensions_ICardExtensionContext.htm))  
[RequestIsSuccessful](P_Tessa_Cards_Extensions_ICardExtensionContext_RequestIsSuccessful.htm)|
Признак того, что процесс взаимодействия с карточкой завершился успешно. Можно
использовать в расширениях, выполняющихся после запроса к сервису.  
(Унаследован от
[ICardExtensionContext](T_Tessa_Cards_Extensions_ICardExtensionContext.htm))  
[Session](P_Tessa_Cards_Extensions_ICardExtensionContext_Session.htm)| Сессия
пользователя, для которого выполняется процесс взаимодействия с карточкой.  
(Унаследован от
[ICardExtensionContext](T_Tessa_Cards_Extensions_ICardExtensionContext.htm))  
[ValidationResult](P_Tessa_Extensions_ITraceableExtensionContext_ValidationResult.htm)|
Объект, выполняющий построение результата валидации. Может использоваться для
того, чтобы запретить выполнение процесса стандартными средствами.  
(Унаследован от
[ITraceableExtensionContext](T_Tessa_Extensions_ITraceableExtensionContext.htm))  
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
