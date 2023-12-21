# CardValidationExtensions.RegisterDefaults - метод
Выполняет регистрацию валидаторов карточки, предоставляемых платформой, в
реестре валидаторов карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void RegisterDefaults(
    	this ICardValidatorRegistry registry
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub RegisterDefaults ( 
    	registry As ICardValidatorRegistry
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void RegisterDefaults(
    	ICardValidatorRegistry^ registry
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member RegisterDefaults : 
            registry : ICardValidatorRegistry -> unit 
#### Параметры
registry
[ICardValidatorRegistry](T_Tessa_Cards_Validation_ICardValidatorRegistry.htm)
    Реестр валидаторов карточки.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[ICardValidatorRegistry](T_Tessa_Cards_Validation_ICardValidatorRegistry.htm).
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardValidationExtensions -
](T_Tessa_Cards_Validation_CardValidationExtensions.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
