# IFileVersion - свойства
##  __Свойства
[Cancellation](P_Tessa_Files_IFileObject_Cancellation.htm)|  Объект, который
может использоваться для отмены асинхронных операций с файлом или версией
файла, которые поддерживают отмену. На текущий момент это доступно для
загрузки содержимого версии файла.  
(Унаследован от [IFileObject](T_Tessa_Files_IFileObject.htm))  
---|---  
[Content](P_Tessa_Files_IFileObject_Content.htm)|  Контент файла или версии
файла. Контент файла обычно равен контенту его последней версии, но имя файла
на файловой системе может отличаться.  
(Унаследован от [IFileObject](T_Tessa_Files_IFileObject.htm))  
[ContentSource](P_Tessa_Files_IFileVersion_ContentSource.htm)| Местоположение
контента версии файла.  
[ContentState](P_Tessa_Files_IFileObject_ContentState.htm)|  Состояние
загрузки контента файла или версии файла в кэш для последующего отображения
пользователю.  
(Унаследован от [IFileObject](T_Tessa_Files_IFileObject.htm))  
[Created](P_Tessa_Files_IFileVersion_Created.htm)| Дата создания версии.  
[CreatedByID](P_Tessa_Files_IFileVersion_CreatedByID.htm)| Идентификатор
пользователя, который создал версию.  
[CreatedByName](P_Tessa_Files_IFileVersion_CreatedByName.htm)| Имя
пользователя, который создал версию.  
[ErrorInfo](P_Tessa_Files_IFileVersion_ErrorInfo.htm)|  Информация по ошибке,
возникшей при сохранении версии файла, или null, если ошибок не было.  
[File](P_Tessa_Files_IFileVersion_File.htm)|  Файл, к которому относится
версия. Свойства файла имеют текущее состояние, а не таковое на момент
создания версии.  
[Hash](P_Tessa_Files_IFileObject_Hash.htm)|  Хеш контента файла или версии
файла, или null, если хеш не вычислен. Хеш является необязательным свойством,
которое по умолчанию не заполняется системой.  
(Унаследован от [IFileObject](T_Tessa_Files_IFileObject.htm))  
[ID](P_Tessa_Files_IFileEntity_ID.htm)| Идентификатор объекта.  
(Унаследован от [IFileEntity](T_Tessa_Files_IFileEntity.htm))  
[Info](P_Tessa_Files_IFileObject_Info.htm)| Дополнительная информация,
используемая в расширениях.  
(Унаследован от [IFileObject](T_Tessa_Files_IFileObject.htm))  
[LinkID](P_Tessa_Files_IFileVersion_LinkID.htm)|  Внешний идентификатор версии
файла или null, если такой идентификатор не задан. Может использоваться в
расширениях для связи с содержимым во внешнем местоположении.  
[Name](P_Tessa_Files_IFileObject_Name.htm)|  Имя файла или версии файла,
которое является допустимым именем файла на файловой системе, но может
отличаться от отображаемого имени файла.  
(Унаследован от [IFileObject](T_Tessa_Files_IFileObject.htm))  
[Number](P_Tessa_Files_IFileVersion_Number.htm)|  Порядковый номер версии
файла, отсчитываемый от 1.  
[Options](P_Tessa_Files_IFileObject_Options.htm)| Настройки файла или версии
файла. Сериализуются в карточке в форме JSON.  
(Унаследован от [IFileObject](T_Tessa_Files_IFileObject.htm))  
[RequestInfo](P_Tessa_Files_IFileObject_RequestInfo.htm)|  Дополнительная
пользовательская информация, передаваемая в запросы к серверу, которые
относятся к загрузке содержимого файла/версии, к загрузке списка версий файла
или к загрузке списка подписей.  
(Унаследован от [IFileObject](T_Tessa_Files_IFileObject.htm))  
[Signatures](P_Tessa_Files_IFileVersion_Signatures.htm)| Подписи для версии
файла.  
[Size](P_Tessa_Files_IFileObject_Size.htm)|  Размер файла или версии файла в
байтах. Устанавливается при создании объекта и затем обновляется в зависимости
от действительного размера контента [IFileContent.Size]. Значение
[FileContent.UnknownSize] определяет, что размер неизвестен.  
(Унаследован от [IFileObject](T_Tessa_Files_IFileObject.htm))  
[Source](P_Tessa_Files_IFileEntity_Source.htm)|  Объект, обеспечивающий
взаимодействие текущего объекта с подсистемой, в которой он был создан,
например, с карточкой.  
(Унаследован от [IFileEntity](T_Tessa_Files_IFileEntity.htm))  
[State](P_Tessa_Files_IFileVersion_State.htm)| Состояние версии файла.  
[Tags](P_Tessa_Files_IFileVersion_Tags.htm)|  Теги, связанные с версией файла.
Например, признак того, что размер содержимого файла трактуется как большой
файл, поэтому файл не копируется во временную папку.  
## __См. также
#### Ссылки
[IFileVersion - ](T_Tessa_Files_IFileVersion.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
