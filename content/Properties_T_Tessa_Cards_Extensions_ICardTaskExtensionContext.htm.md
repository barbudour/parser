# ICardTaskExtensionContext - свойства
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
[Task](P_Tessa_Cards_Extensions_ICardTaskExtensionContext_Task.htm)| Задание,
для которого выполняется расширение.  
[TaskType](P_Tessa_Cards_Extensions_ICardTaskExtensionContext_TaskType.htm)|
Тип завершаемого задания.  
[ValidationResult](P_Tessa_Extensions_ITraceableExtensionContext_ValidationResult.htm)|
Объект, выполняющий построение результата валидации. Может использоваться для
того, чтобы запретить выполнение процесса стандартными средствами.  
(Унаследован от
[ITraceableExtensionContext](T_Tessa_Extensions_ITraceableExtensionContext.htm))  
##  __См. также
#### Ссылки
[ICardTaskExtensionContext -
](T_Tessa_Cards_Extensions_ICardTaskExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
