# ApplicationPackageBuilderExtender.FromDatabase - метод
Создает объект осуществляющий формирование пакета приложения из базы данных
## __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    public static DatabasePackageBinder FromDatabase(
    	[NotNullAttribute] this IPackageBinderFactory binderFactory
    )
VB __Копировать
    <ExtensionAttribute>
    <NotNullAttribute>
    Public Shared Function FromDatabase ( 
    	<NotNullAttribute> binderFactory As IPackageBinderFactory
    ) As DatabasePackageBinder
C++ __Копировать
     public:
    [ExtensionAttribute]
    [NotNullAttribute]
    static DatabasePackageBinder^ FromDatabase(
    	[NotNullAttribute] IPackageBinderFactory^ binderFactory
    )
F# __Копировать
     [<ExtensionAttribute>]
    [<NotNullAttribute>]
    static member FromDatabase : 
            [<NotNullAttribute>] binderFactory : IPackageBinderFactory -> DatabasePackageBinder 
#### Параметры
binderFactory
[IPackageBinderFactory](T_Tessa_Applications_Package_IPackageBinderFactory.htm)
     Фабрика создания объекта формирования пакета приложения 
#### Возвращаемое значение
[DatabasePackageBinder](T_Tessa_Applications_Package_DatabasePackageBinder.htm)  
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
