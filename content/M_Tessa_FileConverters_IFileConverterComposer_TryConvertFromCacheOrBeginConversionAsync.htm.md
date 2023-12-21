# IFileConverterComposer.TryConvertFromCacheOrBeginConversionAsync - метод
Возвращает результат конвертации, если объект доступен через кэш, или null,
если объект недоступен, и был запущен асинхронный процесс конвертации файла
карточки в заданный формат, и возвращает идентификатор операции, по которой
можно контролировать ход конвертации. Файл после конвертации обычно помещается
в кэш. Вторым полем возвращает идентификатор операции, по которой можно
контролировать ход конвертации. Он актуален только в том случае, если метод
первым полем вернул null, т.е. не удалось получить значение из кэша.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    Task<(IFileConverterResponse response, Guid operationID)> TryConvertFromCacheOrBeginConversionAsync(
    	IFileConverterRequest request,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function TryConvertFromCacheOrBeginConversionAsync ( 
    	request As IFileConverterRequest,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of (response As IFileConverterResponse, operationID As Guid))
C++ __Копировать
    Task<ValueTuple<IFileConverterResponse^, Guid>>^ TryConvertFromCacheOrBeginConversionAsync(
    	IFileConverterRequest^ request, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract TryConvertFromCacheOrBeginConversionAsync : 
            request : IFileConverterRequest * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValueTuple<IFileConverterResponse, Guid>> 
#### Параметры
request
[IFileConverterRequest](T_Tessa_FileConverters_IFileConverterRequest.htm)
    Запрос на выполнение операции.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValueTuple](https://learn.microsoft.com/dotnet/api/system.valuetuple-2)<[IFileConverterResponse](T_Tessa_FileConverters_IFileConverterResponse.htm),
[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>>  
Результат конвертации, если объект доступен через кэш, или null, если объект
недоступен, и был запущен асинхронный процесс конвертации.
## __См. также
#### Ссылки
[IFileConverterComposer - ](T_Tessa_FileConverters_IFileConverterComposer.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
