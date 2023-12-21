# CardContentContext(ICardFileContentSource, IValidationResultBuilder) -
конструктор
Создаёт экземпляр объекта на основании свойств заданного объекта
[ICardFileContentSource](T_Tessa_Cards_ICardFileContentSource.htm).
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardContentContext(
    	ICardFileContentSource contentSource,
    	IValidationResultBuilder validationResult = null
    )
VB __Копировать
     Public Sub New ( 
    	contentSource As ICardFileContentSource,
    	Optional validationResult As IValidationResultBuilder = Nothing
    )
C++ __Копировать
     public:
    CardContentContext(
    	ICardFileContentSource^ contentSource, 
    	IValidationResultBuilder^ validationResult = nullptr
    )
F# __Копировать
     new : 
            contentSource : ICardFileContentSource * 
            ?validationResult : IValidationResultBuilder 
    (* Defaults:
            let _validationResult = defaultArg validationResult null
    *)
    -> CardContentContext
#### Параметры
contentSource
[ICardFileContentSource](T_Tessa_Cards_ICardFileContentSource.htm)
    Информация по источнику контента для файла.
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
(Optional)
     Объект, выполняющий построение результата валидации, или null, если создаётся новый экземпляр объекта. 
## __См. также
#### Ссылки
[CardContentContext - ](T_Tessa_Cards_ComponentModel_CardContentContext.htm)
[CardContentContext -
перегрузка](Overload_Tessa_Cards_ComponentModel_CardContentContext__ctor.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
