# ScanDocumentGenerator.TryGenerateAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Scanning](N_Tessa_Extensions_Platform_Client_Scanning.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<(ScanDocument document, List<ITempFile> temporaryFiles, List<ITempFolder> temporaryFolders)> TryGenerateAsync(
    	ITempFile[] files,
    	Func<double, CancellationToken, Task> reportProgressActionAsync = null,
    	Object externalContext = null,
    	Dictionary<string, Object> info = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function TryGenerateAsync ( 
    	files As ITempFile(),
    	Optional reportProgressActionAsync As Func(Of Double, CancellationToken, Task) = Nothing,
    	Optional externalContext As Object = Nothing,
    	Optional info As Dictionary(Of String, Object) = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of (document As ScanDocument, temporaryFiles As List(Of ITempFile), temporaryFolders As List(Of ITempFolder)))
C++ __Копировать
     public:
    Task<ValueTuple<ScanDocument^, List<ITempFile^>^, List<ITempFolder^>^>>^ TryGenerateAsync(
    	array<ITempFile^>^ files, 
    	Func<double, CancellationToken, Task^>^ reportProgressActionAsync = nullptr, 
    	Object^ externalContext = nullptr, 
    	Dictionary<String^, Object^>^ info = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member TryGenerateAsync : 
            files : ITempFile[] * 
            ?reportProgressActionAsync : Func<float, CancellationToken, Task> * 
            ?externalContext : Object * 
            ?info : Dictionary<string, Object> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _reportProgressActionAsync = defaultArg reportProgressActionAsync null
            let _externalContext = defaultArg externalContext null
            let _info = defaultArg info null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValueTuple<ScanDocument, List<ITempFile>, List<ITempFolder>>> 
#### Параметры
files [ITempFile](T_Tessa_Platform_IO_ITempFile.htm)[]
reportProgressActionAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-3)<[Double](https://learn.microsoft.com/dotnet/api/system.double),
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)>
(Optional)
externalContext [Object](https://learn.microsoft.com/dotnet/api/system.object)
(Optional)
info
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)> (Optional)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValueTuple](https://learn.microsoft.com/dotnet/api/system.valuetuple-3)<[ScanDocument](T_Tessa_Extensions_Platform_Client_Scanning_ScanDocument.htm),
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[ITempFile](T_Tessa_Platform_IO_ITempFile.htm)>,
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[ITempFolder](T_Tessa_Platform_IO_ITempFolder.htm)>>>
##  __См. также
#### Ссылки
[ScanDocumentGenerator -
](T_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentGenerator.htm)
[Tessa.Extensions.Platform.Client.Scanning - пространство
имён](N_Tessa_Extensions_Platform_Client_Scanning.htm)
