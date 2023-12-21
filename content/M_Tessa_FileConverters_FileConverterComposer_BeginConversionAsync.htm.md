# FileConverterComposer.BeginConversionAsync - метод
Запускает процесс конвертации файла карточки в заданный формат и возвращает
идентификатор операции, по которой можно контролировать ход конвертации.
Вторым полем возвращает новое значение параметра requestHash. Файл после
конвертации обычно помещается в кэш, но этот метод всегда создаёт новую
операцию по конвертации, даже если конвертация этой версии файла уже была
выполнена и содержится в кэше.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<(Guid operationID, byte[] )> BeginConversionAsync(
    	IFileConverterRequest request,
    	byte[] requestHash,
    	bool failWhenHasSameRequestHash = true,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function BeginConversionAsync ( 
    	request As IFileConverterRequest,
    	requestHash As Byte(),
    	Optional failWhenHasSameRequestHash As Boolean = true,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of (operationID As Guid,  As Byte()))
C++ __Копировать
     public:
    virtual Task<ValueTuple<Guid, array<unsigned char>^>>^ BeginConversionAsync(
    	IFileConverterRequest^ request, 
    	array<unsigned char>^ requestHash, 
    	bool failWhenHasSameRequestHash = true, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract BeginConversionAsync : 
            request : IFileConverterRequest * 
            requestHash : byte[] * 
            ?failWhenHasSameRequestHash : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _failWhenHasSameRequestHash = defaultArg failWhenHasSameRequestHash true
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValueTuple<Guid, byte[]>> 
    override BeginConversionAsync : 
            request : IFileConverterRequest * 
            requestHash : byte[] * 
            ?failWhenHasSameRequestHash : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _failWhenHasSameRequestHash = defaultArg failWhenHasSameRequestHash true
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValueTuple<Guid, byte[]>> 
#### Параметры
request
[IFileConverterRequest](T_Tessa_FileConverters_IFileConverterRequest.htm)
    Запрос на выполнение операции.
requestHash [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]
     Вычисленный хеш от запроса или null, если хеш будет вычислен в процессе выполнения метода. При первом вызове метода для одного и того же запроса рекомендуется передавать null, а при последующих вызовах - результат предыдущего вызова. 
failWhenHasSameRequestHash
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
     Создание операции запрещено и вызовет [Tessa.Platform.Operations.OperationAlreadyExistsException], если в настоящий момент выполняется операция с таким же хешом requestHash. Укажите значение false, если возможно параллельное выполнение операций для одного и того же файла с теми же параметрами конвертации. Укажите значение true указывается, чтобы одинаковые операции по конвертации выполнялись параллельно, а повторная операция по конвертации не создавалась, вместо этого организуется ожидание по окончанию существующей операции. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValueTuple](https://learn.microsoft.com/dotnet/api/system.valuetuple-2)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid),
[Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]>>  
Идентификатор операции, по которой можно контролировать ход конвертации.
#### Реализации
[IFileConverterComposer.BeginConversionAsync(IFileConverterRequest, Byte[],
Boolean,
CancellationToken)](M_Tessa_FileConverters_IFileConverterComposer_BeginConversionAsync.htm)  
##  __См. также
#### Ссылки
[FileConverterComposer - ](T_Tessa_FileConverters_FileConverterComposer.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
