# FileConverterComposer.TryConvertFromCacheAsync - метод
Возвращает результат конвертации, который предоставляет доступ к потоку файла,
для которого была выполнена конвертация, но только если выходной файл
присутствует в кэше на момент вызова, т.е. конвертация выполнялась ранее. В
противном случае возвращает null, т.е. для получения файла потребуется
выполнить конвертацию. Вторым полем возвращает новое значение параметра
requestHash.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<(IFileConverterResponse response, byte[] )> TryConvertFromCacheAsync(
    	IFileConverterRequest request,
    	byte[] requestHash,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function TryConvertFromCacheAsync ( 
    	request As IFileConverterRequest,
    	requestHash As Byte(),
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of (response As IFileConverterResponse,  As Byte()))
C++ __Копировать
     public:
    virtual Task<ValueTuple<IFileConverterResponse^, array<unsigned char>^>>^ TryConvertFromCacheAsync(
    	IFileConverterRequest^ request, 
    	array<unsigned char>^ requestHash, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract TryConvertFromCacheAsync : 
            request : IFileConverterRequest * 
            requestHash : byte[] * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValueTuple<IFileConverterResponse, byte[]>> 
    override TryConvertFromCacheAsync : 
            request : IFileConverterRequest * 
            requestHash : byte[] * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValueTuple<IFileConverterResponse, byte[]>> 
#### Параметры
request
[IFileConverterRequest](T_Tessa_FileConverters_IFileConverterRequest.htm)
    Запрос на выполнение операции.
requestHash [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]
     Вычисленный хеш от запроса или null, если хеш будет вычислен в процессе выполнения метода. При первом вызове метода для одного и того же запроса рекомендуется передавать null, а при последующих вызовах - результат предыдущего вызова. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValueTuple](https://learn.microsoft.com/dotnet/api/system.valuetuple-2)<[IFileConverterResponse](T_Tessa_FileConverters_IFileConverterResponse.htm),
[Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]>>  
Результат конвертации, который предоставляет доступ к потоку файла, для
которого была выполнена конвертация, но только если выходной файл присутствует
в кэше на момент вызова, т.е. конвертация выполнялась ранее. В противном
случае возвращает null, т.е. для получения файла потребуется выполнить
конвертацию.
#### Реализации
[IFileConverterComposer.TryConvertFromCacheAsync(IFileConverterRequest,
Byte[],
CancellationToken)](M_Tessa_FileConverters_IFileConverterComposer_TryConvertFromCacheAsync.htm)  
##  __См. также
#### Ссылки
[FileConverterComposer - ](T_Tessa_FileConverters_FileConverterComposer.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
