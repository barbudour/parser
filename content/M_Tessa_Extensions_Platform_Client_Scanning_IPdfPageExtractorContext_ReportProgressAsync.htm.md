# IPdfPageExtractorContext.ReportProgressAsync - метод
Отображает пользователю текущий прогресс операции.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Scanning](N_Tessa_Extensions_Platform_Client_Scanning.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     ValueTask ReportProgressAsync(
    	double progressPercentage,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function ReportProgressAsync ( 
    	progressPercentage As Double,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     ValueTask ReportProgressAsync(
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
    -> ValueTask 
#### Параметры
progressPercentage
[Double](https://learn.microsoft.com/dotnet/api/system.double)
    Текущий прогресс операции в процентах.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)  
Асинхронная задача.
##  __См. также
#### Ссылки
[IPdfPageExtractorContext -
](T_Tessa_Extensions_Platform_Client_Scanning_IPdfPageExtractorContext.htm)
[Tessa.Extensions.Platform.Client.Scanning - пространство
имён](N_Tessa_Extensions_Platform_Client_Scanning.htm)
