# CardTaskCompletionOptionSettingsBuilder.BuildAsync - метод
Создаёт итоговый объект
[CardTaskCompletionOptionSettings](T_Tessa_Cards_CardTaskCompletionOptionSettings.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<CardTaskCompletionOptionSettings> BuildAsync(
    	IValidationResultBuilder validationResult,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function BuildAsync ( 
    	validationResult As IValidationResultBuilder,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of CardTaskCompletionOptionSettings)
C++ __Копировать
     public:
    virtual ValueTask<CardTaskCompletionOptionSettings^> BuildAsync(
    	IValidationResultBuilder^ validationResult, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract BuildAsync : 
            validationResult : IValidationResultBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<CardTaskCompletionOptionSettings> 
    override BuildAsync : 
            validationResult : IValidationResultBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<CardTaskCompletionOptionSettings> 
#### Параметры
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
Объект, выполняющий построение результата валидации.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, с помощью которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[CardTaskCompletionOptionSettings](T_Tessa_Cards_CardTaskCompletionOptionSettings.htm)>  
Объект с настройками диалога.
#### Реализации
[ICardTaskCompletionOptionSettingsBuilder.BuildAsync(IValidationResultBuilder,
CancellationToken)](M_Tessa_Cards_ICardTaskCompletionOptionSettingsBuilder_BuildAsync.htm)  
##  __См. также
#### Ссылки
[CardTaskCompletionOptionSettingsBuilder -
](T_Tessa_Cards_CardTaskCompletionOptionSettingsBuilder.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
