# FileConverterCache.GetFileAsync - метод
Возвращает объект со значениями: 1) результат обращения к кэшу, может
содержать сообщения об ошибках; 2) асинхронную функцию, которая создаёт поток
к содержимому преобразованного файла, который расположен в кэше (функция может
быть равна null, если возникли ошибки при доступе к кэшу); 3) размер
возвращаемого содержимого в байтах или -1, если содержимое отсутствует или
размер неизвестен.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<(ValidationResult result, Func<CancellationToken, ValueTask<Stream>> getContentAsyncFunc, long size)> GetFileAsync(
    	Guid convertedFileID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetFileAsync ( 
    	convertedFileID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of (result As ValidationResult, getContentAsyncFunc As Func(Of CancellationToken, ValueTask(Of Stream)), size As Long))
C++ __Копировать
     public:
    virtual Task<ValueTuple<ValidationResult^, Func<CancellationToken, ValueTask<Stream^>>^, long long>>^ GetFileAsync(
    	Guid convertedFileID, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetFileAsync : 
            convertedFileID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValueTuple<ValidationResult, Func<CancellationToken, ValueTask<Stream>>, int64>> 
    override GetFileAsync : 
            convertedFileID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValueTuple<ValidationResult, Func<CancellationToken, ValueTask<Stream>>, int64>> 
#### Параметры
convertedFileID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор файла в карточке кэша.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValueTuple](https://learn.microsoft.com/dotnet/api/system.valuetuple-3)<[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm),
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)>>,
[Int64](https://learn.microsoft.com/dotnet/api/system.int64)>>  
Асинхронная задача, возвращающая объект со значениями.
#### Реализации
[IFileConverterCache.GetFileAsync(Guid,
CancellationToken)](M_Tessa_FileConverters_IFileConverterCache_GetFileAsync.htm)  
##  __См. также
#### Ссылки
[FileConverterCache - ](T_Tessa_FileConverters_FileConverterCache.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
