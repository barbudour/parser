# FileSystemGlobalStorage.OpenCoreAsync - метод
Открывает разделяемое хранилище для записи или чтения. При необходимости
некоторое время ожидается снятие блокировки от других процессов.
## __Definition
 **Пространство имён:** [Tessa.Platform.IPC](N_Tessa_Platform_IPC.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override ValueTask<Stream> OpenCoreAsync(
    	bool write,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overrides Function OpenCoreAsync ( 
    	write As Boolean,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Stream)
C++ __Копировать
     protected:
    virtual ValueTask<Stream^> OpenCoreAsync(
    	bool write, 
    	CancellationToken cancellationToken = CancellationToken()
    ) override
F# __Копировать
     abstract OpenCoreAsync : 
            write : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<Stream> 
    override OpenCoreAsync : 
            write : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<Stream> 
#### Параметры
write [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
     Признак того, что в поток будет осуществляться запись. Если указано false, то потом будет использоваться только для чтения. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)>  
Поток, предоставляющий доступ на чтение или запись к текущему процессу. Поток
обязательно необходимо закрыть сразу после чтения или записи.
## __См. также
#### Ссылки
[FileSystemGlobalStorage - ](T_Tessa_Platform_IPC_FileSystemGlobalStorage.htm)
[Tessa.Platform.IPC - пространство имён](N_Tessa_Platform_IPC.htm)
