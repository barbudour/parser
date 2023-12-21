# IScanProvider.GetSourcesAsync - метод
Возвращает список доступных источников сканирования. Значение null аналогично
пустому списку.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Scanning](N_Tessa_Extensions_Platform_Client_Scanning.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
    ValueTask<List<IScanSource>> GetSourcesAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function GetSourcesAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of List(Of IScanSource))
C++ __Копировать
    ValueTask<List<IScanSource^>^> GetSourcesAsync(
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetSourcesAsync : 
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
##  __См. также
#### Ссылки
[IScanProvider -
](T_Tessa_Extensions_Platform_Client_Scanning_IScanProvider.htm)
[Tessa.Extensions.Platform.Client.Scanning - пространство
имён](N_Tessa_Extensions_Platform_Client_Scanning.htm)
