# CardNewContext.ValidationResult - свойство
Объект, выполняющий построение результата валидации. Требуется инициализация
посредством метода
[InitResponse(CardNewResponse)](M_Tessa_Cards_ComponentModel_CardNewContext_InitResponse.htm),
в противном случае возвращает null.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IValidationResultBuilder ValidationResult { get; }
VB __Копировать
     Public ReadOnly Property ValidationResult As IValidationResultBuilder
    	Get
C++ __Копировать
     public:
    property IValidationResultBuilder^ ValidationResult {
    	IValidationResultBuilder^ get ();
    }
F# __Копировать
     member ValidationResult : IValidationResultBuilder with get
#### Значение свойства
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
##  __См. также
#### Ссылки
[CardNewContext - ](T_Tessa_Cards_ComponentModel_CardNewContext.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
