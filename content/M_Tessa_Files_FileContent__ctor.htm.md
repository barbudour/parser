# FileContent - конструктор
Создаёт экземпляр класса с заданными параметрами. После вызова конструктора
объекта требуется инициализировать методом
[InitializeAsync(CancellationToken)](M_Tessa_Platform_IAsyncInitializable_InitializeAsync.htm).
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected FileContent(
    	Func<IFileContent, ValueTask> disposedActionAsync = null,
    	IFileCancellationSource cancellation = null
    )
VB __Копировать
     Protected Sub New ( 
    	Optional disposedActionAsync As Func(Of IFileContent, ValueTask) = Nothing,
    	Optional cancellation As IFileCancellationSource = Nothing
    )
C++ __Копировать
     protected:
    FileContent(
    	Func<IFileContent^, ValueTask>^ disposedActionAsync = nullptr, 
    	IFileCancellationSource^ cancellation = nullptr
    )
F# __Копировать
     new : 
            ?disposedActionAsync : Func<IFileContent, ValueTask> * 
            ?cancellation : IFileCancellationSource 
    (* Defaults:
            let _disposedActionAsync = defaultArg disposedActionAsync null
            let _cancellation = defaultArg cancellation null
    *)
    -> FileContent
#### Параметры
disposedActionAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[IFileContent](T_Tessa_Files_IFileContent.htm),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)>
(Optional)
     Дополнительное действие, выполняемое в случае освобождения контента, или null, если такое действие не требуется. В параметр действия передаётся освобождаемый контент. 
cancellation
[IFileCancellationSource](T_Tessa_Files_IFileCancellationSource.htm)
(Optional)
     Объект, который может использоваться для отмены асинхронных операций с содержимым файла, если оно поддерживает отмену, или null, если создаётся новый экземпляр объекта. 
## __См. также
#### Ссылки
[FileContent - ](T_Tessa_Files_FileContent.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
