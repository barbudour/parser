# FileConverterExtensions.WhenAnyFileConverterEventName - метод
Регистрирует политику фильтрации выполнения методов расширений по любым именам
событий конвертирования файлов. Используйте для замещения политики,
назначенной посредством метода
[WhenFileConverterEventNames(IExtensionPolicyContainer,
String[])](M_Tessa_FileConverters_FileConverterExtensions_WhenFileConverterEventNames.htm).
Для того, чтобы политика использовалась, требуется зарегистрировать политику
[FileConverterExtensionFilterPolicy](T_Tessa_FileConverters_FileConverterExtensionFilterPolicy.htm).
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IExtensionPolicyContainer WhenAnyFileConverterEventName(
    	this IExtensionPolicyContainer policyContainer
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function WhenAnyFileConverterEventName ( 
    	policyContainer As IExtensionPolicyContainer
    ) As IExtensionPolicyContainer
C++ __Копировать
     public:
    [ExtensionAttribute]
    static IExtensionPolicyContainer^ WhenAnyFileConverterEventName(
    	IExtensionPolicyContainer^ policyContainer
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member WhenAnyFileConverterEventName : 
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
[FileConverterExtensions -
](T_Tessa_FileConverters_FileConverterExtensions.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
