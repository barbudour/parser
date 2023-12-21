# FileSystemSynchronizationSource.SyncFolder - метод
Устанавливает папку синхронизации
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    public IFileSystemSynchronizationSource SyncFolder(
    	[NotNullAttribute] string syncFolder
    )
VB __Копировать
    <NotNullAttribute>
    Public Function SyncFolder ( 
    	<NotNullAttribute> syncFolder As String
    ) As IFileSystemSynchronizationSource
C++ __Копировать
     public:
    [NotNullAttribute]
    IFileSystemSynchronizationSource^ SyncFolder(
    	[NotNullAttribute] String^ syncFolder
    )
F# __Копировать
     [<NotNullAttribute>]
    member SyncFolder : 
            [<NotNullAttribute>] syncFolder : string -> IFileSystemSynchronizationSource 
#### Параметры
syncFolder [String](https://learn.microsoft.com/dotnet/api/system.string)
     Папка синхронизации 
#### Возвращаемое значение
[IFileSystemSynchronizationSource](T_Tessa_Applications_Synchronization_IFileSystemSynchronizationSource.htm)  
Источник синхронизации файлов
## __См. также
#### Ссылки
[FileSystemSynchronizationSource -
](T_Tessa_Applications_Synchronization_FileSystemSynchronizationSource.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
