# ApplicationPackageBuilderExtender.Merge(IApplicationPackageBuilderContext,
Func<IPackageBinderFactory, IApplicationPackageBinder>) - метод
Создает контекст построителя пакета приложения содержащий объединение между
пакетом содержащимся в построителе и пакетом mergePackageFunc
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    public static IApplicationPackageBuilderContext Merge(
    	[NotNullAttribute] this IApplicationPackageBuilderContext context,
    	[NotNullAttribute] Func<IPackageBinderFactory, IApplicationPackageBinder> mergePackageFunc
    )
VB __Копировать
    <ExtensionAttribute>
    <NotNullAttribute>
    Public Shared Function Merge ( 
    	<NotNullAttribute> context As IApplicationPackageBuilderContext,
    	<NotNullAttribute> mergePackageFunc As Func(Of IPackageBinderFactory, IApplicationPackageBinder)
    ) As IApplicationPackageBuilderContext
C++ __Копировать
     public:
    [ExtensionAttribute]
    [NotNullAttribute]
    static IApplicationPackageBuilderContext^ Merge(
    	[NotNullAttribute] IApplicationPackageBuilderContext^ context, 
    	[NotNullAttribute] Func<IPackageBinderFactory^, IApplicationPackageBinder^>^ mergePackageFunc
    )
F# __Копировать
     [<ExtensionAttribute>]
    [<NotNullAttribute>]
    static member Merge : 
            [<NotNullAttribute>] context : IApplicationPackageBuilderContext * 
            [<NotNullAttribute>] mergePackageFunc : Func<IPackageBinderFactory, IApplicationPackageBinder> -> IApplicationPackageBuilderContext 
#### Параметры
context
[IApplicationPackageBuilderContext](T_Tessa_Applications_Package_IApplicationPackageBuilderContext.htm)
     Контекст построителя пакета приложения 
mergePackageFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[IPackageBinderFactory](T_Tessa_Applications_Package_IPackageBinderFactory.htm),
[IApplicationPackageBinder](T_Tessa_Applications_Package_IApplicationPackageBinder.htm)>
     Функция формирования пакета обновления 
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
[Merge -
перегрузка](Overload_Tessa_Applications_Package_ApplicationPackageBuilderExtender_Merge.htm)
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
