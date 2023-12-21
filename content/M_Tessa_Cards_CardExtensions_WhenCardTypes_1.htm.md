# CardExtensions.WhenCardTypes(IExtensionPolicyContainer, String[]) - метод
Регистрирует политику фильтрации выполнения методов расширений по имени типа
карточки, которое входит в заданный список имён. Если тип карточки неизвестен,
то метод расширения не выполняется. Для того, чтобы политика использовалась,
требуется зарегистрировать политику
[CardTypeFilterPolicy](T_Tessa_Cards_Extensions_CardTypeFilterPolicy.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IExtensionPolicyContainer WhenCardTypes(
    	this IExtensionPolicyContainer policyContainer,
    	params string[] cardTypeNames
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function WhenCardTypes ( 
    	policyContainer As IExtensionPolicyContainer,
    	ParamArray cardTypeNames As String()
    ) As IExtensionPolicyContainer
C++ __Копировать
     public:
    [ExtensionAttribute]
    static IExtensionPolicyContainer^ WhenCardTypes(
    	IExtensionPolicyContainer^ policyContainer, 
    	... array<String^>^ cardTypeNames
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member WhenCardTypes : 
            policyContainer : IExtensionPolicyContainer * 
            cardTypeNames : string[] -> IExtensionPolicyContainer 
#### Параметры
policyContainer
[IExtensionPolicyContainer](T_Tessa_Extensions_IExtensionPolicyContainer.htm)
    Контейнер политик, ассоциированных с расширениями.
cardTypeNames [String](https://learn.microsoft.com/dotnet/api/system.string)[]
     Список имён типов карточек, в который должно входить имя типа карточки, для которого выполняется метод расширения. Список не должен содержать значений null. 
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
[WhenCardTypes -
перегрузка](Overload_Tessa_Cards_CardExtensions_WhenCardTypes.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
