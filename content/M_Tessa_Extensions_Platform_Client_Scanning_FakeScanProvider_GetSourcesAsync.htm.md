# FakeScanProvider.GetSourcesAsync - метод
Возвращает список доступных источников сканирования. Значение null аналогично
пустому списку.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Scanning](N_Tessa_Extensions_Platform_Client_Scanning.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<List<IScanSource>> GetSourcesAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetSourcesAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of List(Of IScanSource))
C++ __Копировать
     public:
    virtual ValueTask<List<IScanSource^>^> GetSourcesAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetSourcesAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<List<IScanSource>> 
    override GetSourcesAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<List<IScanSource>> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[IScanSource](T_Tessa_Host_IScanSource.htm)>>  
Список доступных источников сканирования.
#### Реализации
[IScanProvider.GetSourcesAsync(CancellationToken)](M_Tessa_Extensions_Platform_Client_Scanning_IScanProvider_GetSourcesAsync.htm)  
##  __См. также
#### Ссылки
[FakeScanProvider -
](T_Tessa_Extensions_Platform_Client_Scanning_FakeScanProvider.htm)
[Tessa.Extensions.Platform.Client.Scanning - пространство
имён](N_Tessa_Extensions_Platform_Client_Scanning.htm)
