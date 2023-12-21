# ApplicationPackageWriter.WritePackageAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task WritePackageAsync(
    	[NotNullAttribute] ApplicationPackage package,
    	ApplicationDownloadFlags flags = ApplicationDownloadFlags.None,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function WritePackageAsync ( 
    	<NotNullAttribute> package As ApplicationPackage,
    	Optional flags As ApplicationDownloadFlags = ApplicationDownloadFlags.None,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    Task^ WritePackageAsync(
    	[NotNullAttribute] ApplicationPackage^ package, 
    	ApplicationDownloadFlags flags = ApplicationDownloadFlags::None, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member WritePackageAsync : 
            [<NotNullAttribute>] package : ApplicationPackage * 
            ?flags : ApplicationDownloadFlags * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _flags = defaultArg flags ApplicationDownloadFlags.None
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
package
[ApplicationPackage](T_Tessa_Applications_Package_ApplicationPackage.htm)
flags
[ApplicationDownloadFlags](T_Tessa_Applications_Services_TessaServer_ApplicationDownloadFlags.htm)
(Optional)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
##  __См. также
#### Ссылки
[ApplicationPackageWriter -
](T_Tessa_Applications_Synchronization_ApplicationPackageWriter.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
