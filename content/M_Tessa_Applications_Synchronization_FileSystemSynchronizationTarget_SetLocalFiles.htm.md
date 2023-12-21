# FileSystemSynchronizationTarget.SetLocalFiles - метод
Задаёт информацию о локальных файлах.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IFileSystemSynchronizationTarget SetLocalFiles(
    	[CanBeNullAttribute] LocalFileEntryCollection localFiles
    )
VB __Копировать
     Public Function SetLocalFiles ( 
    	<CanBeNullAttribute> localFiles As LocalFileEntryCollection
    ) As IFileSystemSynchronizationTarget
C++ __Копировать
     public:
    virtual IFileSystemSynchronizationTarget^ SetLocalFiles(
    	[CanBeNullAttribute] LocalFileEntryCollection^ localFiles
    ) sealed
F# __Копировать
     abstract SetLocalFiles : 
            [<CanBeNullAttribute>] localFiles : LocalFileEntryCollection -> IFileSystemSynchronizationTarget 
    override SetLocalFiles : 
            [<CanBeNullAttribute>] localFiles : LocalFileEntryCollection -> IFileSystemSynchronizationTarget 
#### Параметры
localFiles
[LocalFileEntryCollection](T_Tessa_Applications_Synchronization_LocalFileEntryCollection.htm)
    Коллекция содержащая информацию о локальных файлах.
#### Возвращаемое значение
[IFileSystemSynchronizationTarget](T_Tessa_Applications_Synchronization_IFileSystemSynchronizationTarget.htm)  
Целевой объект синхронизации.
#### Реализации
[IFileSystemSynchronizationTarget.SetLocalFiles(LocalFileEntryCollection)](M_Tessa_Applications_Synchronization_IFileSystemSynchronizationTarget_SetLocalFiles.htm)  
##  __См. также
#### Ссылки
[FileSystemSynchronizationTarget -
](T_Tessa_Applications_Synchronization_FileSystemSynchronizationTarget.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
