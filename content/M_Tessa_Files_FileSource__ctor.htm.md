# FileSource - конструктор
Создаёт экземпляр класса с указанием фабрики, используемый для создания
файлов.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected FileSource(
    	IFileCache cache,
    	ISession session,
    	IFileManager manager = null
    )
VB __Копировать
     Protected Sub New ( 
    	cache As IFileCache,
    	session As ISession,
    	Optional manager As IFileManager = Nothing
    )
C++ __Копировать
     protected:
    FileSource(
    	IFileCache^ cache, 
    	ISession^ session, 
    	IFileManager^ manager = nullptr
    )
F# __Копировать
     new : 
            cache : IFileCache * 
            session : ISession * 
            ?manager : IFileManager 
    (* Defaults:
            let _manager = defaultArg manager null
    *)
    -> FileSource
#### Параметры
cache [IFileCache](T_Tessa_Files_IFileCache.htm)
    Кэш для контента файлов.
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
     Сессия пользователя, который используется для автоматического заполнения свойств в создаваемых токенах для файлов и версий файлов. 
manager [IFileManager](T_Tessa_Files_IFileManager.htm) (Optional)
     Объект, управляющий взаимодействием с файлами по умолчанию, или null, если используется стандартный [FileManager](T_Tessa_Files_FileManager.htm). 
## __См. также
#### Ссылки
[FileSource - ](T_Tessa_Files_FileSource.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
