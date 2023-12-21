# CardExtensions.WhenCardTypes(IExtensionPolicyContainer, Guid[]) - метод
Регистрирует политику фильтрации выполнения методов расширений по
идентификатору типа карточки, который входит в заданный список
идентификаторов. Если тип карточки неизвестен, то метод расширения не
выполняется. Для того, чтобы политика использовалась, требуется
зарегистрировать политику
[CardTypeFilterPolicy](T_Tessa_Cards_Extensions_CardTypeFilterPolicy.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IExtensionPolicyContainer WhenCardTypes(
    	this IExtensionPolicyContainer policyContainer,
    	params Guid[] cardTypeIDs
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function WhenCardTypes ( 
    	policyContainer As IExtensionPolicyContainer,
    	ParamArray cardTypeIDs As Guid()
    ) As IExtensionPolicyContainer
C++ __Копировать
     public:
    [ExtensionAttribute]
    static IExtensionPolicyContainer^ WhenCardTypes(
    	IExtensionPolicyContainer^ policyContainer, 
    	... array<Guid>^ cardTypeIDs
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member WhenCardTypes : 
            policyContainer : IExtensionPolicyContainer * 
            cardTypeIDs : Guid[] -> IExtensionPolicyContainer 
#### Параметры
policyContainer
[IExtensionPolicyContainer](T_Tessa_Extensions_IExtensionPolicyContainer.htm)
    Контейнер политик, ассоциированных с расширениями.
cardTypeIDs [Guid](https://learn.microsoft.com/dotnet/api/system.guid)[]
     Список идентификаторов типов карточек, в который должен входить идентификатор типа карточки, для которого выполняется метод расширения. 
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
