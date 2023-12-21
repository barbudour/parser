# ApplicationManagerProcessServiceClient.UnregisterApplicationAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Services.ApplicationManager](N_Tessa_Applications_Services_ApplicationManager.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask UnregisterApplicationAsync(
    	int processId,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function UnregisterApplicationAsync ( 
    	processId As Integer,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     public:
    virtual ValueTask UnregisterApplicationAsync(
    	int processId, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract UnregisterApplicationAsync : 
            processId : int * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
    override UnregisterApplicationAsync : 
            processId : int * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
#### Параметры
processId [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)
#### Реализации
[IApplicationManagerPipeService.UnregisterApplicationAsync(Int32,
CancellationToken)](M_Tessa_Applications_Pipes_IApplicationManagerPipeService_UnregisterApplicationAsync.htm)  
##  __См. также
#### Ссылки
[ApplicationManagerProcessServiceClient -
](T_Tessa_Applications_Services_ApplicationManager_ApplicationManagerProcessServiceClient.htm)
[Tessa.Applications.Services.ApplicationManager - пространство
имён](N_Tessa_Applications_Services_ApplicationManager.htm)
