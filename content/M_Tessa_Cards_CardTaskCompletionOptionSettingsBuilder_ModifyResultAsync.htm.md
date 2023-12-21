# CardTaskCompletionOptionSettingsBuilder.ModifyResultAsync - метод
Метод для модификации результата билдера, вызывается при вызове
[BuildAsync(IValidationResultBuilder,
CancellationToken)](M_Tessa_Cards_CardTaskCompletionOptionSettingsBuilder_BuildAsync.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual Task ModifyResultAsync(
    	CardTaskCompletionOptionSettings result,
    	IValidationResultBuilder validationResult,
    	CancellationToken cancellationToken
    )
VB __Копировать
     Protected Overridable Function ModifyResultAsync ( 
    	result As CardTaskCompletionOptionSettings,
    	validationResult As IValidationResultBuilder,
    	cancellationToken As CancellationToken
    ) As Task
C++ __Копировать
     protected:
    virtual Task^ ModifyResultAsync(
    	CardTaskCompletionOptionSettings^ result, 
    	IValidationResultBuilder^ validationResult, 
    	CancellationToken cancellationToken
    )
F# __Копировать
     abstract ModifyResultAsync : 
            result : CardTaskCompletionOptionSettings * 
            validationResult : IValidationResultBuilder * 
            cancellationToken : CancellationToken -> Task 
    override ModifyResultAsync : 
            result : CardTaskCompletionOptionSettings * 
            validationResult : IValidationResultBuilder * 
            cancellationToken : CancellationToken -> Task 
#### Параметры
result
[CardTaskCompletionOptionSettings](T_Tessa_Cards_CardTaskCompletionOptionSettings.htm)
    Результат, который модифицируется данным методом.
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
    Результат валидации, куда записываются ошибки.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
    Объект, с помощью которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[CardTaskCompletionOptionSettingsBuilder -
](T_Tessa_Cards_CardTaskCompletionOptionSettingsBuilder.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
