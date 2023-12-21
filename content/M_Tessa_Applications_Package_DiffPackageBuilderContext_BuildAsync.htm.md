# DiffPackageBuilderContext.BuildAsync - метод
Осуществляет построение пакета приложения
## __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<ApplicationPackage> BuildAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function BuildAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of ApplicationPackage)
C++ __Копировать
     public:
    virtual Task<ApplicationPackage^>^ BuildAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract BuildAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ApplicationPackage> 
    override BuildAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ApplicationPackage> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ApplicationPackage](T_Tessa_Applications_Package_ApplicationPackage.htm)>  
Пакет приложения
#### Реализации
[IApplicationPackageBuilderContext.BuildAsync(CancellationToken)](M_Tessa_Applications_Package_IApplicationPackageBuilderContext_BuildAsync.htm)  
##  __См. также
#### Ссылки
[DiffPackageBuilderContext -
](T_Tessa_Applications_Package_DiffPackageBuilderContext.htm)
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
