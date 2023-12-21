# IApplicationPackageBuilderContext - интерфейс
Контекст построителя пакета приложения
## __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IApplicationPackageBuilderContext
VB __Копировать
     Public Interface IApplicationPackageBuilderContext
C++ __Копировать
     public interface class IApplicationPackageBuilderContext
F# __Копировать
     type IApplicationPackageBuilderContext = interface end
##  __Свойства
[BinderFactory](P_Tessa_Applications_Package_IApplicationPackageBuilderContext_BinderFactory.htm)|
Gets Фабрика создания объекта осуществляющего сопоставление пакета приложения
источнику  
---|---  
[ValidationResultBuilder](P_Tessa_Applications_Package_IApplicationPackageBuilderContext_ValidationResultBuilder.htm)|
Gets Построитель результатов валидации  
## __Методы
[BuildAsync](M_Tessa_Applications_Package_IApplicationPackageBuilderContext_BuildAsync.htm)|
Осуществляет построение пакета приложения  
---|---  
## __Методы расширения
[Diff](M_Tessa_Applications_Package_ApplicationPackageBuilderExtender_Diff.htm)|
Создает контекст построителя пакета приложения содержащий разницу между
пакетом содержащимся в построителе и пакетом updatePackageFunc  
(Определяется
[ApplicationPackageBuilderExtender](T_Tessa_Applications_Package_ApplicationPackageBuilderExtender.htm))  
---|---  
[MakeDiff](M_Tessa_Applications_Package_ApplicationPackageBuilderExtender_MakeDiff_1.htm)|
Создает контекст построителя пакета приложения содержащий разницу между
пакетом содержащимся в построителе и пакетом updatePackage  
(Определяется
[ApplicationPackageBuilderExtender](T_Tessa_Applications_Package_ApplicationPackageBuilderExtender.htm))  
[MakeDiff](M_Tessa_Applications_Package_ApplicationPackageBuilderExtender_MakeDiff.htm)|
Создает контекст построителя пакета приложения содержащий разницу между
пакетом содержащимся в построителе и пакетом updatePackageFunc  
(Определяется
[ApplicationPackageBuilderExtender](T_Tessa_Applications_Package_ApplicationPackageBuilderExtender.htm))  
[Merge](M_Tessa_Applications_Package_ApplicationPackageBuilderExtender_Merge_1.htm)|
Создает контекст построителя пакета приложения содержащий объединение пакетов
содержащимся в построителе и пакетом mergePackage  
(Определяется
[ApplicationPackageBuilderExtender](T_Tessa_Applications_Package_ApplicationPackageBuilderExtender.htm))  
[Merge](M_Tessa_Applications_Package_ApplicationPackageBuilderExtender_Merge.htm)|
Создает контекст построителя пакета приложения содержащий объединение между
пакетом содержащимся в построителе и пакетом mergePackageFunc  
(Определяется
[ApplicationPackageBuilderExtender](T_Tessa_Applications_Package_ApplicationPackageBuilderExtender.htm))  
##  __См. также
#### Ссылки
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
