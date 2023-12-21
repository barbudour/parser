# ApplicationPipeService.TryGetFaultedResultAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Pipes](N_Tessa_Applications_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<byte[]> TryGetFaultedResultAsync(
    	Guid rowID,
    	ApplicationHostConnectionInfo connectionInfo,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function TryGetFaultedResultAsync ( 
    	rowID As Guid,
    	connectionInfo As ApplicationHostConnectionInfo,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Byte())
C++ __Копировать
     public:
    virtual ValueTask<array<unsigned char>^> TryGetFaultedResultAsync(
    	Guid rowID, 
    	ApplicationHostConnectionInfo^ connectionInfo, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract TryGetFaultedResultAsync : 
            rowID : Guid * 
            connectionInfo : ApplicationHostConnectionInfo * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<byte[]> 
    override TryGetFaultedResultAsync : 
            rowID : Guid * 
            connectionInfo : ApplicationHostConnectionInfo * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<byte[]> 
#### Параметры
rowID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
connectionInfo
[ApplicationHostConnectionInfo](T_Tessa_Applications_Services_TessaServer_ApplicationHostConnectionInfo.htm)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]>
#### Реализации
[IApplicationPipeService.TryGetFaultedResultAsync(Guid,
ApplicationHostConnectionInfo,
CancellationToken)](M_Tessa_Applications_Pipes_IApplicationPipeService_TryGetFaultedResultAsync.htm)  
##  __См. также
#### Ссылки
[ApplicationPipeService -
](T_Tessa_Applications_Pipes_ApplicationPipeService.htm)
[Tessa.Applications.Pipes - пространство имён](N_Tessa_Applications_Pipes.htm)
