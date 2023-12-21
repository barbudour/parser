# FileConverterResponse.GetStreamOrThrowAsync - метод
Возвращает поток с содержимым файла. Возвращённое значение потока не равно
null. В случае ошибок в
[Tessa.FileConverters.IFileConverterResponse.ValidationResult] или в случае,
если ожидание результата не было завершено, т.е.
[Tessa.FileConverters.IFileConverterResponse.HasAwaitedResult] равен false,
выбрасывается исключение.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<Stream> GetStreamOrThrowAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetStreamOrThrowAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Stream)
C++ __Копировать
     public:
    virtual ValueTask<Stream^> GetStreamOrThrowAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetStreamOrThrowAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<Stream> 
    override GetStreamOrThrowAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<Stream> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)>  
Поток с содержимым файла. Возвращённое значение не равно null.
#### Реализации
[IFileConverterResponse.GetStreamOrThrowAsync(CancellationToken)](M_Tessa_FileConverters_IFileConverterResponse_GetStreamOrThrowAsync.htm)  
##  __Исключения
[InvalidOperationException]|  В результате операции
[Tessa.FileConverters.IFileConverterResponse.ValidationResult] присутствуют
ошибки.  
---|---  
## __См. также
#### Ссылки
[FileConverterResponse - ](T_Tessa_FileConverters_FileConverterResponse.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
