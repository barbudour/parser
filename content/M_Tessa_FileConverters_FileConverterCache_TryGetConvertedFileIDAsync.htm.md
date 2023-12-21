# FileConverterCache.TryGetConvertedFileIDAsync - метод
Возвращает идентификатор преобразованного файла в кэше по идентификатору
версии исходного файла и по хешу от запроса или null, если файл ещё не был
преобразован или операция неизвестна.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<Guid?> TryGetConvertedFileIDAsync(
    	Guid versionID,
    	byte[] requestHash,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function TryGetConvertedFileIDAsync ( 
    	versionID As Guid,
    	requestHash As Byte(),
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Guid?)
C++ __Копировать
     public:
    virtual Task<Nullable<Guid>>^ TryGetConvertedFileIDAsync(
    	Guid versionID, 
    	array<unsigned char>^ requestHash, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract TryGetConvertedFileIDAsync : 
            versionID : Guid * 
            requestHash : byte[] * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<Nullable<Guid>> 
    override TryGetConvertedFileIDAsync : 
            versionID : Guid * 
            requestHash : byte[] * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<Nullable<Guid>> 
#### Параметры
versionID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор версии исходного файла.
requestHash [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]
    Хеш от запроса на преобразование файла.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>>  
Идентификатор преобразованного файла в кэше или null, если файл ещё не был
преобразован с параметрами, определяемыми по хешу.
#### Реализации
[IFileConverterCache.TryGetConvertedFileIDAsync(Guid, Byte[],
CancellationToken)](M_Tessa_FileConverters_IFileConverterCache_TryGetConvertedFileIDAsync.htm)  
##  __См. также
#### Ссылки
[FileConverterCache - ](T_Tessa_FileConverters_FileConverterCache.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
