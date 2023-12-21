# CardExtensionContext.ValidationResult - свойство
Объект, выполняющий построение результата валидации. Может использоваться для
того, чтобы запретить выполнение процесса стандартными средствами.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IValidationResultBuilder ValidationResult { get; set; }
VB __Копировать
     Public Property ValidationResult As IValidationResultBuilder
    	Get
    	Set
C++ __Копировать
     public:
    virtual property IValidationResultBuilder^ ValidationResult {
    	IValidationResultBuilder^ get () sealed;
    	void set (IValidationResultBuilder^ value) sealed;
    }
F# __Копировать
     abstract ValidationResult : IValidationResultBuilder with get, set
    override ValidationResult : IValidationResultBuilder with get, set
#### Значение свойства
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
#### Реализации
[ITraceableExtensionContext.ValidationResult](P_Tessa_Extensions_ITraceableExtensionContext_ValidationResult.htm)  
##  __См. также
#### Ссылки
[CardExtensionContext - ](T_Tessa_Cards_Extensions_CardExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
