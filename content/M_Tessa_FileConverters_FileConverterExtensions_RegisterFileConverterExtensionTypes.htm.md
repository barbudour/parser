# FileConverterExtensions.RegisterFileConverterExtensionTypes - метод
Выполняет регистрацию стандартных типов расширений для конвертеров файлов.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IExtensionContainer RegisterFileConverterExtensionTypes(
    	this IExtensionContainer container
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function RegisterFileConverterExtensionTypes ( 
    	container As IExtensionContainer
    ) As IExtensionContainer
C++ __Копировать
     public:
    [ExtensionAttribute]
    static IExtensionContainer^ RegisterFileConverterExtensionTypes(
    	IExtensionContainer^ container
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member RegisterFileConverterExtensionTypes : 
            container : IExtensionContainer -> IExtensionContainer 
#### Параметры
container [IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm)
    Контейнер, в котором регистрируются расширения.
#### Возвращаемое значение
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm)  
Заданный контейнер container для цепочки вызовов.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm). При вызове
метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
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
