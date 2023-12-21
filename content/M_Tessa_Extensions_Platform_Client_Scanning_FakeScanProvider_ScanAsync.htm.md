# FakeScanProvider.ScanAsync - метод
Запускает сканирование для заданного источника. Возвращает признак того, что
сканирование было запущено и отсутствовали ошибки при запуске. Ошибки
выводятся на экран средствами текущего объекта.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Scanning](N_Tessa_Extensions_Platform_Client_Scanning.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<bool> ScanAsync(
    	IScanSource source,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function ScanAsync ( 
    	source As IScanSource,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Boolean)
C++ __Копировать
     public:
    virtual ValueTask<bool> ScanAsync(
    	IScanSource^ source, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract ScanAsync : 
            source : IScanSource * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<bool> 
    override ScanAsync : 
            source : IScanSource * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<bool> 
#### Параметры
source [IScanSource](T_Tessa_Host_IScanSource.htm)
    Источник (драйвер сканера), для которого запускается сканирование.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если сканирование было запущено и отсутствовали ошибки при запуске;
false в противном случае.
#### Реализации
[IScanProvider.ScanAsync(IScanSource,
CancellationToken)](M_Tessa_Extensions_Platform_Client_Scanning_IScanProvider_ScanAsync.htm)  
##  __См. также
#### Ссылки
[FakeScanProvider -
](T_Tessa_Extensions_Platform_Client_Scanning_FakeScanProvider.htm)
[Tessa.Extensions.Platform.Client.Scanning - пространство
имён](N_Tessa_Extensions_Platform_Client_Scanning.htm)
