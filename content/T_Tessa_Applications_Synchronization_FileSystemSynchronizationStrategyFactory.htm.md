# FileSystemSynchronizationStrategyFactory - делегат
Фабрика создания стратегии синхронизации
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    public delegate IFileSystemSynchronizationStrategy FileSystemSynchronizationStrategyFactory(
    	[NotNullAttribute] string syncPath,
    	[NotNullAttribute] LocalFileEntryCollection localFiles
    )
VB __Копировать
    <NotNullAttribute>
    Public Delegate Function FileSystemSynchronizationStrategyFactory ( 
    	<NotNullAttribute> syncPath As String,
    	<NotNullAttribute> localFiles As LocalFileEntryCollection
    ) As IFileSystemSynchronizationStrategy
C++ __Копировать
    [NotNullAttribute]
    public delegate IFileSystemSynchronizationStrategy^ FileSystemSynchronizationStrategyFactory(
    	[NotNullAttribute] String^ syncPath, 
    	[NotNullAttribute] LocalFileEntryCollection^ localFiles
    )
F# __Копировать
     [<NotNullAttribute>]
    type FileSystemSynchronizationStrategyFactory = 
        delegate of 
            [<NotNullAttribute>] syncPath : string * 
            [<NotNullAttribute>] localFiles : LocalFileEntryCollection -> IFileSystemSynchronizationStrategy
#### Параметры
syncPath [String](https://learn.microsoft.com/dotnet/api/system.string)
    Путь к синхронизируемой папке
localFiles
[LocalFileEntryCollection](T_Tessa_Applications_Synchronization_LocalFileEntryCollection.htm)
    Коллекция содержащая информацию о локальных файлах.
#### Возвращаемое значение
[IFileSystemSynchronizationStrategy](T_Tessa_Applications_Synchronization_IFileSystemSynchronizationStrategy.htm)  
Стратегия синхронизации файлов
##  __См. также
#### Ссылки
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
