# IFileSystemSynchronizationTarget.SyncFolder - метод
Устанавливает папку синхронизации.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    IFileSystemSynchronizationTarget SyncFolder(
    	[NotNullAttribute] string syncFolder
    )
VB __Копировать
    <NotNullAttribute>
    Function SyncFolder ( 
    	<NotNullAttribute> syncFolder As String
    ) As IFileSystemSynchronizationTarget
C++ __Копировать
    [NotNullAttribute]
    IFileSystemSynchronizationTarget^ SyncFolder(
    	[NotNullAttribute] String^ syncFolder
    )
F# __Копировать
     [<NotNullAttribute>]
    abstract SyncFolder : 
            [<NotNullAttribute>] syncFolder : string -> IFileSystemSynchronizationTarget 
#### Параметры
syncFolder [String](https://learn.microsoft.com/dotnet/api/system.string)
     Папка синхронизации. 
#### Возвращаемое значение
[IFileSystemSynchronizationTarget](T_Tessa_Applications_Synchronization_IFileSystemSynchronizationTarget.htm)  
Целевой объект синхронизации.
## __См. также
#### Ссылки
[IFileSystemSynchronizationTarget -
](T_Tessa_Applications_Synchronization_IFileSystemSynchronizationTarget.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
