# TagParserCardTypeVisitor - конструктор
Создаёт экземпляр класса.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public TagParserCardTypeVisitor(
    	IValidationResultBuilder validationResult = null
    )
VB __Копировать
     Public Sub New ( 
    	Optional validationResult As IValidationResultBuilder = Nothing
    )
C++ __Копировать
     public:
    TagParserCardTypeVisitor(
    	IValidationResultBuilder^ validationResult = nullptr
    )
F# __Копировать
     new : 
            ?validationResult : IValidationResultBuilder 
    (* Defaults:
            let _validationResult = defaultArg validationResult null
    *)
    -> TagParserCardTypeVisitor
#### Параметры
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
(Optional)
     Результат валидации, полученный посредством посещения объектов типа карточки. Укажите null, чтобы был создан новый экземпляр класса [ValidationResultBuilder](T_Tessa_Platform_Validation_ValidationResultBuilder.htm). 
## __См. также
#### Ссылки
[TagParserCardTypeVisitor -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_TagParserCardTypeVisitor.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
