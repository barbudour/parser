# ApplicationManagerPipeClient.RegisterApplicationAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Pipes](N_Tessa_Applications_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask RegisterApplicationAsync(
    	int processId,
    	string serviceAddress,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function RegisterApplicationAsync ( 
    	processId As Integer,
    	serviceAddress As String,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     public:
    virtual ValueTask RegisterApplicationAsync(
    	int processId, 
    	String^ serviceAddress, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract RegisterApplicationAsync : 
            processId : int * 
            serviceAddress : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
    override RegisterApplicationAsync : 
            processId : int * 
            serviceAddress : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
#### Параметры
processId [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
serviceAddress [String](https://learn.microsoft.com/dotnet/api/system.string)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)
#### Реализации
[IApplicationManagerPipeService.RegisterApplicationAsync(Int32, String,
CancellationToken)](M_Tessa_Applications_Pipes_IApplicationManagerPipeService_RegisterApplicationAsync.htm)  
##  __См. также
#### Ссылки
[ApplicationManagerPipeClient -
](T_Tessa_Applications_Pipes_ApplicationManagerPipeClient.htm)
[Tessa.Applications.Pipes - пространство имён](N_Tessa_Applications_Pipes.htm)
