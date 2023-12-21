# ScanDocumentGenerator.TryGenerateCoreAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Scanning](N_Tessa_Extensions_Platform_Client_Scanning.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     protected abstract Task<ScanDocument> TryGenerateCoreAsync(
    	ITempFile[] files,
    	List<ITempFile> temporaryFiles,
    	List<ITempFolder> temporaryFolders,
    	Func<double, CancellationToken, Task> reportProgressActionAsync,
    	Object externalContext,
    	Dictionary<string, Object> info,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected MustOverride Function TryGenerateCoreAsync ( 
    	files As ITempFile(),
    	temporaryFiles As List(Of ITempFile),
    	temporaryFolders As List(Of ITempFolder),
    	reportProgressActionAsync As Func(Of Double, CancellationToken, Task),
    	externalContext As Object,
    	info As Dictionary(Of String, Object),
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of ScanDocument)
C++ __Копировать
     protected:
    virtual Task<ScanDocument^>^ TryGenerateCoreAsync(
    	array<ITempFile^>^ files, 
    	List<ITempFile^>^ temporaryFiles, 
    	List<ITempFolder^>^ temporaryFolders, 
    	Func<double, CancellationToken, Task^>^ reportProgressActionAsync, 
    	Object^ externalContext, 
    	Dictionary<String^, Object^>^ info, 
    	CancellationToken cancellationToken = CancellationToken()
    ) abstract
F# __Копировать
     abstract TryGenerateCoreAsync : 
            files : ITempFile[] * 
            temporaryFiles : List<ITempFile> * 
            temporaryFolders : List<ITempFolder> * 
            reportProgressActionAsync : Func<float, CancellationToken, Task> * 
            externalContext : Object * 
            info : Dictionary<string, Object> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ScanDocument> 
#### Параметры
files [ITempFile](T_Tessa_Platform_IO_ITempFile.htm)[]
temporaryFiles
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[ITempFile](T_Tessa_Platform_IO_ITempFile.htm)>
temporaryFolders
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[ITempFolder](T_Tessa_Platform_IO_ITempFolder.htm)>
reportProgressActionAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-3)<[Double](https://learn.microsoft.com/dotnet/api/system.double),
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)>
externalContext [Object](https://learn.microsoft.com/dotnet/api/system.object)
info
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ScanDocument](T_Tessa_Extensions_Platform_Client_Scanning_ScanDocument.htm)>
##  __См. также
#### Ссылки
[ScanDocumentGenerator -
](T_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentGenerator.htm)
[Tessa.Extensions.Platform.Client.Scanning - пространство
имён](N_Tessa_Extensions_Platform_Client_Scanning.htm)
