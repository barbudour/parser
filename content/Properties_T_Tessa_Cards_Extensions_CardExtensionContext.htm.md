# CardExtensionContext - свойства
##  __Свойства
[CancellationToken](P_Tessa_Cards_Extensions_CardExtensionContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
---|---  
[CardMetadata](P_Tessa_Cards_Extensions_CardExtensionContext_CardMetadata.htm)|
Метаинформация по типам карточек, известным в системе.  
[CardType](P_Tessa_Cards_Extensions_CardExtensionContext_CardType.htm)|  Тип
карточки или null, если тип карточки неизвестен.  
[CardTypeName](P_Tessa_Cards_Extensions_CardExtensionContext_CardTypeName.htm)|
Уникальное имя типа карточки или null, если тип карточки неизвестен. Имя может
не соответствовать действительному типу в метаинформации.  
[DbScope](P_Tessa_Cards_Extensions_CardExtensionContext_DbScope.htm)|  Объект,
обеспечивающий взаимодействие с базой данных. Значение равно null на клиенте и
не равно null на сервере.  
[EnableTracing](P_Tessa_Cards_Extensions_CardExtensionContext_EnableTracing.htm)|
Признак того, что для текущего метода расширений разрешена запись сообщения
трассировки при включённой в системе трассировке. Установка значения равным
false позволяет запретить запись сообщения, например, для реализации метода,
которая по умолчанию не выполняет полезной работы. При отключённой сортировке
значение равно false.  
[Info](P_Tessa_Cards_Extensions_CardExtensionContext_Info.htm)|  Информация,
передаваемая между расширениями в процессе взаимодействия с карточкой.  
[RequestIsSuccessful](P_Tessa_Cards_Extensions_CardExtensionContext_RequestIsSuccessful.htm)|
Признак того, что процесс взаимодействия с карточкой завершился успешно. Можно
использовать в расширениях, выполняющихся после запроса к сервису.  
[Session](P_Tessa_Cards_Extensions_CardExtensionContext_Session.htm)| Сессия
пользователя, для которого выполняется процесс взаимодействия с карточкой.  
[ValidationResult](P_Tessa_Cards_Extensions_CardExtensionContext_ValidationResult.htm)|
Объект, выполняющий построение результата валидации. Может использоваться для
того, чтобы запретить выполнение процесса стандартными средствами.  
## __См. также
#### Ссылки
[CardExtensionContext - ](T_Tessa_Cards_Extensions_CardExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
