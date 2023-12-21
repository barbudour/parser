# FileSystemSynchronizationTarget.SyncFolder - метод
Устанавливает папку синхронизации.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IFileSystemSynchronizationTarget SyncFolder(
    	string syncFolder
    )
VB __Копировать
     Public Function SyncFolder ( 
    	syncFolder As String
    ) As IFileSystemSynchronizationTarget
C++ __Копировать
     public:
    virtual IFileSystemSynchronizationTarget^ SyncFolder(
    	String^ syncFolder
    ) sealed
F# __Копировать
     abstract SyncFolder : 
            syncFolder : string -> IFileSystemSynchronizationTarget 
    override SyncFolder : 
            syncFolder : string -> IFileSystemSynchronizationTarget 
#### Параметры
syncFolder [String](https://learn.microsoft.com/dotnet/api/system.string)
     Папка синхронизации. 
#### Возвращаемое значение
[IFileSystemSynchronizationTarget](T_Tessa_Applications_Synchronization_IFileSystemSynchronizationTarget.htm)  
Целевой объект синхронизации.
#### Реализации
[IFileSystemSynchronizationTarget.SyncFolder(String)](M_Tessa_Applications_Synchronization_IFileSystemSynchronizationTarget_SyncFolder.htm)  
##  __См. также
#### Ссылки
[FileSystemSynchronizationTarget -
](T_Tessa_Applications_Synchronization_FileSystemSynchronizationTarget.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
