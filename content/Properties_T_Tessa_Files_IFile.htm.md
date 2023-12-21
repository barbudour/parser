# IFile - свойства
##  __Свойства
[Cancellation](P_Tessa_Files_IFileObject_Cancellation.htm)|  Объект, который
может использоваться для отмены асинхронных операций с файлом или версией
файла, которые поддерживают отмену. На текущий момент это доступно для
загрузки содержимого версии файла.  
(Унаследован от [IFileObject](T_Tessa_Files_IFileObject.htm))  
---|---  
[Category](P_Tessa_Files_IFile_Category.htm)|  Категория файла или null, если
файл не имеет категории.  
[Content](P_Tessa_Files_IFileObject_Content.htm)|  Контент файла или версии
файла. Контент файла обычно равен контенту его последней версии, но имя файла
на файловой системе может отличаться.  
(Унаследован от [IFileObject](T_Tessa_Files_IFileObject.htm))  
[ContentState](P_Tessa_Files_IFileObject_ContentState.htm)|  Состояние
загрузки контента файла или версии файла в кэш для последующего отображения
пользователю.  
(Унаследован от [IFileObject](T_Tessa_Files_IFileObject.htm))  
[Hash](P_Tessa_Files_IFileObject_Hash.htm)|  Хеш контента файла или версии
файла, или null, если хеш не вычислен. Хеш является необязательным свойством,
которое по умолчанию не заполняется системой.  
(Унаследован от [IFileObject](T_Tessa_Files_IFileObject.htm))  
[ID](P_Tessa_Files_IFileEntity_ID.htm)| Идентификатор объекта.  
(Унаследован от [IFileEntity](T_Tessa_Files_IFileEntity.htm))  
[Info](P_Tessa_Files_IFileObject_Info.htm)| Дополнительная информация,
используемая в расширениях.  
(Унаследован от [IFileObject](T_Tessa_Files_IFileObject.htm))  
[InitialState](P_Tessa_Files_IFile_InitialState.htm)| Изначальное состояние
файла.  
[IsLocal](P_Tessa_Files_IFile_IsLocal.htm)|  Признак того, что файл был
загружен локально и отсутствует во внешней подсистеме. Значение используется
при просмотре превью или при открытии файла, только что добавленного в элемент
управления и не существующего на сервере.  
[Modified](P_Tessa_Files_IFile_Modified.htm)|  Дата и время последнего
изменения файла.  
[ModifiedByID](P_Tessa_Files_IFile_ModifiedByID.htm)|  Идентификатор
пользователя изменившего файл.  
[ModifiedByName](P_Tessa_Files_IFile_ModifiedByName.htm)|  Имя пользователя
изменившего файл.  
[Name](P_Tessa_Files_IFileObject_Name.htm)|  Имя файла или версии файла,
которое является допустимым именем файла на файловой системе, но может
отличаться от отображаемого имени файла.  
(Унаследован от [IFileObject](T_Tessa_Files_IFileObject.htm))  
[NewVersionTags](P_Tessa_Files_IFile_NewVersionTags.htm)|  Список тегов,
связанных с добавляемой версией файла, т.е. при изменении содержимого файла в
случае замены, редактирования и др. Сериализуются в карточке в форме строки.  
[Options](P_Tessa_Files_IFileObject_Options.htm)| Настройки файла или версии
файла. Сериализуются в карточке в форме JSON.  
(Унаследован от [IFileObject](T_Tessa_Files_IFileObject.htm))  
[Origin](P_Tessa_Files_IFile_Origin.htm)|  Исходный файл, из которого был
скопирован текущий файл, или null, если текущий файл не был скопирован.  
[Permissions](P_Tessa_Files_IFile_Permissions.htm)| Разрешения на действия с
файлом.  
[PreviewContent](P_Tessa_Files_IFile_PreviewContent.htm)|  Контент файла или
версии файла, используемый для предпросмотра. Обычно это ссылка на свойство
Content, но для файлов, которые конвертируются для предпросмотра (например,
конвертация docx в pdf), это будет независимый объект контента.  
[RequestInfo](P_Tessa_Files_IFileObject_RequestInfo.htm)|  Дополнительная
пользовательская информация, передаваемая в запросы к серверу, которые
относятся к загрузке содержимого файла/версии, к загрузке списка версий файла
или к загрузке списка подписей.  
(Унаследован от [IFileObject](T_Tessa_Files_IFileObject.htm))  
[Size](P_Tessa_Files_IFileObject_Size.htm)|  Размер файла или версии файла в
байтах. Устанавливается при создании объекта и затем обновляется в зависимости
от действительного размера контента [IFileContent.Size]. Значение
[FileContent.UnknownSize] определяет, что размер неизвестен.  
(Унаследован от [IFileObject](T_Tessa_Files_IFileObject.htm))  
[Source](P_Tessa_Files_IFileEntity_Source.htm)|  Объект, обеспечивающий
взаимодействие текущего объекта с подсистемой, в которой он был создан,
например, с карточкой.  
(Унаследован от [IFileEntity](T_Tessa_Files_IFileEntity.htm))  
[Type](P_Tessa_Files_IFile_Type.htm)| Тип файла.  
[Versions](P_Tessa_Files_IFile_Versions.htm)|  Список версий файла. Коллекция
может быть пустой, если информация по версиям ещё не была запрошена.  
## __См. также
#### Ссылки
[IFile - ](T_Tessa_Files_IFile.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
