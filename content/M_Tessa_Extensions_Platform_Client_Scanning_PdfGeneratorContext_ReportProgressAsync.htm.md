# PdfGeneratorContext.ReportProgressAsync - метод
Отображает пользователю текущий прогресс операции.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Scanning](N_Tessa_Extensions_Platform_Client_Scanning.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public Task ReportProgressAsync(
    	double progressPercentage,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function ReportProgressAsync ( 
    	progressPercentage As Double,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ ReportProgressAsync(
    	double progressPercentage, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract ReportProgressAsync : 
            progressPercentage : float * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override ReportProgressAsync : 
            progressPercentage : float * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
progressPercentage
[Double](https://learn.microsoft.com/dotnet/api/system.double)
    Текущий прогресс операции в процентах.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[IPdfGeneratorContext.ReportProgressAsync(Double,
CancellationToken)](M_Tessa_Extensions_Platform_Client_Scanning_IPdfGeneratorContext_ReportProgressAsync.htm)  
##  __См. также
#### Ссылки
[PdfGeneratorContext -
](T_Tessa_Extensions_Platform_Client_Scanning_PdfGeneratorContext.htm)
[Tessa.Extensions.Platform.Client.Scanning - пространство
имён](N_Tessa_Extensions_Platform_Client_Scanning.htm)
