# RemoteFileContent - конструктор
Создаёт контент с указанием используемых функций. После вызова конструктора
объекта требуется инициализировать методом
[InitializeAsync(CancellationToken)](M_Tessa_Platform_IAsyncInitializable_InitializeAsync.htm).
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public RemoteFileContent(
    	Func<CancellationToken, ValueTask<Stream>> getContentFuncAsync,
    	Func<CancellationToken, ValueTask<long>> getSizeFuncAsync,
    	Uri uri = null,
    	Func<IFileContent, ValueTask> disposedActionAsync = null,
    	IFileCancellationSource cancellation = null,
    	bool isBoundToFileSource = false
    )
VB __Копировать
     Public Sub New ( 
    	getContentFuncAsync As Func(Of CancellationToken, ValueTask(Of Stream)),
    	getSizeFuncAsync As Func(Of CancellationToken, ValueTask(Of Long)),
    	Optional uri As Uri = Nothing,
    	Optional disposedActionAsync As Func(Of IFileContent, ValueTask) = Nothing,
    	Optional cancellation As IFileCancellationSource = Nothing,
    	Optional isBoundToFileSource As Boolean = false
    )
C++ __Копировать
     public:
    RemoteFileContent(
    	Func<CancellationToken, ValueTask<Stream^>>^ getContentFuncAsync, 
    	Func<CancellationToken, ValueTask<long long>>^ getSizeFuncAsync, 
    	Uri^ uri = nullptr, 
    	Func<IFileContent^, ValueTask>^ disposedActionAsync = nullptr, 
    	IFileCancellationSource^ cancellation = nullptr, 
    	bool isBoundToFileSource = false
    )
F# __Копировать
     new : 
            getContentFuncAsync : Func<CancellationToken, ValueTask<Stream>> * 
            getSizeFuncAsync : Func<CancellationToken, ValueTask<int64>> * 
            ?uri : Uri * 
            ?disposedActionAsync : Func<IFileContent, ValueTask> * 
            ?cancellation : IFileCancellationSource * 
            ?isBoundToFileSource : bool 
    (* Defaults:
            let _uri = defaultArg uri null
            let _disposedActionAsync = defaultArg disposedActionAsync null
            let _cancellation = defaultArg cancellation null
            let _isBoundToFileSource = defaultArg isBoundToFileSource false
    *)
    -> RemoteFileContent
#### Параметры
getContentFuncAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)>>
     Функция, возвращающая содержимое файла. Если функция возвращает null, то используется пустой поток [Null](https://learn.microsoft.com/dotnet/api/system.io.stream.null). 
getSizeFuncAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Int64](https://learn.microsoft.com/dotnet/api/system.int64)>>
    Функция, возвращающая размер содержимого.
uri [Uri](https://learn.microsoft.com/dotnet/api/system.uri) (Optional)
     Ссылка, описывающая местоположение удалённого контента файла, или null, если ссылка на контент отсутствует. 
disposedActionAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[IFileContent](T_Tessa_Files_IFileContent.htm),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)>
(Optional)
     Дополнительное действие, выполняемое в случае освобождения контента, или null, если такое действие не требуется. В параметр действия передаётся освобождаемый контент. 
cancellation
[IFileCancellationSource](T_Tessa_Files_IFileCancellationSource.htm)
(Optional)
     Объект, который может использоваться для отмены асинхронных операций с содержимым файла, если оно поддерживает отмену, или null, если создаётся новый экземпляр объекта. 
isBoundToFileSource
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
     Признак того, что контент был создан источником файлов, а не передан снаружи, поэтому для оптимизации обращения к содержимому можно использовать источник файлов. 
## __См. также
#### Ссылки
[RemoteFileContent - ](T_Tessa_Files_RemoteFileContent.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
