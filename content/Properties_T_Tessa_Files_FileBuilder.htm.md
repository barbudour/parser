# FileBuilder - свойства
##  __Свойства
[Author](P_Tessa_Files_FileBuilder_Author.htm)|  Автор файла, т.е.
пользователь, создавший файл, или null, если автором является текущий
пользователь.  
---|---  
[Category](P_Tessa_Files_FileBuilder_Category.htm)|  Категория файла или null,
если категория не указана.  
[ContentActionAsync](P_Tessa_Files_FileBuilder_ContentActionAsync.htm)|
Метод, инициализирующий контент файла для способа создания контента
[Action](T_Tessa_Files_FileBuilder_ContentCreationType.htm).  
[ContentFactoryAsync](P_Tessa_Files_FileBuilder_ContentFactoryAsync.htm)|
Функция, создающая контент файла для способа создания контента
[Factory](T_Tessa_Files_FileBuilder_ContentCreationType.htm).  
[ContentPath](P_Tessa_Files_FileBuilder_ContentPath.htm)|  Полный путь к
контенту файла для способа создания контента
[Path](T_Tessa_Files_FileBuilder_ContentCreationType.htm).  
[ContentStream](P_Tessa_Files_FileBuilder_ContentStream.htm)|  Полный путь к
потоку с контентом файла для способа создания контента
[Stream](T_Tessa_Files_FileBuilder_ContentCreationType.htm).  
[ContentType](P_Tessa_Files_FileBuilder_ContentType.htm)|  Способ создания
контента файла. По умолчанию значение
[Undefined](T_Tessa_Files_FileBuilder_ContentCreationType.htm) запрещает
создание файла.  
[Files](P_Tessa_Files_FileBuilder_Files.htm)|  Коллекция, в которую может быть
добавлен файл с уведомлением об изменениях.  
[FileTokenActionAsync](P_Tessa_Files_FileBuilder_FileTokenActionAsync.htm)|
Метод, выполняющий дополнительное изменение токена на создание файла перед
тем, как объект файла будет создан.  
[Modified](P_Tessa_Files_FileBuilder_Modified.htm)|  Дата и время последнего
изменения файла.  
[ModifiedByID](P_Tessa_Files_FileBuilder_ModifiedByID.htm)|  Идентификатор
пользователя изменившего файл.  
[ModifiedByName](P_Tessa_Files_FileBuilder_ModifiedByName.htm)|  Имя
пользователя изменившего файл.  
[Name](P_Tessa_Files_FileBuilder_Name.htm)|  Имя файла или null, если имя не
задано. Для значения null имя может быть автоматически определено по пути к
файлу [ContentPath](P_Tessa_Files_FileBuilder_ContentPath.htm).  
[Permissions](P_Tessa_Files_FileBuilder_Permissions.htm)|  Разрешения на
редактирование файла или null, если будут использоваться разрешения по
умолчанию. По умолчанию разрешения определяются источником файлов, но обычно
это файл со всеми разрешениями.  
[Source](P_Tessa_Files_FileBuilder_Source.htm)|  Источник файлов, используемый
для создания файла.  
[Type](P_Tessa_Files_FileBuilder_Type.htm)|  Тип файла или null, если тип
файла не указан. Для значения null источник файлов может указать стандартный
тип файла.  
[VersionTokenActionAsync](P_Tessa_Files_FileBuilder_VersionTokenActionAsync.htm)|
Метод, выполняющий дополнительное изменение токена на создание версии файла
перед тем, как объект версия будет создана.  
## __См. также
#### Ссылки
[FileBuilder - ](T_Tessa_Files_FileBuilder.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
