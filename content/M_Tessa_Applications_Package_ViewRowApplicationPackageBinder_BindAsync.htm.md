# ViewRowApplicationPackageBinder.BindAsync - метод
Заполняет пакет приложения
## __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task BindAsync(
    	ApplicationPackage package,
    	IValidationResultBuilder validationResultBuilder,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function BindAsync ( 
    	package As ApplicationPackage,
    	validationResultBuilder As IValidationResultBuilder,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ BindAsync(
    	ApplicationPackage^ package, 
    	IValidationResultBuilder^ validationResultBuilder, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract BindAsync : 
            package : ApplicationPackage * 
            validationResultBuilder : IValidationResultBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override BindAsync : 
            package : ApplicationPackage * 
            validationResultBuilder : IValidationResultBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
package
[ApplicationPackage](T_Tessa_Applications_Package_ApplicationPackage.htm)
     Пакет приложения 
validationResultBuilder
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
    Построитель результатов валидации
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[IApplicationPackageBinder.BindAsync(ApplicationPackage,
IValidationResultBuilder,
CancellationToken)](M_Tessa_Applications_Package_IApplicationPackageBinder_BindAsync.htm)  
##  __См. также
#### Ссылки
[ViewRowApplicationPackageBinder -
](T_Tessa_Applications_Package_ViewRowApplicationPackageBinder.htm)
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
