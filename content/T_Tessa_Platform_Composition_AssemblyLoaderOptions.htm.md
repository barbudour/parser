# AssemblyLoaderOptions - класс
Настройки, связанные с экспортом метаданных из сборки.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Composition](N_Tessa_Platform_Composition.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class AssemblyLoaderOptions : IAssemblyLoaderOptions
VB __Копировать
     Public Class AssemblyLoaderOptions
    	Implements IAssemblyLoaderOptions
C++ __Копировать
     public ref class AssemblyLoaderOptions : IAssemblyLoaderOptions
F# __Копировать
     type AssemblyLoaderOptions = 
        class
            interface IAssemblyLoaderOptions
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ AssemblyLoaderOptions
Implements
    [IAssemblyLoaderOptions](T_Tessa_Platform_Composition_IAssemblyLoaderOptions.htm)
##  __Заметки
Наследники класса могут добавлять свойства.
## __Конструкторы
[AssemblyLoaderOptions](M_Tessa_Platform_Composition_AssemblyLoaderOptions__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[Flags](P_Tessa_Platform_Composition_AssemblyLoaderOptions_Flags.htm)| Флаги,
определяющие процесс загрузки сборок при экспорте метаинформации.  
---|---  
[InterfaceTypesToCheck](P_Tessa_Platform_Composition_AssemblyLoaderOptions_InterfaceTypesToCheck.htm)|
Типы интерфейсов, для которых надо проверить, что экспортируемый тип с
атрибутом их реализует.  
##  __Методы
[CheckInterface<T>](M_Tessa_Platform_Composition_AssemblyLoaderOptions_CheckInterface__1.htm)|
Указывает, что для указанного типа интерфейса потребуется проверить, реализуем
ли его экспортированный тип.  
---|---  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Composition - пространство
имён](N_Tessa_Platform_Composition.htm)
