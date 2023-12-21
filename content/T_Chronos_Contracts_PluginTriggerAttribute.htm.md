# PluginTriggerAttribute - класс
Атрибут, указывающий метаданные дополнительного триггера, на основании
которого планировщик будет вызывать плагин.
## __Definition
 **Пространство имён:** [Chronos.Contracts](N_Chronos_Contracts.htm)  
 **Сборка:** Chronos.Contracts (в Chronos.Contracts.dll) Версия: 3.6.0.17
C# __Копировать
    [AttributeUsageAttribute(AttributeTargets.Class, Inherited = false, AllowMultiple = true)]
    public sealed class PluginTriggerAttribute : Attribute, 
    	IPluginMetadataTrigger, ISerializableMetadata<IPluginMetadataTrigger>
VB __Копировать
    <AttributeUsageAttribute(AttributeTargets.Class, Inherited := false, AllowMultiple := true)>
    Public NotInheritable Class PluginTriggerAttribute
    	Inherits Attribute
    	Implements IPluginMetadataTrigger, ISerializableMetadata(Of IPluginMetadataTrigger)
C++ __Копировать
    [AttributeUsageAttribute(AttributeTargets::Class, Inherited = false, AllowMultiple = true)]
    public ref class PluginTriggerAttribute sealed : public Attribute, 
    	IPluginMetadataTrigger, ISerializableMetadata<IPluginMetadataTrigger^>
F# __Копировать
     [<SealedAttribute>]
    [<AttributeUsageAttribute(AttributeTargets.Class, Inherited = false, AllowMultiple = true)>]
    type PluginTriggerAttribute = 
        class
            inherit Attribute
            interface IPluginMetadataTrigger
            interface ISerializableMetadata<IPluginMetadataTrigger>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[Attribute](https://learn.microsoft.com/dotnet/api/system.attribute) __ PluginTriggerAttribute
Implements
    [IPluginMetadataTrigger](T_Chronos_Contracts_IPluginMetadataTrigger.htm), [ISerializableMetadata](T_Chronos_Contracts_ISerializableMetadata_1.htm)<[IPluginMetadataTrigger](T_Chronos_Contracts_IPluginMetadataTrigger.htm)>
##  __Заметки
Атрибут должен использоваться на классе, реализующем интерфейс
[IPlugin](T_Chronos_Contracts_IPlugin.htm) и уже имеющим атрибут
[PluginAttribute](T_Chronos_Contracts_PluginAttribute.htm).
## __Конструкторы
[PluginTriggerAttribute](M_Chronos_Contracts_PluginTriggerAttribute__ctor.htm)|
Инициализирует новый экземпляр класса PluginTriggerAttribute  
---|---  
##  __Свойства
[ConfigFile](P_Chronos_Contracts_PluginTriggerAttribute_ConfigFile.htm)|  Имя
или путь к конфигурационному файлу, описывающему плагин, относительно папки со
сборкой плагина.  
---|---  
[Cron](P_Chronos_Contracts_PluginTriggerAttribute_Cron.htm)|  Описание времени
вызова плагина в строке формата Cron.  
[RepeatSecondInterval](P_Chronos_Contracts_PluginTriggerAttribute_RepeatSecondInterval.htm)|
Целочисленный интервал в секундах между вызовами плагина.  
[TypeId](https://learn.microsoft.com/dotnet/api/system.attribute.typeid#system-
attribute-typeid)| When implemented in a derived class, gets a unique
identifier for this
[Attribute](https://learn.microsoft.com/dotnet/api/system.attribute).  
(Унаследован от
[Attribute](https://learn.microsoft.com/dotnet/api/system.attribute))  
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.attribute.equals#system-
attribute-equals\(system-object\))| Returns a value that indicates whether
this instance is equal to a specified object.  
(Унаследован от
[Attribute](https://learn.microsoft.com/dotnet/api/system.attribute))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.attribute.gethashcode#system-
attribute-gethashcode)| Returns the hash code for this instance.  
(Унаследован от
[Attribute](https://learn.microsoft.com/dotnet/api/system.attribute))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[IsDefaultAttribute](https://learn.microsoft.com/dotnet/api/system.attribute.isdefaultattribute#system-
attribute-isdefaultattribute)| When overridden in a derived class, indicates
whether the value of this instance is the default value for the derived class.  
(Унаследован от
[Attribute](https://learn.microsoft.com/dotnet/api/system.attribute))  
[Match](https://learn.microsoft.com/dotnet/api/system.attribute.match#system-
attribute-match\(system-object\))| When overridden in a derived class, returns
a value that indicates whether this instance equals a specified object.  
(Унаследован от
[Attribute](https://learn.microsoft.com/dotnet/api/system.attribute))  
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
[ConfigFileSpecified](M_Chronos_Platform_Scheduling_SchedulingExtensions_ConfigFileSpecified.htm)|
Возвращает признак того, что метаданные содержат информацию о конфигурационном
файле.  
(Определяется
[SchedulingExtensions](T_Chronos_Platform_Scheduling_SchedulingExtensions.htm))  
---|---  
[CronSpecified](M_Chronos_Platform_Scheduling_SchedulingExtensions_CronSpecified.htm)|
Возвращает признак того, что метаданные содержат информацию о строке в формате
Cron.  
(Определяется
[SchedulingExtensions](T_Chronos_Platform_Scheduling_SchedulingExtensions.htm))  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[RepeatSecondIntervalSpecified](M_Chronos_Platform_Scheduling_SchedulingExtensions_RepeatSecondIntervalSpecified.htm)|
Возвращает признак того, что метаданные содержат информацию об интервале между
вызовами плагина.  
(Определяется
[SchedulingExtensions](T_Chronos_Platform_Scheduling_SchedulingExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[TriggerHasData](M_Chronos_Platform_Scheduling_SchedulingExtensions_TriggerHasData.htm)|
Возвращает признак того, что метаданные содержат какую-либо информацию по
триггеру.  
(Определяется
[SchedulingExtensions](T_Chronos_Platform_Scheduling_SchedulingExtensions.htm))  
[ValidateTrigger](M_Chronos_Platform_Scheduling_SchedulingExtensions_ValidateTrigger.htm)|
Выполняет проверку корректности заданных метаданных триггера.  
(Определяется
[SchedulingExtensions](T_Chronos_Platform_Scheduling_SchedulingExtensions.htm))  
##  __См. также
#### Ссылки
[Chronos.Contracts - пространство имён](N_Chronos_Contracts.htm)
