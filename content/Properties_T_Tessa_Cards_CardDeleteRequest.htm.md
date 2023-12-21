# CardDeleteRequest - свойства
##  __Свойства
[CardID](P_Tessa_Cards_CardRequestBase_CardID.htm)|  Идентификатор
запрашиваемой карточки или null, если запрашивается виртуальная карточка,
идентификатор которой задаётся другим способом.  
(Унаследован от [CardRequestBase](T_Tessa_Cards_CardRequestBase.htm))  
---|---  
[CardTypeID](P_Tessa_Cards_CardRequestBase_CardTypeID.htm)|  Идентификатор
типа карточки. Значение необязательно для заполнения.  
(Унаследован от [CardRequestBase](T_Tessa_Cards_CardRequestBase.htm))  
[CardTypeName](P_Tessa_Cards_CardRequestBase_CardTypeName.htm)|  Имя типа
карточки. Значение необязательно для заполнения.  
(Унаследован от [CardRequestBase](T_Tessa_Cards_CardRequestBase.htm))  
[DeletionMode](P_Tessa_Cards_CardDeleteRequest_DeletionMode.htm)|  Способ
удаления карточки.  
[Dynamic](P_Tessa_Cards_CardInfoStorageObject_Dynamic.htm)|  Объект,
осуществляющий доступ к текущему объекту через позднее связывание свойств.  
(Унаследован от
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm))  
[DynamicInfo](P_Tessa_Cards_CardInfoStorageObject_DynamicInfo.htm)|  Объект,
осуществляющий доступ к дополнительной пользовательской информации по текущему
объекту через позднее связывание свойств.  
(Унаследован от
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm))  
[Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm)|  Дополнительная
пользовательская информация.  
(Унаследован от
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm))  
[KeepFileContent](P_Tessa_Cards_CardDeleteRequest_KeepFileContent.htm)|
Признак того, что контент файлов не должен быть удалён при удалении карточки.
Значение следует устанавливать только при вызове серверного API. При этом
информацию по наличию файлов будет удалена, поэтому указывайте значение true
только в том случае, если вызывающий код самостоятельно будет заботиться об
удалении контента.  
[Method](P_Tessa_Cards_CardDeleteRequest_Method.htm)|  Способ удаления
карточки.  
[ServiceType](P_Tessa_Cards_CardRequestBase_ServiceType.htm)|  Тип сервиса, от
которого был получен текущий объект запроса. Позволяет определить надёжность
данных в запросе. При сериализации значение не передаётся с клиента на сервер.
Это свойство используется платформой, не рекомендуется устанавливать его
значение вручную.  
(Унаследован от [CardRequestBase](T_Tessa_Cards_CardRequestBase.htm))  
##  __См. также
#### Ссылки
[CardDeleteRequest - ](T_Tessa_Cards_CardDeleteRequest.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
