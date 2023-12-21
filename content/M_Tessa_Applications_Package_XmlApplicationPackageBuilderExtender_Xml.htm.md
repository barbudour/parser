# XmlApplicationPackageBuilderExtender.Xml - метод
Создает объект осуществляющий формирование пакета приложения из xml
## __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    public static XmlPackageBinder Xml(
    	[NotNullAttribute] this IPackageBinderFactory binderFactory
    )
VB __Копировать
    <ExtensionAttribute>
    <NotNullAttribute>
    Public Shared Function Xml ( 
    	<NotNullAttribute> binderFactory As IPackageBinderFactory
    ) As XmlPackageBinder
C++ __Копировать
     public:
    [ExtensionAttribute]
    [NotNullAttribute]
    static XmlPackageBinder^ Xml(
    	[NotNullAttribute] IPackageBinderFactory^ binderFactory
    )
F# __Копировать
     [<ExtensionAttribute>]
    [<NotNullAttribute>]
    static member Xml : 
            [<NotNullAttribute>] binderFactory : IPackageBinderFactory -> XmlPackageBinder 
#### Параметры
binderFactory
[IPackageBinderFactory](T_Tessa_Applications_Package_IPackageBinderFactory.htm)
     Фабрика создания объекта формирования пакета приложения 
#### Возвращаемое значение
[XmlPackageBinder](T_Tessa_Applications_Package_XmlPackageBinder.htm)  
Объект осуществляющий формирование пакета приложения
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[IPackageBinderFactory](T_Tessa_Applications_Package_IPackageBinderFactory.htm).
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[XmlApplicationPackageBuilderExtender -
](T_Tessa_Applications_Package_XmlApplicationPackageBuilderExtender.htm)
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
