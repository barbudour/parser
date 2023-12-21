# PluginImportingResult - класс
Результат импортирования плагинов, выполненный с помощью метода
[Import(IPluginFinder)](M_Chronos_Platform_Scheduling_PluginImporter_Import.htm).
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class PluginImportingResult
VB __Копировать
     Public NotInheritable Class PluginImportingResult
C++ __Копировать
     public ref class PluginImportingResult sealed
F# __Копировать
     [<SealedAttribute>]
    type PluginImportingResult = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PluginImportingResult
##  __Свойства
[AddedPlugins](P_Chronos_Platform_Scheduling_PluginImportingResult_AddedPlugins.htm)|
Получает список плагинов, которые ранее отсутствовали и были добавлены при
данном импортировании.  
---|---  
[AllResultingPlugins](P_Chronos_Platform_Scheduling_PluginImportingResult_AllResultingPlugins.htm)|
Список всех плагинов, доступных после импортирования.  
[RemovedPlugins](P_Chronos_Platform_Scheduling_PluginImportingResult_RemovedPlugins.htm)|
Список плагинов, которые были импортированы ранее и были удалены при данном
импортировании.  
[UnchangedPlugins](P_Chronos_Platform_Scheduling_PluginImportingResult_UnchangedPlugins.htm)|
Список плагинов, которые были импортированы ранее и не были удалены при данном
импортировании.  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
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
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
