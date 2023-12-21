#
ApplicationPackageBuilderExtender.MakeDiff(IApplicationPackageBuilderContext,
ApplicationPackage) - метод
Создает контекст построителя пакета приложения содержащий разницу между
пакетом содержащимся в построителе и пакетом updatePackage
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    public static IApplicationPackageBuilderContext MakeDiff(
    	[NotNullAttribute] this IApplicationPackageBuilderContext context,
    	[NotNullAttribute] ApplicationPackage updatePackage
    )
VB __Копировать
    <ExtensionAttribute>
    <NotNullAttribute>
    Public Shared Function MakeDiff ( 
    	<NotNullAttribute> context As IApplicationPackageBuilderContext,
    	<NotNullAttribute> updatePackage As ApplicationPackage
    ) As IApplicationPackageBuilderContext
C++ __Копировать
     public:
    [ExtensionAttribute]
    [NotNullAttribute]
    static IApplicationPackageBuilderContext^ MakeDiff(
    	[NotNullAttribute] IApplicationPackageBuilderContext^ context, 
    	[NotNullAttribute] ApplicationPackage^ updatePackage
    )
F# __Копировать
     [<ExtensionAttribute>]
    [<NotNullAttribute>]
    static member MakeDiff : 
            [<NotNullAttribute>] context : IApplicationPackageBuilderContext * 
            [<NotNullAttribute>] updatePackage : ApplicationPackage -> IApplicationPackageBuilderContext 
#### Параметры
context
[IApplicationPackageBuilderContext](T_Tessa_Applications_Package_IApplicationPackageBuilderContext.htm)
     Контекст построителя пакета приложения 
updatePackage
[ApplicationPackage](T_Tessa_Applications_Package_ApplicationPackage.htm)
     Пакет содержащий обновленную версию приложения 
#### Возвращаемое значение
[IApplicationPackageBuilderContext](T_Tessa_Applications_Package_IApplicationPackageBuilderContext.htm)  
Ссылка на контекст построителя пакета приложения
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[IApplicationPackageBuilderContext](T_Tessa_Applications_Package_IApplicationPackageBuilderContext.htm).
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
[MakeDiff -
перегрузка](Overload_Tessa_Applications_Package_ApplicationPackageBuilderExtender_MakeDiff.htm)
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
