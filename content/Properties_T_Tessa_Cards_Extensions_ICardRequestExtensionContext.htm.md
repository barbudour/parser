# ICardRequestExtensionContext - свойства
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
[FileType](P_Tessa_Cards_Extensions_ICardRequestExtensionContext_FileType.htm)|
Тип файла или null, если тип файла неизвестен.  
[FileTypeName](P_Tessa_Cards_Extensions_ICardRequestExtensionContext_FileTypeName.htm)|
Имя типа файла или null, если имя типа неизвестно. Имя может быть задано для
несуществующего типа файла.  
[Info](P_Tessa_Cards_Extensions_ICardExtensionContext_Info.htm)|  Информация,
передаваемая между расширениями в процессе взаимодействия с карточкой.  
(Унаследован от
[ICardExtensionContext](T_Tessa_Cards_Extensions_ICardExtensionContext.htm))  
[Request](P_Tessa_Cards_Extensions_ICardRequestExtensionContext_2_Request.htm)|
Запрос на взаимодействие с карточкой.  
(Унаследован от [ICardRequestExtensionContext<TRequest,
TResponse>](T_Tessa_Cards_Extensions_ICardRequestExtensionContext_2.htm))  
[RequestIsSuccessful](P_Tessa_Cards_Extensions_ICardExtensionContext_RequestIsSuccessful.htm)|
Признак того, что процесс взаимодействия с карточкой завершился успешно. Можно
использовать в расширениях, выполняющихся после запроса к сервису.  
(Унаследован от
[ICardExtensionContext](T_Tessa_Cards_Extensions_ICardExtensionContext.htm))  
[RequestType](P_Tessa_Cards_Extensions_ICardRequestExtensionContext_RequestType.htm)|
Идентификатор типа универсального запроса к сервису карточек. Соответствует
конкретной операции, которую требуется выполнить.  
[Response](P_Tessa_Cards_Extensions_ICardRequestExtensionContext_2_Response.htm)|
Ответ на запрос по взаимодействию с карточкой. Если свойство установлено перед
выполнением взаимодействия с карточкой стандартными средствами, то такое
взаимодействие не производится.  
(Унаследован от [ICardRequestExtensionContext<TRequest,
TResponse>](T_Tessa_Cards_Extensions_ICardRequestExtensionContext_2.htm))  
[Session](P_Tessa_Cards_Extensions_ICardExtensionContext_Session.htm)| Сессия
пользователя, для которого выполняется процесс взаимодействия с карточкой.  
(Унаследован от
[ICardExtensionContext](T_Tessa_Cards_Extensions_ICardExtensionContext.htm))  
[TaskType](P_Tessa_Cards_Extensions_ICardRequestExtensionContext_TaskType.htm)|
Тип задания или null, если тип задания неизвестен.  
[TaskTypeName](P_Tessa_Cards_Extensions_ICardRequestExtensionContext_TaskTypeName.htm)|
Имя типа задания или null, если имя типа неизвестно. Имя может быть задано для
несуществующего типа задания.  
[ValidationResult](P_Tessa_Extensions_ITraceableExtensionContext_ValidationResult.htm)|
Объект, выполняющий построение результата валидации. Может использоваться для
того, чтобы запретить выполнение процесса стандартными средствами.  
(Унаследован от
[ITraceableExtensionContext](T_Tessa_Extensions_ITraceableExtensionContext.htm))  
##  __См. также
#### Ссылки
[ICardRequestExtensionContext -
](T_Tessa_Cards_Extensions_ICardRequestExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
