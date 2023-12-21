# CardValidationResult.Context - свойство
Контекст валидации, для которого был создан результат, или null, если
результат не связан с контекстом (например, он был пустой).
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ICardValidationContext Context { get; }
VB __Копировать
     Public ReadOnly Property Context As ICardValidationContext
    	Get
C++ __Копировать
     public:
    virtual property ICardValidationContext^ Context {
    	ICardValidationContext^ get () sealed;
    }
F# __Копировать
     abstract Context : ICardValidationContext with get
    override Context : ICardValidationContext with get
#### Значение свойства
[ICardValidationContext](T_Tessa_Cards_Validation_ICardValidationContext.htm)
#### Реализации
[ICardValidationResult.Context](P_Tessa_Cards_Validation_ICardValidationResult_Context.htm)  
##  __См. также
#### Ссылки
[CardValidationResult - ](T_Tessa_Cards_Validation_CardValidationResult.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
