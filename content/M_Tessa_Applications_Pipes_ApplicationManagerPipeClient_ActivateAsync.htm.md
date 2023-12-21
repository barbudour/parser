# ApplicationManagerPipeClient.ActivateAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Pipes](N_Tessa_Applications_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask ActivateAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function ActivateAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     public:
    virtual ValueTask ActivateAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract ActivateAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
    override ActivateAsync : 
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
[IApplicationManagerPipeService.ActivateAsync(CancellationToken)](M_Tessa_Applications_Pipes_IApplicationManagerPipeService_ActivateAsync.htm)  
##  __См. также
#### Ссылки
[ApplicationManagerPipeClient -
](T_Tessa_Applications_Pipes_ApplicationManagerPipeClient.htm)
[Tessa.Applications.Pipes - пространство имён](N_Tessa_Applications_Pipes.htm)
