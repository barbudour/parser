# ApplicationPackageBuilderExtender.FromPackage - метод
Создает объект осуществляющий формирование пакета приложения из существующего
пакета приложения
## __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    public static ApplicationPackageBinder FromPackage(
    	[NotNullAttribute] this IPackageBinderFactory binderFactory,
    	[NotNullAttribute] ApplicationPackage package
    )
VB __Копировать
    <ExtensionAttribute>
    <NotNullAttribute>
    Public Shared Function FromPackage ( 
    	<NotNullAttribute> binderFactory As IPackageBinderFactory,
    	<NotNullAttribute> package As ApplicationPackage
    ) As ApplicationPackageBinder
C++ __Копировать
     public:
    [ExtensionAttribute]
    [NotNullAttribute]
    static ApplicationPackageBinder^ FromPackage(
    	[NotNullAttribute] IPackageBinderFactory^ binderFactory, 
    	[NotNullAttribute] ApplicationPackage^ package
    )
F# __Копировать
     [<ExtensionAttribute>]
    [<NotNullAttribute>]
    static member FromPackage : 
            [<NotNullAttribute>] binderFactory : IPackageBinderFactory * 
            [<NotNullAttribute>] package : ApplicationPackage -> ApplicationPackageBinder 
#### Параметры
binderFactory
[IPackageBinderFactory](T_Tessa_Applications_Package_IPackageBinderFactory.htm)
     Фабрика создания объекта формирования пакета приложения 
package
[ApplicationPackage](T_Tessa_Applications_Package_ApplicationPackage.htm)
     Существующий пакет приложения 
#### Возвращаемое значение
[ApplicationPackageBinder](T_Tessa_Applications_Package_ApplicationPackageBinder.htm)  
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
[ApplicationPackageBuilderExtender -
](T_Tessa_Applications_Package_ApplicationPackageBuilderExtender.htm)
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
