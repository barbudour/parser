# FileVersionCreationToken - свойства
##  __Свойства
[ContentSource](P_Tessa_Files_FileVersionCreationToken_ContentSource.htm)|
Местоположение контента файла.  
---|---  
[Created](P_Tessa_Files_FileVersionCreationToken_Created.htm)| Дата создания
версии.  
[CreatedByID](P_Tessa_Files_FileVersionCreationToken_CreatedByID.htm)|
Идентификатор пользователя, который создал версию.  
[CreatedByName](P_Tessa_Files_FileVersionCreationToken_CreatedByName.htm)| Имя
пользователя, который создал версию.  
[ErrorInfo](P_Tessa_Files_FileVersionCreationToken_ErrorInfo.htm)|  Информация
по ошибке, возникшей при сохранении версии файла, или null, если ошибок не
было.  
[Hash](P_Tessa_Files_FileVersionCreationToken_Hash.htm)|  Хеш контента версии
файла или null, если хеш не вычислен. Хеш является необязательным свойством,
которое по умолчанию не заполняется системой.  
[ID](P_Tessa_Files_FileVersionCreationToken_ID.htm)|  Идентификатор версии
файла или null, если при создании версии ей присваивается новый идентификатор.  
[LinkID](P_Tessa_Files_FileVersionCreationToken_LinkID.htm)|  Внешний
идентификатор версии файла или null, если такой идентификатор не задан. Может
использоваться в расширениях для связи с содержимым во внешнем местоположении.  
[Name](P_Tessa_Files_FileVersionCreationToken_Name.htm)|  Имя файла
[IFileObject.Name] на момент создания версии. Если указано null или пустая
строка, то в момент создания версии будет использовано имя файла.  
[Number](P_Tessa_Files_FileVersionCreationToken_Number.htm)|  Порядковый номер
версии файла, отсчитываемый от 1. По умолчанию устанавливается номер, равный
1.  
[Options](P_Tessa_Files_FileVersionCreationToken_Options.htm)| Настройки
версии файла. Сериализуются в карточке в форме JSON.  
[RequestInfo](P_Tessa_Files_FileVersionCreationToken_RequestInfo.htm)|
Дополнительная пользовательская информация, передаваемая в запросы к серверу,
которые относятся к загрузке содержимого версии или к загрузке списка её
подписей.  
[Size](P_Tessa_Files_FileVersionCreationToken_Size.htm)|  Начальный размер
создаваемой версии файла в байтах. Задавать значение свойства имеет смысл для
версий, контент которых может быть установлен позднее, чем запрошен размер.
Значение по умолчанию [FileContent.UnknownSize] определяет, что размер
неизвестен.  
[State](P_Tessa_Files_FileVersionCreationToken_State.htm)|  Состояние версии
файла. По умолчанию устанавливается состояние
[Tessa.Files.FileVersionState.Created].  
[Tags](P_Tessa_Files_FileVersionCreationToken_Tags.htm)| Список тегов,
связанных с версией файла. Сериализуются в карточке в форме строки.  
##  __См. также
#### Ссылки
[FileVersionCreationToken - ](T_Tessa_Files_FileVersionCreationToken.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
