# IPdfGeneratorContext.ReportProgressAsync - метод
Отображает пользователю текущий прогресс операции.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Scanning](N_Tessa_Extensions_Platform_Client_Scanning.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     Task ReportProgressAsync(
    	double progressPercentage,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function ReportProgressAsync ( 
    	progressPercentage As Double,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
    Task^ ReportProgressAsync(
    	double progressPercentage, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract ReportProgressAsync : 
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
##  __См. также
#### Ссылки
[IPdfGeneratorContext -
](T_Tessa_Extensions_Platform_Client_Scanning_IPdfGeneratorContext.htm)
[Tessa.Extensions.Platform.Client.Scanning - пространство
имён](N_Tessa_Extensions_Platform_Client_Scanning.htm)
