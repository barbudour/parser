# FileConverterExtensions.WhenFileConverterEventNames - метод
Регистрирует политику фильтрации выполнения методов расширений по имени
события конвертирования файлов, которое входит в заданный список имён. Для
того, чтобы политика использовалась, требуется зарегистрировать политику
[FileConverterExtensionFilterPolicy](T_Tessa_FileConverters_FileConverterExtensionFilterPolicy.htm).
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IExtensionPolicyContainer WhenFileConverterEventNames(
    	this IExtensionPolicyContainer policyContainer,
    	params string[] eventNames
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function WhenFileConverterEventNames ( 
    	policyContainer As IExtensionPolicyContainer,
    	ParamArray eventNames As String()
    ) As IExtensionPolicyContainer
C++ __Копировать
     public:
    [ExtensionAttribute]
    static IExtensionPolicyContainer^ WhenFileConverterEventNames(
    	IExtensionPolicyContainer^ policyContainer, 
    	... array<String^>^ eventNames
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member WhenFileConverterEventNames : 
            policyContainer : IExtensionPolicyContainer * 
            eventNames : string[] -> IExtensionPolicyContainer 
#### Параметры
policyContainer
[IExtensionPolicyContainer](T_Tessa_Extensions_IExtensionPolicyContainer.htm)
    Контейнер политик, ассоциированных с расширениями.
eventNames [String](https://learn.microsoft.com/dotnet/api/system.string)[]
     Список имён событий конвертирования файлов, в который должно входить имя события, для которого выполняется метод расширения. 
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
[FileConverterExtensions -
](T_Tessa_FileConverters_FileConverterExtensions.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
