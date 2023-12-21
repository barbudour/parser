# CardStoreTaskExtensionContext - свойства
##  __Свойства
[Action](P_Tessa_Cards_Extensions_CardStoreTaskExtensionContext_Action.htm)|
Действие, выполняемое с заданием.  
---|---  
[CancellationToken](P_Tessa_Cards_Extensions_CardExtensionContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
(Унаследован от
[CardExtensionContext](T_Tessa_Cards_Extensions_CardExtensionContext.htm))  
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
[CompletionOption](P_Tessa_Cards_Extensions_CardStoreTaskExtensionContext_CompletionOption.htm)|
Вариант завершения задания или null, если вариант завершения неизвестен или
задание не завершается. Если задание завершается, т.е.
[Tessa.Cards.Extensions.ICardStoreTaskExtensionContext.IsCompletion] равен
true, то вариант завершения гарантированно не равен null.  
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
[IsCompletion](P_Tessa_Cards_Extensions_CardStoreTaskExtensionContext_IsCompletion.htm)|
Признак того, что задание в процессе своего завершения.  
[Method](P_Tessa_Cards_Extensions_CardStoreTaskExtensionContext_Method.htm)|
Способ сохранения карточки.  
[Request](P_Tessa_Cards_Extensions_CardStoreTaskExtensionContext_Request.htm)|
Запрос на сохранение карточки, в которой расположено задание.  
[RequestIsSuccessful](P_Tessa_Cards_Extensions_CardExtensionContext_RequestIsSuccessful.htm)|
Признак того, что процесс взаимодействия с карточкой завершился успешно. Можно
использовать в расширениях, выполняющихся после запроса к сервису.  
(Унаследован от
[CardExtensionContext](T_Tessa_Cards_Extensions_CardExtensionContext.htm))  
[Session](P_Tessa_Cards_Extensions_CardExtensionContext_Session.htm)| Сессия
пользователя, для которого выполняется процесс взаимодействия с карточкой.  
(Унаследован от
[CardExtensionContext](T_Tessa_Cards_Extensions_CardExtensionContext.htm))  
[State](P_Tessa_Cards_Extensions_CardStoreTaskExtensionContext_State.htm)|
Состояние задания.  
[StoreContext](P_Tessa_Cards_Extensions_CardStoreTaskExtensionContext_StoreContext.htm)|
Контекст сохранения основной карточки, в рамках которого
сохраняется/завершается задание.  
[StoreDateTime](P_Tessa_Cards_Extensions_CardStoreTaskExtensionContext_StoreDateTime.htm)|
Текущие дата и время сохранения для использования в транзакции или null, если
код не выполняется в транзакции.  
[Task](P_Tessa_Cards_Extensions_CardTaskExtensionContext_Task.htm)| Задание,
для которого выполняется расширение.  
(Унаследован от
[CardTaskExtensionContext](T_Tessa_Cards_Extensions_CardTaskExtensionContext.htm))  
[TaskType](P_Tessa_Cards_Extensions_CardTaskExtensionContext_TaskType.htm)|
Тип завершаемого задания.  
(Унаследован от
[CardTaskExtensionContext](T_Tessa_Cards_Extensions_CardTaskExtensionContext.htm))  
[ValidationResult](P_Tessa_Cards_Extensions_CardExtensionContext_ValidationResult.htm)|
Объект, выполняющий построение результата валидации. Может использоваться для
того, чтобы запретить выполнение процесса стандартными средствами.  
(Унаследован от
[CardExtensionContext](T_Tessa_Cards_Extensions_CardExtensionContext.htm))  
##  __См. также
#### Ссылки
[CardStoreTaskExtensionContext -
](T_Tessa_Cards_Extensions_CardStoreTaskExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
