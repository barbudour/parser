# ApplicationPackageBuilderExtender - класс
Методы расширения для построителя пакета приложения
## __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class ApplicationPackageBuilderExtender
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class ApplicationPackageBuilderExtender
C++ __Копировать
    [ExtensionAttribute]
    public ref class ApplicationPackageBuilderExtender abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type ApplicationPackageBuilderExtender = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ApplicationPackageBuilderExtender
##  __Методы
[Diff](M_Tessa_Applications_Package_ApplicationPackageBuilderExtender_Diff.htm)|
Создает контекст построителя пакета приложения содержащий разницу между
пакетом содержащимся в построителе и пакетом updatePackageFunc  
---|---  
[FromAssembly](M_Tessa_Applications_Package_ApplicationPackageBuilderExtender_FromAssembly.htm)|
Создает объект осуществляющий формирование пакета приложения из сборки
приложения  
[FromCard](M_Tessa_Applications_Package_ApplicationPackageBuilderExtender_FromCard.htm)|
Создает объект осуществляющий формирование пакета приложения из строки
представления  
[FromDatabase](M_Tessa_Applications_Package_ApplicationPackageBuilderExtender_FromDatabase.htm)|
Создает объект осуществляющий формирование пакета приложения из базы данных  
[FromPackage](M_Tessa_Applications_Package_ApplicationPackageBuilderExtender_FromPackage.htm)|
Создает объект осуществляющий формирование пакета приложения из существующего
пакета приложения  
[FromRequest](M_Tessa_Applications_Package_ApplicationPackageBuilderExtender_FromRequest.htm)|
Создает объект осуществляющий формирование пакета приложения из запроса к
сервису представлений  
[GetTotalBytes(ApplicationPackage)](M_Tessa_Applications_Package_ApplicationPackageBuilderExtender_GetTotalBytes_1.htm)|
Подсчитывает размер файлов в пакете приложения  
[GetTotalBytes(IList<ApplicationPackageFile>)](M_Tessa_Applications_Package_ApplicationPackageBuilderExtender_GetTotalBytes.htm)|
Подсчитывает размер файлов в пакете приложения  
[MakeDiff(IApplicationPackageBuilderContext,
ApplicationPackage)](M_Tessa_Applications_Package_ApplicationPackageBuilderExtender_MakeDiff_1.htm)|
Создает контекст построителя пакета приложения содержащий разницу между
пакетом содержащимся в построителе и пакетом updatePackage  
[MakeDiff(IApplicationPackageBuilderContext, Func<IPackageBinderFactory,
IApplicationPackageBinder>,
Boolean)](M_Tessa_Applications_Package_ApplicationPackageBuilderExtender_MakeDiff.htm)|
Создает контекст построителя пакета приложения содержащий разницу между
пакетом содержащимся в построителе и пакетом updatePackageFunc  
[Merge(IApplicationPackageBuilderContext, Func<IPackageBinderFactory,
IApplicationPackageBinder>)](M_Tessa_Applications_Package_ApplicationPackageBuilderExtender_Merge.htm)|
Создает контекст построителя пакета приложения содержащий объединение между
пакетом содержащимся в построителе и пакетом mergePackageFunc  
[Merge(IApplicationPackageBuilderContext,
ApplicationPackage)](M_Tessa_Applications_Package_ApplicationPackageBuilderExtender_Merge_1.htm)|
Создает контекст построителя пакета приложения содержащий объединение пакетов
содержащимся в построителе и пакетом mergePackage  
[ViewRow](M_Tessa_Applications_Package_ApplicationPackageBuilderExtender_ViewRow.htm)|
Создает объект осуществляющий формирование пакета приложения из строки
представления  
## __См. также
#### Ссылки
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
