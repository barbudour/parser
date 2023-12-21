# AssemblyApplicationPackageBinder.Source(Func<Assembly>) - метод
Устанавливает в качестве источника функцию assemblyFunc возвращающую сборку
приложения
## __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    public AssemblyApplicationPackageBinder Source(
    	[NotNullAttribute] Func<Assembly> assemblyFunc
    )
VB __Копировать
    <NotNullAttribute>
    Public Function Source ( 
    	<NotNullAttribute> assemblyFunc As Func(Of Assembly)
    ) As AssemblyApplicationPackageBinder
C++ __Копировать
     public:
    [NotNullAttribute]
    AssemblyApplicationPackageBinder^ Source(
    	[NotNullAttribute] Func<Assembly^>^ assemblyFunc
    )
F# __Копировать
     [<NotNullAttribute>]
    member Source : 
            [<NotNullAttribute>] assemblyFunc : Func<Assembly> -> AssemblyApplicationPackageBinder 
#### Параметры
assemblyFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[Assembly](https://learn.microsoft.com/dotnet/api/system.reflection.assembly)>
     Функция возвращающая сборку приложения 
#### Возвращаемое значение
[AssemblyApplicationPackageBinder](T_Tessa_Applications_Package_AssemblyApplicationPackageBinder.htm)  
Ссылку на себя
## __См. также
#### Ссылки
[AssemblyApplicationPackageBinder -
](T_Tessa_Applications_Package_AssemblyApplicationPackageBinder.htm)
[Source -
перегрузка](Overload_Tessa_Applications_Package_AssemblyApplicationPackageBinder_Source.htm)
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
