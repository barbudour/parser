# StreamApplicationPackageFileEnumerable.GetPackageAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<ApplicationPackage> GetPackageAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetPackageAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of ApplicationPackage)
C++ __Копировать
     public:
    virtual ValueTask<ApplicationPackage^> GetPackageAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetPackageAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ApplicationPackage> 
    override GetPackageAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ApplicationPackage> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[ApplicationPackage](T_Tessa_Applications_Package_ApplicationPackage.htm)>
#### Реализации
[IApplicationPackageFileEnumerable.GetPackageAsync(CancellationToken)](M_Tessa_Applications_Synchronization_IApplicationPackageFileEnumerable_GetPackageAsync.htm)  
##  __См. также
#### Ссылки
[StreamApplicationPackageFileEnumerable -
](T_Tessa_Applications_Synchronization_StreamApplicationPackageFileEnumerable.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
