# DiffPackageBuilderContext - конструктор
Initializes a new instance of the
[DiffPackageBuilderContext](T_Tessa_Applications_Package_DiffPackageBuilderContext.htm)
class. Initializes a new instance of the
[UpdatePackageBuilderContext](T_Tessa_Applications_Package_UpdatePackageBuilderContext.htm)
class. Инициализирует новый экземпляр класса
[Object](https://learn.microsoft.com/dotnet/api/system.object).
## __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public DiffPackageBuilderContext(
    	[CanBeNullAttribute] IApplicationPackageBuilderContext sourceContext,
    	[NotNullAttribute] Func<IPackageBinderFactory, IApplicationPackageBinder> packageUpdateFunc
    )
VB __Копировать
     Public Sub New ( 
    	<CanBeNullAttribute> sourceContext As IApplicationPackageBuilderContext,
    	<NotNullAttribute> packageUpdateFunc As Func(Of IPackageBinderFactory, IApplicationPackageBinder)
    )
C++ __Копировать
     public:
    DiffPackageBuilderContext(
    	[CanBeNullAttribute] IApplicationPackageBuilderContext^ sourceContext, 
    	[NotNullAttribute] Func<IPackageBinderFactory^, IApplicationPackageBinder^>^ packageUpdateFunc
    )
F# __Копировать
     new : 
            [<CanBeNullAttribute>] sourceContext : IApplicationPackageBuilderContext * 
            [<NotNullAttribute>] packageUpdateFunc : Func<IPackageBinderFactory, IApplicationPackageBinder> -> DiffPackageBuilderContext
#### Параметры
sourceContext
[IApplicationPackageBuilderContext](T_Tessa_Applications_Package_IApplicationPackageBuilderContext.htm)
     Контекст содержащий исходный пакет приложения 
packageUpdateFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[IPackageBinderFactory](T_Tessa_Applications_Package_IPackageBinderFactory.htm),
[IApplicationPackageBinder](T_Tessa_Applications_Package_IApplicationPackageBinder.htm)>
     Пакет приложения содержащий текущий пакет 
## __См. также
#### Ссылки
[DiffPackageBuilderContext -
](T_Tessa_Applications_Package_DiffPackageBuilderContext.htm)
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
