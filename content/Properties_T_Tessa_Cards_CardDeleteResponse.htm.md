# CardDeleteResponse - свойства
##  __Свойства
[CardTypeID](P_Tessa_Cards_CardDeleteResponse_CardTypeID.htm)|  Идентификатор
типа удалённой карточки или null, если тип не был определён, т.к. удаления не
произошло.  
---|---  
[CardTypeName](P_Tessa_Cards_CardDeleteResponse_CardTypeName.htm)|  Имя типа
удалённой карточки или null, если тип не был определён, т.к. удаления не
произошло.  
[ContentsToDelete](P_Tessa_Cards_CardDeleteResponse_ContentsToDelete.htm)|
Список контентов файлов, для которых было выполнено или должно быть выполнено
удаление, в зависимости от признака
[KeepFileContent](P_Tessa_Cards_CardDeleteRequest_KeepFileContent.htm). Может
быть равен null, если файлы отсутствуют и не требуется выполнять действий.
Свойство не является сериализуемым, не содержится в хранилище, а значит,
доступно только на сервере, не передаётся с сервера на клиент, и не
переносится при клонировании.  
[DeletedCardID](P_Tessa_Cards_CardDeleteResponse_DeletedCardID.htm)|
Идентификатор карточки удаления, которая содержит информацию об удалённой
карточке и может использоваться для её восстановления, или null, если карточка
была удалена без возможности восстановления или при удалении возникла ошибка.  
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
[RestoredCardID](P_Tessa_Cards_CardDeleteResponse_RestoredCardID.htm)|
Идентификатор восстановленной карточки или null, если восстановление карточки
не выполнялось или при восстановлении возникла ошибка.  
[ValidationResult](P_Tessa_Cards_CardResponseBase_ValidationResult.htm)|
Объект, используемый для построения результата валидации.  
(Унаследован от [CardResponseBase](T_Tessa_Cards_CardResponseBase.htm))  
##  __См. также
#### Ссылки
[CardDeleteResponse - ](T_Tessa_Cards_CardDeleteResponse.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
