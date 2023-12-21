# ICardStoreTaskExtensionContext - свойства
##  __Свойства
[Action](P_Tessa_Cards_Extensions_ICardStoreTaskExtensionContext_Action.htm)|
Действие, выполняемое с заданием.  
---|---  
[CancellationToken](P_Tessa_Extensions_IExtensionContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
(Унаследован от [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm))  
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
[CompletionOption](P_Tessa_Cards_Extensions_ICardStoreTaskExtensionContext_CompletionOption.htm)|
Вариант завершения задания или null, если вариант завершения неизвестен или
задание не завершается. Если задание завершается, т.е.
[Tessa.Cards.Extensions.ICardStoreTaskExtensionContext.IsCompletion] равен
true, то вариант завершения гарантированно не равен null.  
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
[IsCompletion](P_Tessa_Cards_Extensions_ICardStoreTaskExtensionContext_IsCompletion.htm)|
Признак того, что задание в процессе своего завершения.  
[Method](P_Tessa_Cards_Extensions_ICardStoreTaskExtensionContext_Method.htm)|
Способ сохранения карточки.  
[Request](P_Tessa_Cards_Extensions_ICardStoreTaskExtensionContext_Request.htm)|
Запрос на сохранение карточки, в которой расположено задание.  
[RequestIsSuccessful](P_Tessa_Cards_Extensions_ICardExtensionContext_RequestIsSuccessful.htm)|
Признак того, что процесс взаимодействия с карточкой завершился успешно. Можно
использовать в расширениях, выполняющихся после запроса к сервису.  
(Унаследован от
[ICardExtensionContext](T_Tessa_Cards_Extensions_ICardExtensionContext.htm))  
[Session](P_Tessa_Cards_Extensions_ICardExtensionContext_Session.htm)| Сессия
пользователя, для которого выполняется процесс взаимодействия с карточкой.  
(Унаследован от
[ICardExtensionContext](T_Tessa_Cards_Extensions_ICardExtensionContext.htm))  
[State](P_Tessa_Cards_Extensions_ICardStoreTaskExtensionContext_State.htm)|
Состояние задания.  
[StoreContext](P_Tessa_Cards_Extensions_ICardStoreTaskExtensionContext_StoreContext.htm)|
Контекст сохранения основной карточки, в рамках которого
сохраняется/завершается задание.  
[StoreDateTime](P_Tessa_Cards_Extensions_ICardStoreTaskExtensionContext_StoreDateTime.htm)|
Текущие дата и время сохранения для использования в транзакции или null, если
код не выполняется в транзакции.  
[Task](P_Tessa_Cards_Extensions_ICardTaskExtensionContext_Task.htm)| Задание,
для которого выполняется расширение.  
(Унаследован от
[ICardTaskExtensionContext](T_Tessa_Cards_Extensions_ICardTaskExtensionContext.htm))  
[TaskType](P_Tessa_Cards_Extensions_ICardTaskExtensionContext_TaskType.htm)|
Тип завершаемого задания.  
(Унаследован от
[ICardTaskExtensionContext](T_Tessa_Cards_Extensions_ICardTaskExtensionContext.htm))  
[ValidationResult](P_Tessa_Extensions_ITraceableExtensionContext_ValidationResult.htm)|
Объект, выполняющий построение результата валидации. Может использоваться для
того, чтобы запретить выполнение процесса стандартными средствами.  
(Унаследован от
[ITraceableExtensionContext](T_Tessa_Extensions_ITraceableExtensionContext.htm))  
##  __См. также
#### Ссылки
[ICardStoreTaskExtensionContext -
](T_Tessa_Cards_Extensions_ICardStoreTaskExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
