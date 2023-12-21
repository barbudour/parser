# PluginImportingItem - класс
Информация об импортируемом плагине.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class PluginImportingItem : IEquatable<PluginImportingItem>
VB __Копировать
     Public NotInheritable Class PluginImportingItem
    	Implements IEquatable(Of PluginImportingItem)
C++ __Копировать
     public ref class PluginImportingItem sealed : IEquatable<PluginImportingItem^>
F# __Копировать
     [<SealedAttribute>]
    type PluginImportingItem = 
        class
            interface IEquatable<PluginImportingItem>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PluginImportingItem
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<PluginImportingItem>
##  __Конструкторы
[PluginImportingItem](M_Chronos_Platform_Scheduling_PluginImportingItem__ctor.htm)|
Создаёт экземпляр класса с указанием типа плагина, метаданных плагина и списка
дополнительных триггеров.  
---|---  
## __Свойства
[AdditionalTriggers](P_Chronos_Platform_Scheduling_PluginImportingItem_AdditionalTriggers.htm)|
Список дополнительных триггеров (кроме метаданных плагина
[PluginMetadata](P_Chronos_Platform_Scheduling_PluginImportingItem_PluginMetadata.htm)).  
---|---  
[PluginAssemblyLocation](P_Chronos_Platform_Scheduling_PluginImportingItem_PluginAssemblyLocation.htm)|
Полный путь к сборке, содержащей плагин.  
[PluginAssemblyQualifiedName](P_Chronos_Platform_Scheduling_PluginImportingItem_PluginAssemblyQualifiedName.htm)|
Полное имя типа плагина с указанием имени сборки.  
[PluginMetadata](P_Chronos_Platform_Scheduling_PluginImportingItem_PluginMetadata.htm)|
Метаданные плагина.  
[PluginTypeFullName](P_Chronos_Platform_Scheduling_PluginImportingItem_PluginTypeFullName.htm)|
Полное имя типа плагина.  
[SupportGracefulStop](P_Chronos_Platform_Scheduling_PluginImportingItem_SupportGracefulStop.htm)|
Признак того, что плагин поддерживает вежливую остановку через интерфейс
[ISupportGracefulStop](T_Chronos_Contracts_ISupportGracefulStop.htm).  
## __Методы
[EnumerateAllTriggers](M_Chronos_Platform_Scheduling_PluginImportingItem_EnumerateAllTriggers.htm)|
Перечисляет все триггеры, содержащиеся в информации о плагине.  
---|---  
[Equals(Object)](M_Chronos_Platform_Scheduling_PluginImportingItem_Equals_1.htm)|
Проверяет объект на равенство.  
(Переопределяет
[Object.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)))  
[Equals(PluginImportingItem)](M_Chronos_Platform_Scheduling_PluginImportingItem_Equals.htm)|
Проверяет объект на равенство.  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Chronos_Platform_Scheduling_PluginImportingItem_GetHashCode.htm)|
Возвращает хеш-код объекта.  
(Переопределяет
[Object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode))  
[GetNotEmptyTriggers](M_Chronos_Platform_Scheduling_PluginImportingItem_GetNotEmptyTriggers.htm)|
Возвращает список триггеров, содержащих полезную информацию.  
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
[ToString](M_Chronos_Platform_Scheduling_PluginImportingItem_ToString.htm)|
Возвращает строковое представление объекта.  
(Переопределяет
[Object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring))  
[TryResolveConfigs](M_Chronos_Platform_Scheduling_PluginImportingItem_TryResolveConfigs.htm)|
Возвращает информацию о плагине, которая была загружена из всех
конфигурационных файлов, указанных в триггерах, или null, если доступные
плагины отсуствуют.  
[Validate](M_Chronos_Platform_Scheduling_PluginImportingItem_Validate.htm)|
Выполняет проверку на корректность информации о плагине.  
## __Методы расширения
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
