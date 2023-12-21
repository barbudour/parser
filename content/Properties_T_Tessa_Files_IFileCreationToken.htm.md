# IFileCreationToken - свойства
##  __Свойства
[Category](P_Tessa_Files_IFileCreationToken_Category.htm)|  Категория файла
или null, если файл не имеет категории.  
---|---  
[Hash](P_Tessa_Files_IFileCreationToken_Hash.htm)|  Хеш контента файла или
null, если хеш не вычислен. Хеш является необязательным свойством, которое по
умолчанию не заполняется системой.  
[ID](P_Tessa_Files_IFileCreationToken_ID.htm)|  Идентификатор файла или null,
если создаётся случайный идентификатор.  
[IsLocal](P_Tessa_Files_IFileCreationToken_IsLocal.htm)|  Признак того, что
файл был загружен локально и отсутствует во внешней подсистеме. Значение
используется при просмотре превью или при открытии файла, только что
добавленного в элемент управления и не существующего на сервере. По умолчанию
значение равно true.  
[LastVersionTags](P_Tessa_Files_IFileCreationToken_LastVersionTags.htm)|
Список тегов, связанных с последней существующей версией файла. Актуально для
загружаемых или копируемых файлов. В объект [Tessa.Files.IFile] такой список
не копируется.  
[Modified](P_Tessa_Files_IFileCreationToken_Modified.htm)|  Дата и время
последнего изменения файла.  
[ModifiedByID](P_Tessa_Files_IFileCreationToken_ModifiedByID.htm)|
Идентификатор пользователя изменившего файл.  
[ModifiedByName](P_Tessa_Files_IFileCreationToken_ModifiedByName.htm)|  Имя
пользователя изменившего файл.  
[Name](P_Tessa_Files_IFileCreationToken_Name.htm)| Имя файла, которое является
допустимым именем файла на файловой системе.  
[NewVersionTags](P_Tessa_Files_IFileCreationToken_NewVersionTags.htm)|  Список
тегов, связанных с добавляемой версией файла, т.е. при изменении содержимого
файла в случае замены, редактирования и др. Сериализуются в карточке в форме
строки.  
[Options](P_Tessa_Files_IFileCreationToken_Options.htm)| Настройки файла.
Сериализуются в карточке в форме JSON.  
[Permissions](P_Tessa_Files_IFileCreationToken_Permissions.htm)| Разрешения на
действия с файлом.  
[RequestInfo](P_Tessa_Files_IFileCreationToken_RequestInfo.htm)|
Дополнительная пользовательская информация, передаваемая в запросы к серверу,
которые относятся к загрузке содержимого файла и его версий, к загрузке списка
версий этого файла или к загрузке списка подписей.  
[Size](P_Tessa_Files_IFileCreationToken_Size.htm)|  Начальный размер
создаваемого файла в байтах. Задавать значение свойства имеет смысл для
файлов, контент которых может быть установлен позднее, чем запрошен размер.
Значение по умолчанию [FileContent.UnknownSize] определяет, что размер
неизвестен.  
[Type](P_Tessa_Files_IFileCreationToken_Type.htm)| Тип файла.  
##  __См. также
#### Ссылки
[IFileCreationToken - ](T_Tessa_Files_IFileCreationToken.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
