# FileConverterAggregateWorker.ConvertFileAsync - метод
Преобразует файл в заданный формат.
##  __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task ConvertFileAsync(
    	IFileConverterContext context,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function ConvertFileAsync ( 
    	context As IFileConverterContext,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ ConvertFileAsync(
    	IFileConverterContext^ context, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract ConvertFileAsync : 
            context : IFileConverterContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override ConvertFileAsync : 
            context : IFileConverterContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
context
[IFileConverterContext](T_Tessa_FileConverters_IFileConverterContext.htm)
    Контекст, содержащий информацию по выполняемому преобразованию.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[IFileConverterWorker.ConvertFileAsync(IFileConverterContext,
CancellationToken)](M_Tessa_FileConverters_IFileConverterWorker_ConvertFileAsync.htm)  
##  __Исключения
[System.NotSupportedException]|  Конвертация не может быть выполнена для
заданных параметров. Например, формат выходного файла не поддерживает, или
объект требует указания объекта Request в контексте.  
---|---  
## __См. также
#### Ссылки
[FileConverterAggregateWorker -
](T_Tessa_FileConverters_FileConverterAggregateWorker.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
