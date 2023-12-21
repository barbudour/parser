# FileConverter.ConvertFileAsync - метод
Выполняет асинхронную конвертацию файла карточки в заданный формат. Это
рекомендуемый способ выполнения конвертации. Возвращает асинхронный
[System.Threading.Tasks.Task], при завершении которого будет получен результат
конвертации, который предоставляет доступ к содержимому файла, для которого
была выполнена конвертация. Результат всегда не равен null, ошибки и
исключения будут сохранены в объекте результата.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<IFileConverterResponse> ConvertFileAsync(
    	IFileConverterRequest request,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function ConvertFileAsync ( 
    	request As IFileConverterRequest,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of IFileConverterResponse)
C++ __Копировать
     public:
    virtual Task<IFileConverterResponse^>^ ConvertFileAsync(
    	IFileConverterRequest^ request, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract ConvertFileAsync : 
            request : IFileConverterRequest * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<IFileConverterResponse> 
    override ConvertFileAsync : 
            request : IFileConverterRequest * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<IFileConverterResponse> 
#### Параметры
request
[IFileConverterRequest](T_Tessa_FileConverters_IFileConverterRequest.htm)
    Запрос на выполнение операции.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[IFileConverterResponse](T_Tessa_FileConverters_IFileConverterResponse.htm)>  
Результат конвертации, который предоставляет доступ к содержимому файла, для
которого была выполнена конвертация. Результат всегда не равен null, ошибки и
исключения будут сохранены в объекте результата.
#### Реализации
[IFileConverter.ConvertFileAsync(IFileConverterRequest,
CancellationToken)](M_Tessa_FileConverters_IFileConverter_ConvertFileAsync.htm)  
##  __См. также
#### Ссылки
[FileConverter - ](T_Tessa_FileConverters_FileConverter.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
