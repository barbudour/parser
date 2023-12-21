# CardGetRequest - свойства
##  __Свойства
[AuthorTaskRowIDList](P_Tessa_Cards_CardGetRequest_AuthorTaskRowIDList.htm)|
Список идентификаторов заданий, все данные которых будут полностью загружены,
если такие задания доступны от имени автора.  
---|---  
[CardID](P_Tessa_Cards_CardRequestBase_CardID.htm)|  Идентификатор
запрашиваемой карточки или null, если запрашивается виртуальная карточка,
идентификатор которой задаётся другим способом.  
(Унаследован от [CardRequestBase](T_Tessa_Cards_CardRequestBase.htm))  
[CardTypeID](P_Tessa_Cards_CardRequestBase_CardTypeID.htm)|  Идентификатор
типа карточки. Значение необязательно для заполнения.  
(Унаследован от [CardRequestBase](T_Tessa_Cards_CardRequestBase.htm))  
[CardTypeName](P_Tessa_Cards_CardRequestBase_CardTypeName.htm)|  Имя типа
карточки. Значение необязательно для заполнения.  
(Унаследован от [CardRequestBase](T_Tessa_Cards_CardRequestBase.htm))  
[CompressionMode](P_Tessa_Cards_CardGetRequest_CompressionMode.htm)|  Способ
сжатия карточки.  
[Dynamic](P_Tessa_Cards_CardInfoStorageObject_Dynamic.htm)|  Объект,
осуществляющий доступ к текущему объекту через позднее связывание свойств.  
(Унаследован от
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm))  
[DynamicInfo](P_Tessa_Cards_CardInfoStorageObject_DynamicInfo.htm)|  Объект,
осуществляющий доступ к дополнительной пользовательской информации по текущему
объекту через позднее связывание свойств.  
(Унаследован от
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm))  
[ExportFormat](P_Tessa_Cards_CardGetRequest_ExportFormat.htm)|  Формат файла
для экспорта карточки. Актуально только при указании
[Method](P_Tessa_Cards_CardGetRequest_Method.htm) равным
[Export](T_Tessa_Cards_CardGetMethod.htm).  
[GetMode](P_Tessa_Cards_CardGetRequest_GetMode.htm)|  Способ открытия
карточки.  
[GetTaskMode](P_Tessa_Cards_CardGetRequest_GetTaskMode.htm)|  Способ загрузки
заданий в открываемой карточке.  
[Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm)|  Дополнительная
пользовательская информация.  
(Унаследован от
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm))  
[Method](P_Tessa_Cards_CardGetRequest_Method.htm)|  Способ загрузки карточки.  
[NewMode](P_Tessa_Cards_CardGetRequest_NewMode.htm)|  Способ создания пустых
строк для карточки.  
[RestrictionFlags](P_Tessa_Cards_CardGetRequest_RestrictionFlags.htm)|  Флаги,
ограничивающие загружаемую по карточке информацию. По умолчанию загружаемая
информация не ограничивается.  
[SectionsToExclude](P_Tessa_Cards_CardGetRequest_SectionsToExclude.htm)|
Список имён физических секций, которые не следует загружать. Не влияет на
виртуальные секции.  
[ServiceType](P_Tessa_Cards_CardRequestBase_ServiceType.htm)|  Тип сервиса, от
которого был получен текущий объект запроса. Позволяет определить надёжность
данных в запросе. При сериализации значение не передаётся с клиента на сервер.
Это свойство используется платформой, не рекомендуется устанавливать его
значение вручную.  
(Унаследован от [CardRequestBase](T_Tessa_Cards_CardRequestBase.htm))  
##  __См. также
#### Ссылки
[CardGetRequest - ](T_Tessa_Cards_CardGetRequest.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
