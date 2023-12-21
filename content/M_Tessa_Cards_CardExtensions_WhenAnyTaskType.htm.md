# CardExtensions.WhenAnyTaskType - метод
Регистрирует политику фильтрации выполнения методов расширений по любым типам
заданий. Используйте для замещения политики, назначенной посредством методов
[WhenTaskTypes(IExtensionPolicyContainer,
String[])](M_Tessa_Cards_CardExtensions_WhenTaskTypes_1.htm) и
[WhenTaskTypes(IExtensionPolicyContainer,
Guid[])](M_Tessa_Cards_CardExtensions_WhenTaskTypes.htm). Если идентификатор и
имя типа задания неизвестны, то метод расширения выполняется. Для того, чтобы
политика использовалась, требуется зарегистрировать политику
[CardTaskTypeFilterPolicy](T_Tessa_Cards_Extensions_CardTaskTypeFilterPolicy.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IExtensionPolicyContainer WhenAnyTaskType(
    	this IExtensionPolicyContainer policyContainer
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function WhenAnyTaskType ( 
    	policyContainer As IExtensionPolicyContainer
    ) As IExtensionPolicyContainer
C++ __Копировать
     public:
    [ExtensionAttribute]
    static IExtensionPolicyContainer^ WhenAnyTaskType(
    	IExtensionPolicyContainer^ policyContainer
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member WhenAnyTaskType : 
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
