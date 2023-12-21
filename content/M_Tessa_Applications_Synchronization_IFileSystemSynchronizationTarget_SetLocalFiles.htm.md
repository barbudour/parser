# IFileSystemSynchronizationTarget.SetLocalFiles - метод
Задаёт информацию о локальных файлах.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    IFileSystemSynchronizationTarget SetLocalFiles(
    	[CanBeNullAttribute] LocalFileEntryCollection localFiles
    )
VB __Копировать
    <NotNullAttribute>
    Function SetLocalFiles ( 
    	<CanBeNullAttribute> localFiles As LocalFileEntryCollection
    ) As IFileSystemSynchronizationTarget
C++ __Копировать
    [NotNullAttribute]
    IFileSystemSynchronizationTarget^ SetLocalFiles(
    	[CanBeNullAttribute] LocalFileEntryCollection^ localFiles
    )
F# __Копировать
     [<NotNullAttribute>]
    abstract SetLocalFiles : 
            [<CanBeNullAttribute>] localFiles : LocalFileEntryCollection -> IFileSystemSynchronizationTarget 
#### Параметры
localFiles
[LocalFileEntryCollection](T_Tessa_Applications_Synchronization_LocalFileEntryCollection.htm)
    Коллекция содержащая информацию о локальных файлах.
#### Возвращаемое значение
[IFileSystemSynchronizationTarget](T_Tessa_Applications_Synchronization_IFileSystemSynchronizationTarget.htm)  
Целевой объект синхронизации.
##  __См. также
#### Ссылки
[IFileSystemSynchronizationTarget -
](T_Tessa_Applications_Synchronization_IFileSystemSynchronizationTarget.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
