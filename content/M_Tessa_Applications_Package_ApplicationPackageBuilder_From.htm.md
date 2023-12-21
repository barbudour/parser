# ApplicationPackageBuilder.From - метод
Создает пакет приложения с помощью метода binderFactory
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    public IApplicationPackageBuilderContext From(
    	[NotNullAttribute] Func<IPackageBinderFactory, IApplicationPackageBinder> binderFactory
    )
VB __Копировать
    <NotNullAttribute>
    Public Function From ( 
    	<NotNullAttribute> binderFactory As Func(Of IPackageBinderFactory, IApplicationPackageBinder)
    ) As IApplicationPackageBuilderContext
C++ __Копировать
     public:
    [NotNullAttribute]
    IApplicationPackageBuilderContext^ From(
    	[NotNullAttribute] Func<IPackageBinderFactory^, IApplicationPackageBinder^>^ binderFactory
    )
F# __Копировать
     [<NotNullAttribute>]
    member From : 
            [<NotNullAttribute>] binderFactory : Func<IPackageBinderFactory, IApplicationPackageBinder> -> IApplicationPackageBuilderContext 
#### Параметры
binderFactory
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[IPackageBinderFactory](T_Tessa_Applications_Package_IPackageBinderFactory.htm),
[IApplicationPackageBinder](T_Tessa_Applications_Package_IApplicationPackageBinder.htm)>
     Фабрика формирования пакета приложения 
#### Возвращаемое значение
[IApplicationPackageBuilderContext](T_Tessa_Applications_Package_IApplicationPackageBuilderContext.htm)  
Пакет приложения
## __См. также
#### Ссылки
[ApplicationPackageBuilder -
](T_Tessa_Applications_Package_ApplicationPackageBuilder.htm)
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
