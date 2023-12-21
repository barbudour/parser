# CardValidationLimitationManager.GetCardResult - метод
Возвращает результат валидации для данных карточки, в котором ограничивается
набор сообщений для заданных секций и их строк.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValidationResult GetCardResult(
    	ICardValidationContext context,
    	ICardValidationResult result
    )
VB __Копировать
     Public Function GetCardResult ( 
    	context As ICardValidationContext,
    	result As ICardValidationResult
    ) As ValidationResult
C++ __Копировать
     public:
    virtual ValidationResult^ GetCardResult(
    	ICardValidationContext^ context, 
    	ICardValidationResult^ result
    ) sealed
F# __Копировать
     abstract GetCardResult : 
            context : ICardValidationContext * 
            result : ICardValidationResult -> ValidationResult 
    override GetCardResult : 
            context : ICardValidationContext * 
            result : ICardValidationResult -> ValidationResult 
#### Параметры
context
[ICardValidationContext](T_Tessa_Cards_Validation_ICardValidationContext.htm)
    Контекст валидации карточки.
result
[ICardValidationResult](T_Tessa_Cards_Validation_ICardValidationResult.htm)
    Результат валидации карточки.
#### Возвращаемое значение
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)  
Результат валидации для данных карточки, в котором ограничивается набор
сообщений для заданных секций и их строк.
#### Реализации
[ICardValidationLimitationManager.GetCardResult(ICardValidationContext,
ICardValidationResult)](M_Tessa_Cards_Validation_ICardValidationLimitationManager_GetCardResult.htm)  
##  __См. также
#### Ссылки
[CardValidationLimitationManager -
](T_Tessa_Cards_Validation_CardValidationLimitationManager.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
