# IAssemblyLoaderOptions - интерфейс
Настройки, связанные с экспортом метаданных из сборки.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Composition](N_Tessa_Platform_Composition.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IAssemblyLoaderOptions
VB __Копировать
     Public Interface IAssemblyLoaderOptions
C++ __Копировать
     public interface class IAssemblyLoaderOptions
F# __Копировать
     type IAssemblyLoaderOptions = interface end
##  __Свойства
[Flags](P_Tessa_Platform_Composition_IAssemblyLoaderOptions_Flags.htm)| Флаги,
определяющие процесс загрузки сборок при экспорте метаинформации.  
---|---  
[InterfaceTypesToCheck](P_Tessa_Platform_Composition_IAssemblyLoaderOptions_InterfaceTypesToCheck.htm)|
Типы интерфейсов, для которых надо проверить, что экспортируемый тип с
атрибутом их реализует.  
##  __Методы
[CheckInterface<T>](M_Tessa_Platform_Composition_IAssemblyLoaderOptions_CheckInterface__1.htm)|
Указывает, что для указанного типа интерфейса потребуется проверить, реализуем
ли его экспортированный тип.  
---|---  
##  __См. также
#### Ссылки
[Tessa.Platform.Composition - пространство
имён](N_Tessa_Platform_Composition.htm)
