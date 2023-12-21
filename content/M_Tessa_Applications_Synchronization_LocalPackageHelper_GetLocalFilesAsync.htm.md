# LocalPackageHelper.GetLocalFilesAsync - метод
Возвращает информацию о локальных файлах.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<LocalFileEntryCollection> GetLocalFilesAsync(
    	IEnumerable<string> applicationFolders,
    	ApplicationPackageBuilder packageBuilder,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function GetLocalFilesAsync ( 
    	applicationFolders As IEnumerable(Of String),
    	packageBuilder As ApplicationPackageBuilder,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of LocalFileEntryCollection)
C++ __Копировать
     public:
    static Task<LocalFileEntryCollection^>^ GetLocalFilesAsync(
    	IEnumerable<String^>^ applicationFolders, 
    	ApplicationPackageBuilder^ packageBuilder, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member GetLocalFilesAsync : 
            applicationFolders : IEnumerable<string> * 
            packageBuilder : ApplicationPackageBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<LocalFileEntryCollection> 
#### Параметры
applicationFolders
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
    Коллекция директорий содержащих файлы [LocalPackageFile](F_Tessa_Applications_ApplicationCardConstants_LocalPackageFile.htm).
packageBuilder
[ApplicationPackageBuilder](T_Tessa_Applications_Package_ApplicationPackageBuilder.htm)
    Построитель локального пакета приложения [LocalPackageFile](F_Tessa_Applications_ApplicationCardConstants_LocalPackageFile.htm).
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[LocalFileEntryCollection](T_Tessa_Applications_Synchronization_LocalFileEntryCollection.htm)>  
Коллекция доступных локально файлов.
##  __Заметки
Возращает информацию по локальным файлам содержащуюся в файлах
[LocalPackageFile](F_Tessa_Applications_ApplicationCardConstants_LocalPackageFile.htm).
##  __См. также
#### Ссылки
[LocalPackageHelper -
](T_Tessa_Applications_Synchronization_LocalPackageHelper.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
