# CardExtensions.WhenFileTypes(IExtensionPolicyContainer, String[]) - метод
Регистрирует политику фильтрации выполнения методов расширений по имени типа
файла, которое входит в заданный список имён. Если тип файла неизвестен, то
метод расширения не выполняется. Для того, чтобы политика использовалась,
требуется зарегистрировать политику
[CardFileTypeFilterPolicy](T_Tessa_Cards_Extensions_CardFileTypeFilterPolicy.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IExtensionPolicyContainer WhenFileTypes(
    	this IExtensionPolicyContainer policyContainer,
    	params string[] fileTypeNames
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function WhenFileTypes ( 
    	policyContainer As IExtensionPolicyContainer,
    	ParamArray fileTypeNames As String()
    ) As IExtensionPolicyContainer
C++ __Копировать
     public:
    [ExtensionAttribute]
    static IExtensionPolicyContainer^ WhenFileTypes(
    	IExtensionPolicyContainer^ policyContainer, 
    	... array<String^>^ fileTypeNames
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member WhenFileTypes : 
            policyContainer : IExtensionPolicyContainer * 
            fileTypeNames : string[] -> IExtensionPolicyContainer 
#### Параметры
policyContainer
[IExtensionPolicyContainer](T_Tessa_Extensions_IExtensionPolicyContainer.htm)
    Контейнер политик, ассоциированных с расширениями.
fileTypeNames [String](https://learn.microsoft.com/dotnet/api/system.string)[]
     Список имён типов файлов, в который должно входить имя типа файла, для которого выполняется метод расширения. Список не должен содержать значений null. 
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
[WhenFileTypes -
перегрузка](Overload_Tessa_Cards_CardExtensions_WhenFileTypes.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
