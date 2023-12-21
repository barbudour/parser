# CardExtensions.WhenAnyCardType - метод
Регистрирует политику фильтрации выполнения методов расширений по любым типам
карточек. Используйте для замещения политики, назначенной посредством методов
[WhenCardTypes(IExtensionPolicyContainer,
String[])](M_Tessa_Cards_CardExtensions_WhenCardTypes_1.htm) и
[WhenCardTypes(IExtensionPolicyContainer,
Guid[])](M_Tessa_Cards_CardExtensions_WhenCardTypes.htm). Если идентификатор и
имя типа карточки неизвестны, то метод расширения не выполняется. Для того,
чтобы политика использовалась, требуется зарегистрировать политику
[CardTypeFilterPolicy](T_Tessa_Cards_Extensions_CardTypeFilterPolicy.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IExtensionPolicyContainer WhenAnyCardType(
    	this IExtensionPolicyContainer policyContainer
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function WhenAnyCardType ( 
    	policyContainer As IExtensionPolicyContainer
    ) As IExtensionPolicyContainer
C++ __Копировать
     public:
    [ExtensionAttribute]
    static IExtensionPolicyContainer^ WhenAnyCardType(
    	IExtensionPolicyContainer^ policyContainer
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member WhenAnyCardType : 
            policyContainer : IExtensionPolicyContainer -> IExtensionPolicyContainer 
#### Параметры
policyContainer
[IExtensionPolicyContainer](T_Tessa_Extensions_IExtensionPolicyContainer.htm)
    Контейнер политик, ассоциированных с расширениями.
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
