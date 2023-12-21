# ApplicationPackageReader.TryReadPackageAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<ApplicationPackage> TryReadPackageAsync(
    	ApplicationDownloadFlags flags = ApplicationDownloadFlags.None,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function TryReadPackageAsync ( 
    	Optional flags As ApplicationDownloadFlags = ApplicationDownloadFlags.None,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of ApplicationPackage)
C++ __Копировать
     public:
    ValueTask<ApplicationPackage^> TryReadPackageAsync(
    	ApplicationDownloadFlags flags = ApplicationDownloadFlags::None, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member TryReadPackageAsync : 
            ?flags : ApplicationDownloadFlags * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _flags = defaultArg flags ApplicationDownloadFlags.None
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ApplicationPackage> 
#### Параметры
flags
[ApplicationDownloadFlags](T_Tessa_Applications_Services_TessaServer_ApplicationDownloadFlags.htm)
(Optional)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[ApplicationPackage](T_Tessa_Applications_Package_ApplicationPackage.htm)>
##  __См. также
#### Ссылки
[ApplicationPackageReader -
](T_Tessa_Applications_Synchronization_ApplicationPackageReader.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
