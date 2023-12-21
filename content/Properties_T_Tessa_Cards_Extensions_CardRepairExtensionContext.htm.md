# CardRepairExtensionContext - свойства
##  __Свойства
[CancellationToken](P_Tessa_Cards_Extensions_CardRepairExtensionContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
---|---  
[Card](P_Tessa_Cards_Extensions_CardRepairExtensionContext_Card.htm)|
Карточка, для которой выполняется исправление структуры.  
[CardMetadata](P_Tessa_Cards_Extensions_CardRepairExtensionContext_CardMetadata.htm)|
Метаинформация по типам карточек.  
[CardType](P_Tessa_Cards_Extensions_CardRepairExtensionContext_CardType.htm)|
Тип карточки или null, если тип карточки неизвестен.  
[CardTypeName](P_Tessa_Cards_Extensions_CardRepairExtensionContext_CardTypeName.htm)|
Уникальное имя типа карточки или null, если тип карточки неизвестен. Имя может
не соответствовать действительному типу в метаинформации.  
[DefaultManager](P_Tessa_Cards_Extensions_CardRepairExtensionContext_DefaultManager.htm)|
Объект, управляющий исправлением структуры карточки без расширений.  
[EnableTracing](P_Tessa_Cards_Extensions_CardRepairExtensionContext_EnableTracing.htm)|
Признак того, что для текущего метода расширений разрешена запись сообщения
трассировки при включённой в системе трассировке. Установка значения равным
false позволяет запретить запись сообщения, например, для реализации метода,
которая по умолчанию не выполняет полезной работы. При отключённой сортировке
значение равно false.  
[ExtendedManager](P_Tessa_Cards_Extensions_CardRepairExtensionContext_ExtendedManager.htm)|
Объект, управляющий исправлением структуры карточки с расширениями.  
[Info](P_Tessa_Cards_Extensions_CardRepairExtensionContext_Info.htm)|
Дополнительная информация для расширений.  
[NewMode](P_Tessa_Cards_Extensions_CardRepairExtensionContext_NewMode.htm)|
Способ заполнения полей значениями по умолчанию при исправлении структуры.  
[NotifyFieldsUpdated](P_Tessa_Cards_Extensions_CardRepairExtensionContext_NotifyFieldsUpdated.htm)|
Признак того, что при исправлении структуры значения полей требуется изменить
с уведомлениями об изменениях.  
[ParentContext](P_Tessa_Cards_Extensions_CardRepairExtensionContext_ParentContext.htm)|
Контекст по исправлению родительской карточки или null, если текущая
исправляемая карточка не связана с родительской карточкой, т.е. не является
сателлитом.  
[RequestIsSuccessful](P_Tessa_Cards_Extensions_CardRepairExtensionContext_RequestIsSuccessful.htm)|
Признак того, что исправление структуры карточки выполнено успешно. Свойство
принимает актуальное значение только после того, как исправление структуры
было выполнено стандартными средствами.  
[ValidationResult](P_Tessa_Cards_Extensions_CardRepairExtensionContext_ValidationResult.htm)|
Объект, выполняющий построение результата валидации. Может использоваться для
того, чтобы запретить выполнение процесса стандартными средствами.  
## __См. также
#### Ссылки
[CardRepairExtensionContext -
](T_Tessa_Cards_Extensions_CardRepairExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
