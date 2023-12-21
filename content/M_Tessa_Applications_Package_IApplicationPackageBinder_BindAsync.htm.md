# IApplicationPackageBinder.BindAsync - метод
Заполняет пакет приложения
## __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task BindAsync(
    	[NotNullAttribute] ApplicationPackage package,
    	[NotNullAttribute] IValidationResultBuilder validationResultBuilder,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function BindAsync ( 
    	<NotNullAttribute> package As ApplicationPackage,
    	<NotNullAttribute> validationResultBuilder As IValidationResultBuilder,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
    Task^ BindAsync(
    	[NotNullAttribute] ApplicationPackage^ package, 
    	[NotNullAttribute] IValidationResultBuilder^ validationResultBuilder, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract BindAsync : 
            [<NotNullAttribute>] package : ApplicationPackage * 
            [<NotNullAttribute>] validationResultBuilder : IValidationResultBuilder * 
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
##  __См. также
#### Ссылки
[IApplicationPackageBinder -
](T_Tessa_Applications_Package_IApplicationPackageBinder.htm)
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
