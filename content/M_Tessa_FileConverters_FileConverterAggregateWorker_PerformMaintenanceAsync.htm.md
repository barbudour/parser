# FileConverterAggregateWorker.PerformMaintenanceAsync - метод
Выполняет обработку в процессе выполнения цикла обслуживания для очереди на
конвертацию файлов. Метод запускается множество раз внутри цикла с
переидичностью, заданной в конфигурационном файле.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task PerformMaintenanceAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function PerformMaintenanceAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ PerformMaintenanceAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract PerformMaintenanceAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override PerformMaintenanceAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[IFileConverterWorker.PerformMaintenanceAsync(CancellationToken)](M_Tessa_FileConverters_IFileConverterWorker_PerformMaintenanceAsync.htm)  
##  __См. также
#### Ссылки
[FileConverterAggregateWorker -
](T_Tessa_FileConverters_FileConverterAggregateWorker.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
