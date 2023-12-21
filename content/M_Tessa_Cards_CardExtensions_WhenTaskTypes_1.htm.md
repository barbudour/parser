# CardExtensions.WhenTaskTypes(IExtensionPolicyContainer, String[]) - метод
Регистрирует политику фильтрации выполнения методов расширений по имени типа
задания, которое входит в заданный список имён. Если тип задания неизвестен,
то метод расширения не выполняется. Для того, чтобы политика использовалась,
требуется зарегистрировать политику
[CardTaskTypeFilterPolicy](T_Tessa_Cards_Extensions_CardTaskTypeFilterPolicy.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IExtensionPolicyContainer WhenTaskTypes(
    	this IExtensionPolicyContainer policyContainer,
    	params string[] taskTypeNames
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function WhenTaskTypes ( 
    	policyContainer As IExtensionPolicyContainer,
    	ParamArray taskTypeNames As String()
    ) As IExtensionPolicyContainer
C++ __Копировать
     public:
    [ExtensionAttribute]
    static IExtensionPolicyContainer^ WhenTaskTypes(
    	IExtensionPolicyContainer^ policyContainer, 
    	... array<String^>^ taskTypeNames
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member WhenTaskTypes : 
            policyContainer : IExtensionPolicyContainer * 
            taskTypeNames : string[] -> IExtensionPolicyContainer 
#### Параметры
policyContainer
[IExtensionPolicyContainer](T_Tessa_Extensions_IExtensionPolicyContainer.htm)
    Контейнер политик, ассоциированных с расширениями.
taskTypeNames [String](https://learn.microsoft.com/dotnet/api/system.string)[]
     Список имён типов заданий, в который должно входить имя типа задания, для которого выполняется метод расширения. Список не должен содержать значений null. 
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
[WhenTaskTypes -
перегрузка](Overload_Tessa_Cards_CardExtensions_WhenTaskTypes.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
