# CardExtensions.WhenCardGetFunc - метод
Регистрирует политику фильтрации выполнения методов расширений
[ICardGetExtension](T_Tessa_Cards_Extensions_ICardGetExtension.htm) в
соответствии с функцией isAllowedFunc, которая проверяет контекст расширений.
Если зарегистрировано несколько политик, то должны выполняться все из них.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IExtensionPolicyContainer WhenCardGetFunc(
    	this IExtensionPolicyContainer policyContainer,
    	Func<ICardGetExtensionContext, bool> isAllowedFunc
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function WhenCardGetFunc ( 
    	policyContainer As IExtensionPolicyContainer,
    	isAllowedFunc As Func(Of ICardGetExtensionContext, Boolean)
    ) As IExtensionPolicyContainer
C++ __Копировать
     public:
    [ExtensionAttribute]
    static IExtensionPolicyContainer^ WhenCardGetFunc(
    	IExtensionPolicyContainer^ policyContainer, 
    	Func<ICardGetExtensionContext^, bool>^ isAllowedFunc
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member WhenCardGetFunc : 
            policyContainer : IExtensionPolicyContainer * 
            isAllowedFunc : Func<ICardGetExtensionContext, bool> -> IExtensionPolicyContainer 
#### Параметры
policyContainer
[IExtensionPolicyContainer](T_Tessa_Extensions_IExtensionPolicyContainer.htm)
    Контейнер политик, ассоциированных с расширениями.
isAllowedFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[ICardGetExtensionContext](T_Tessa_Cards_Extensions_ICardGetExtensionContext.htm),
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>
     Функция, получающая контекст (не равный null) и возвращающая признак того, что контекст удовлетворяет политике. Параметр не равен null. Исключения логируются в логгере [Extensions](F_Tessa_Platform_TessaLoggers_Extensions.htm), а также добавляются в контекст как сообщение валидации. Расширение, для которого возникло исключение, пропускается. 
#### Возвращаемое значение
[IExtensionPolicyContainer](T_Tessa_Extensions_IExtensionPolicyContainer.htm)  
Заданный контейнер policyContainer для цепочки расширений.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[IExtensionPolicyContainer](T_Tessa_Extensions_IExtensionPolicyContainer.htm).
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
