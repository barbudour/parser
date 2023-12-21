# ICardTemporaryRole.CheckHasPlannedForRoleAsync - метод
Наполняет состав временной роли. Возвращает признак того, что состав успешно
получен.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<bool> CheckHasPlannedForRoleAsync(
    	DbManager db,
    	IQueryBuilderFactory builderFactory,
    	IValidationResultBuilder validationResult,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function CheckHasPlannedForRoleAsync ( 
    	db As DbManager,
    	builderFactory As IQueryBuilderFactory,
    	validationResult As IValidationResultBuilder,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
    Task<bool>^ CheckHasPlannedForRoleAsync(
    	DbManager^ db, 
    	IQueryBuilderFactory^ builderFactory, 
    	IValidationResultBuilder^ validationResult, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract CheckHasPlannedForRoleAsync : 
            db : DbManager * 
            builderFactory : IQueryBuilderFactory * 
            validationResult : IValidationResultBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
#### Параметры
db [DbManager](T_Tessa_Platform_Data_DbManager.htm)
     Объект, выполняющий SQL-запросы. Не может быть равен null. 
builderFactory
[IQueryBuilderFactory](T_Tessa_Platform_Data_IQueryBuilderFactory.htm)
    Объект для генерации текста запросов.
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
     Объект, содержащий результат валидации. Не может быть равен null. В случае ошибки, когда метод возвращает false, в результат валидации записывается информация по произошедшей ошибке. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если состав роли успешно получен; false, если при получении состава роли
возникли ошибки.
## __См. также
#### Ссылки
[ICardTemporaryRole - ](T_Tessa_Cards_ComponentModel_ICardTemporaryRole.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
