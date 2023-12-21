# ApplicationPackageBuilderExtender.ViewRow - метод
Создает объект осуществляющий формирование пакета приложения из строки
представления
## __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    public static ViewRowApplicationPackageBinder ViewRow(
    	[NotNullAttribute] this IPackageBinderFactory binderFactory
    )
VB __Копировать
    <ExtensionAttribute>
    <NotNullAttribute>
    Public Shared Function ViewRow ( 
    	<NotNullAttribute> binderFactory As IPackageBinderFactory
    ) As ViewRowApplicationPackageBinder
C++ __Копировать
     public:
    [ExtensionAttribute]
    [NotNullAttribute]
    static ViewRowApplicationPackageBinder^ ViewRow(
    	[NotNullAttribute] IPackageBinderFactory^ binderFactory
    )
F# __Копировать
     [<ExtensionAttribute>]
    [<NotNullAttribute>]
    static member ViewRow : 
            [<NotNullAttribute>] binderFactory : IPackageBinderFactory -> ViewRowApplicationPackageBinder 
#### Параметры
binderFactory
[IPackageBinderFactory](T_Tessa_Applications_Package_IPackageBinderFactory.htm)
     Фабрика создания объекта формирования пакета приложения 
#### Возвращаемое значение
[ViewRowApplicationPackageBinder](T_Tessa_Applications_Package_ViewRowApplicationPackageBinder.htm)  
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
