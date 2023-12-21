# ApplicationManagerProcessServiceHost.StopServiceAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Services.ApplicationManager](N_Tessa_Applications_Services_ApplicationManager.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask StopServiceAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function StopServiceAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     public:
    virtual ValueTask StopServiceAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract StopServiceAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
    override StopServiceAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)
#### Реализации
[IApplicationManagerServiceHost.StopServiceAsync(CancellationToken)](M_Tessa_Applications_Services_ApplicationManager_IApplicationManagerServiceHost_StopServiceAsync.htm)  
##  __См. также
#### Ссылки
[ApplicationManagerProcessServiceHost -
](T_Tessa_Applications_Services_ApplicationManager_ApplicationManagerProcessServiceHost.htm)
[Tessa.Applications.Services.ApplicationManager - пространство
имён](N_Tessa_Applications_Services_ApplicationManager.htm)
