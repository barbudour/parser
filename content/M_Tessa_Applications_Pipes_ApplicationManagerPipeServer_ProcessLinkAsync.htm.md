# ApplicationManagerPipeServer.ProcessLinkAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Pipes](N_Tessa_Applications_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<IPipeResponse> ProcessLinkAsync(
    	IPipeRequest request,
    	IPipeResponse response,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function ProcessLinkAsync ( 
    	request As IPipeRequest,
    	response As IPipeResponse,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of IPipeResponse)
C++ __Копировать
     public:
    ValueTask<IPipeResponse^> ProcessLinkAsync(
    	IPipeRequest^ request, 
    	IPipeResponse^ response, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member ProcessLinkAsync : 
            request : IPipeRequest * 
            response : IPipeResponse * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IPipeResponse> 
#### Параметры
request [IPipeRequest](T_Tessa_Platform_Pipes_IPipeRequest.htm)
response [IPipeResponse](T_Tessa_Platform_Pipes_IPipeResponse.htm)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IPipeResponse](T_Tessa_Platform_Pipes_IPipeResponse.htm)>
##  __См. также
#### Ссылки
[ApplicationManagerPipeServer -
](T_Tessa_Applications_Pipes_ApplicationManagerPipeServer.htm)
[Tessa.Applications.Pipes - пространство имён](N_Tessa_Applications_Pipes.htm)
