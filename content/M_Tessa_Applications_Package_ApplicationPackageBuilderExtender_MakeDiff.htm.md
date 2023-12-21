#
ApplicationPackageBuilderExtender.MakeDiff(IApplicationPackageBuilderContext,
Func<IPackageBinderFactory, IApplicationPackageBinder>, Boolean) - метод
Создает контекст построителя пакета приложения содержащий разницу между
пакетом содержащимся в построителе и пакетом updatePackageFunc
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    public static IApplicationPackageBuilderContext MakeDiff(
    	[NotNullAttribute] this IApplicationPackageBuilderContext context,
    	[NotNullAttribute] Func<IPackageBinderFactory, IApplicationPackageBinder> updatePackageFunc,
    	bool withOldFileId = false
    )
VB __Копировать
    <ExtensionAttribute>
    <NotNullAttribute>
    Public Shared Function MakeDiff ( 
    	<NotNullAttribute> context As IApplicationPackageBuilderContext,
    	<NotNullAttribute> updatePackageFunc As Func(Of IPackageBinderFactory, IApplicationPackageBinder),
    	Optional withOldFileId As Boolean = false
    ) As IApplicationPackageBuilderContext
C++ __Копировать
     public:
    [ExtensionAttribute]
    [NotNullAttribute]
    static IApplicationPackageBuilderContext^ MakeDiff(
    	[NotNullAttribute] IApplicationPackageBuilderContext^ context, 
    	[NotNullAttribute] Func<IPackageBinderFactory^, IApplicationPackageBinder^>^ updatePackageFunc, 
    	bool withOldFileId = false
    )
F# __Копировать
     [<ExtensionAttribute>]
    [<NotNullAttribute>]
    static member MakeDiff : 
            [<NotNullAttribute>] context : IApplicationPackageBuilderContext * 
            [<NotNullAttribute>] updatePackageFunc : Func<IPackageBinderFactory, IApplicationPackageBinder> * 
            ?withOldFileId : bool 
    (* Defaults:
            let _withOldFileId = defaultArg withOldFileId false
    *)
    -> IApplicationPackageBuilderContext 
#### Параметры
context
[IApplicationPackageBuilderContext](T_Tessa_Applications_Package_IApplicationPackageBuilderContext.htm)
     Контекст построителя пакета приложения 
updatePackageFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[IPackageBinderFactory](T_Tessa_Applications_Package_IPackageBinderFactory.htm),
[IApplicationPackageBinder](T_Tessa_Applications_Package_IApplicationPackageBinder.htm)>
     Функция формирования пакета обновления 
withOldFileId [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
    Признак копирования исходных идентификаторов файлов в новый пакет
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
