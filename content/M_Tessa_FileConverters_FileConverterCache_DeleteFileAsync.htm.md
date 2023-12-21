# FileConverterCache.DeleteFileAsync - метод
Удаляет сконвертированный файл из кэша файлов, если он там присутствует.
Возвращает результат удаления с сообщениями об ошибках и предупреждениями, а
также признак того, был ли файл в кэше на момент вызова метода. Используйте
метод в таких сценариях, как конвертация, инициируемая с веб-сервиса, но
фактически выполняемая в плагине Chronos, где кэш файлов требуется как способ
передачи содержимого файла после конвертации. Если известно, что операция по
конвертации уникальна и результат конвертации не будет нужен, то посредством
этого метода можно удалить содержимое файла из кэша файлов.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<(ValidationResult result, bool fileExisted)> DeleteFileAsync(
    	Guid versionID,
    	byte[] requestHash,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function DeleteFileAsync ( 
    	versionID As Guid,
    	requestHash As Byte(),
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of (result As ValidationResult, fileExisted As Boolean))
C++ __Копировать
     public:
    virtual Task<ValueTuple<ValidationResult^, bool>>^ DeleteFileAsync(
    	Guid versionID, 
    	array<unsigned char>^ requestHash, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract DeleteFileAsync : 
            versionID : Guid * 
            requestHash : byte[] * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValueTuple<ValidationResult, bool>> 
    override DeleteFileAsync : 
            versionID : Guid * 
            requestHash : byte[] * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValueTuple<ValidationResult, bool>> 
#### Параметры
versionID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор версии исходного файла, конвертация которой выполнялась.
requestHash [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]
    Хеш от запроса на преобразование файла.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValueTuple](https://learn.microsoft.com/dotnet/api/system.valuetuple-2)<[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm),
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>>  
Результат удаления с сообщениями об ошибках и предупреждениями, а также
признак того, был ли файл в кэше на момент вызова метода.
#### Реализации
[IFileConverterCache.DeleteFileAsync(Guid, Byte[],
CancellationToken)](M_Tessa_FileConverters_IFileConverterCache_DeleteFileAsync.htm)  
##  __См. также
#### Ссылки
[FileConverterCache - ](T_Tessa_FileConverters_FileConverterCache.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
