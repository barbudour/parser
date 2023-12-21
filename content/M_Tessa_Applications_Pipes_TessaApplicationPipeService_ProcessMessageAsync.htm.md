# TessaApplicationPipeService.ProcessMessageAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Pipes](N_Tessa_Applications_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<bool> ProcessMessageAsync(
    	ApplicationMessage message,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function ProcessMessageAsync ( 
    	message As ApplicationMessage,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Boolean)
C++ __Копировать
     public:
    virtual ValueTask<bool> ProcessMessageAsync(
    	ApplicationMessage^ message, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract ProcessMessageAsync : 
            message : ApplicationMessage * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<bool> 
    override ProcessMessageAsync : 
            message : ApplicationMessage * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<bool> 
#### Параметры
message
[ApplicationMessage](T_Tessa_Applications_Messages_ApplicationMessage.htm)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>
#### Реализации
[ITessaApplicationPipeService.ProcessMessageAsync(ApplicationMessage,
CancellationToken)](M_Tessa_Applications_Pipes_ITessaApplicationPipeService_ProcessMessageAsync.htm)  
##  __См. также
#### Ссылки
[TessaApplicationPipeService -
](T_Tessa_Applications_Pipes_TessaApplicationPipeService.htm)
[Tessa.Applications.Pipes - пространство имён](N_Tessa_Applications_Pipes.htm)
