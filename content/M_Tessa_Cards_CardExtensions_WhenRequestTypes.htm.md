# CardExtensions.WhenRequestTypes - метод
Регистрирует политику фильтрации выполнения методов расширений по типу
универсального запроса к сервису карточек, которое входит в заданный список
типов. Тип запроса является обязательным параметром и должен быть известен.
Для того, чтобы политика использовалась, требуется зарегистрировать политику
[CardRequestFilterPolicy](T_Tessa_Cards_Extensions_CardRequestFilterPolicy.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IExtensionPolicyContainer WhenRequestTypes(
    	this IExtensionPolicyContainer policyContainer,
    	params Guid[] requestTypes
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function WhenRequestTypes ( 
    	policyContainer As IExtensionPolicyContainer,
    	ParamArray requestTypes As Guid()
    ) As IExtensionPolicyContainer
C++ __Копировать
     public:
    [ExtensionAttribute]
    static IExtensionPolicyContainer^ WhenRequestTypes(
    	IExtensionPolicyContainer^ policyContainer, 
    	... array<Guid>^ requestTypes
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member WhenRequestTypes : 
            policyContainer : IExtensionPolicyContainer * 
            requestTypes : Guid[] -> IExtensionPolicyContainer 
#### Параметры
policyContainer
[IExtensionPolicyContainer](T_Tessa_Extensions_IExtensionPolicyContainer.htm)
    Контейнер политик, ассоциированных с расширениями.
requestTypes [Guid](https://learn.microsoft.com/dotnet/api/system.guid)[]
     Список типов универсальных запросов к сервису карточек, в который должен входить тип запроса, для которого выполняется метод расширения. Список не должен содержать значений null. 
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
