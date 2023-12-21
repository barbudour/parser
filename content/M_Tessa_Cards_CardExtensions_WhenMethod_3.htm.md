# CardExtensions.WhenMethod(IExtensionPolicyContainer, CardGetMethod[]) -
метод
Регистрирует политику фильтрации выполнения методов расширений по списку
допустимых методов загрузки карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IExtensionPolicyContainer WhenMethod(
    	this IExtensionPolicyContainer policyContainer,
    	params CardGetMethod[] methods
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function WhenMethod ( 
    	policyContainer As IExtensionPolicyContainer,
    	ParamArray methods As CardGetMethod()
    ) As IExtensionPolicyContainer
C++ __Копировать
     public:
    [ExtensionAttribute]
    static IExtensionPolicyContainer^ WhenMethod(
    	IExtensionPolicyContainer^ policyContainer, 
    	... array<CardGetMethod>^ methods
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member WhenMethod : 
            policyContainer : IExtensionPolicyContainer * 
            methods : CardGetMethod[] -> IExtensionPolicyContainer 
#### Параметры
policyContainer
[IExtensionPolicyContainer](T_Tessa_Extensions_IExtensionPolicyContainer.htm)
    Контейнер политик, ассоциированных с расширениями.
methods [CardGetMethod](T_Tessa_Cards_CardGetMethod.htm)[]
    Список допустимых методов выполнения запроса к API карточек.
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
[WhenMethod - перегрузка](Overload_Tessa_Cards_CardExtensions_WhenMethod.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
