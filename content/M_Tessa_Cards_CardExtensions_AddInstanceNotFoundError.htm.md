# CardExtensions.AddInstanceNotFoundError - метод
Добавляет ошибку валидации
[InstanceNotFound](F_Tessa_Cards_CardValidationKeys_InstanceNotFound.htm) с
информацией по стеку вызовов, если это разрешено флагами flags.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IValidationResultBuilder AddInstanceNotFoundError(
    	this IValidationResultBuilder validationResult,
    	Object thisObject,
    	ConfigurationFlags flags,
    	Object objectIdentity
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function AddInstanceNotFoundError ( 
    	validationResult As IValidationResultBuilder,
    	thisObject As Object,
    	flags As ConfigurationFlags,
    	objectIdentity As Object
    ) As IValidationResultBuilder
C++ __Копировать
     public:
    [ExtensionAttribute]
    static IValidationResultBuilder^ AddInstanceNotFoundError(
    	IValidationResultBuilder^ validationResult, 
    	Object^ thisObject, 
    	ConfigurationFlags flags, 
    	Object^ objectIdentity
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member AddInstanceNotFoundError : 
            validationResult : IValidationResultBuilder * 
            thisObject : Object * 
            flags : ConfigurationFlags * 
            objectIdentity : Object -> IValidationResultBuilder 
#### Параметры
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
    Объект, в который добавляется сообщение.
thisObject [Object](https://learn.microsoft.com/dotnet/api/system.object)
     Текущий объект this, например, экземпляр класса расширения. Можно также передать тип объекта (например, typeof(MyHelperClass)), строку с именем объекта или null, если имя останется неизвестным. 
flags [ConfigurationFlags](T_Tessa_Platform_Runtime_ConfigurationFlags.htm)
    Режимы конфигурации.
objectIdentity [Object](https://learn.microsoft.com/dotnet/api/system.object)
    Идентифицирующая не найденный объект информация (идентификатор карточки, имя и т.п.).
#### Возвращаемое значение
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)  
Объект validationResult для цепочки вызовов.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm).
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardExtensions - ](T_Tessa_Cards_CardExtensions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
