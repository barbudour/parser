# ICardRepairExtensionContext - свойства
##  __Свойства
[CancellationToken](P_Tessa_Extensions_IExtensionContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
(Унаследован от [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm))  
---|---  
[Card](P_Tessa_Cards_Extensions_ICardRepairExtensionContext_Card.htm)|
Карточка, для которой выполняется исправление структуры.  
[CardMetadata](P_Tessa_Cards_Extensions_ICardRepairExtensionContext_CardMetadata.htm)|
Метаинформация по типам карточек.  
[CardType](P_Tessa_Cards_Extensions_ICardTypeExtensionContext_CardType.htm)|
Тип карточки или null, если тип карточки неизвестен.  
(Унаследован от
[ICardTypeExtensionContext](T_Tessa_Cards_Extensions_ICardTypeExtensionContext.htm))  
[CardTypeName](P_Tessa_Cards_Extensions_ICardTypeExtensionContext_CardTypeName.htm)|
Уникальное имя типа карточки или null, если тип карточки неизвестен. Имя может
не соответствовать действительному типу в метаинформации.  
(Унаследован от
[ICardTypeExtensionContext](T_Tessa_Cards_Extensions_ICardTypeExtensionContext.htm))  
[DefaultManager](P_Tessa_Cards_Extensions_ICardRepairExtensionContext_DefaultManager.htm)|
Объект, управляющий исправлением структуры карточки без расширений.  
[EnableTracing](P_Tessa_Extensions_ITraceableExtensionContext_EnableTracing.htm)|
Признак того, что для текущего метода расширений разрешена запись сообщения
трассировки при включённой в системе трассировке. Установка значения равным
false позволяет запретить запись сообщения, например, для реализации метода,
которая по умолчанию не выполняет полезной работы. При отключённой сортировке
значение равно false.  
(Унаследован от
[ITraceableExtensionContext](T_Tessa_Extensions_ITraceableExtensionContext.htm))  
[ExtendedManager](P_Tessa_Cards_Extensions_ICardRepairExtensionContext_ExtendedManager.htm)|
Объект, управляющий исправлением структуры карточки с расширениями.  
[Info](P_Tessa_Cards_Extensions_ICardRepairExtensionContext_Info.htm)|
Дополнительная информация для расширений.  
[NewMode](P_Tessa_Cards_Extensions_ICardRepairExtensionContext_NewMode.htm)|
Способ заполнения полей значениями по умолчанию при исправлении структуры.  
[NotifyFieldsUpdated](P_Tessa_Cards_Extensions_ICardRepairExtensionContext_NotifyFieldsUpdated.htm)|
Признак того, что при исправлении структуры значения полей требуется изменить
с уведомлениями об изменениях.  
[ParentContext](P_Tessa_Cards_Extensions_ICardRepairExtensionContext_ParentContext.htm)|
Контекст по исправлению родительской карточки или null, если текущая
исправляемая карточка не связана с родительской карточкой, т.е. не является
сателлитом.  
[RequestIsSuccessful](P_Tessa_Cards_Extensions_ICardRepairExtensionContext_RequestIsSuccessful.htm)|
Признак того, что исправление структуры карточки выполнено успешно. Свойство
принимает актуальное значение только после того, как исправление структуры
было выполнено стандартными средствами.  
[ValidationResult](P_Tessa_Extensions_ITraceableExtensionContext_ValidationResult.htm)|
Объект, выполняющий построение результата валидации. Может использоваться для
того, чтобы запретить выполнение процесса стандартными средствами.  
(Унаследован от
[ITraceableExtensionContext](T_Tessa_Extensions_ITraceableExtensionContext.htm))  
##  __См. также
#### Ссылки
[ICardRepairExtensionContext -
](T_Tessa_Cards_Extensions_ICardRepairExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
