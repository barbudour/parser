# FileSystemSynchronizationStrategy - конструктор
Initializes a new instance of the
[FileSystemSynchronizationStrategy](T_Tessa_Applications_Synchronization_FileSystemSynchronizationStrategy.htm)
class. Initializes a new instance of the
[Object](https://learn.microsoft.com/dotnet/api/system.object) class.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public FileSystemSynchronizationStrategy(
    	[NotNullAttribute] string syncFolder,
    	[NotNullAttribute] ILogger logger,
    	[NotNullAttribute] IStorageFactory storageFactory,
    	[NotNullAttribute] LocalFileEntryCollection localFiles
    )
VB __Копировать
     Public Sub New ( 
    	<NotNullAttribute> syncFolder As String,
    	<NotNullAttribute> logger As ILogger,
    	<NotNullAttribute> storageFactory As IStorageFactory,
    	<NotNullAttribute> localFiles As LocalFileEntryCollection
    )
C++ __Копировать
     public:
    FileSystemSynchronizationStrategy(
    	[NotNullAttribute] String^ syncFolder, 
    	[NotNullAttribute] ILogger^ logger, 
    	[NotNullAttribute] IStorageFactory^ storageFactory, 
    	[NotNullAttribute] LocalFileEntryCollection^ localFiles
    )
F# __Копировать
     new : 
            [<NotNullAttribute>] syncFolder : string * 
            [<NotNullAttribute>] logger : ILogger * 
            [<NotNullAttribute>] storageFactory : IStorageFactory * 
            [<NotNullAttribute>] localFiles : LocalFileEntryCollection -> FileSystemSynchronizationStrategy
#### Параметры
syncFolder [String](https://learn.microsoft.com/dotnet/api/system.string)
     Папка синхронизации 
logger ILogger
     Логгер 
storageFactory
[IStorageFactory](T_Tessa_Applications_Containers_Storage_IStorageFactory.htm)
     Фабрика создания хранилища 
localFiles
[LocalFileEntryCollection](T_Tessa_Applications_Synchronization_LocalFileEntryCollection.htm)
    Коллекция содержащая информацию о локальных файлах.
##  __См. также
#### Ссылки
[FileSystemSynchronizationStrategy -
](T_Tessa_Applications_Synchronization_FileSystemSynchronizationStrategy.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
