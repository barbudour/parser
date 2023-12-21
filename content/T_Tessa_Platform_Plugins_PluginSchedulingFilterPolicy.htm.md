# PluginSchedulingFilterPolicy - класс
Политика фильтрации расширений плагинов
[IPluginExtension](T_Tessa_Platform_Plugins_IPluginExtension.htm),
использующая политику
[IPluginSchedulingPolicy](T_Tessa_Platform_Plugins_IPluginSchedulingPolicy.htm)
для того, чтобы не выполнять методы плагинов, для которых в контексте
[IPluginExtensionContext](T_Tessa_Platform_Plugins_IPluginExtensionContext.htm)
использован способ диспетчеризации
[SchedulingMode](P_Tessa_Platform_Plugins_IPluginExtensionContext_SchedulingMode.htm),
запрещённый указанной политикой. Если политика
[IPluginSchedulingPolicy](T_Tessa_Platform_Plugins_IPluginSchedulingPolicy.htm)
не зарегистрирована, то метод расширения не будет выполнен, т.е. указание этой
политики является обязательным для выполнения таких расширений.
## __Definition
 **Пространство имён:** [Tessa.Platform.Plugins](N_Tessa_Platform_Plugins.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class PluginSchedulingFilterPolicy : IFilterPolicy, 
    	IExtensionPolicy
VB __Копировать
     Public NotInheritable Class PluginSchedulingFilterPolicy
    	Implements IFilterPolicy, IExtensionPolicy
C++ __Копировать
     public ref class PluginSchedulingFilterPolicy sealed : IFilterPolicy, 
    	IExtensionPolicy
F# __Копировать
     [<SealedAttribute>]
    type PluginSchedulingFilterPolicy = 
        class
            interface IFilterPolicy
            interface IExtensionPolicy
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PluginSchedulingFilterPolicy
Implements
    [IExtensionPolicy](T_Tessa_Extensions_IExtensionPolicy.htm), [IFilterPolicy](T_Tessa_Extensions_IFilterPolicy.htm)
##  __Конструкторы
[PluginSchedulingFilterPolicy](M_Tessa_Platform_Plugins_PluginSchedulingFilterPolicy__ctor.htm)|
Инициализирует новый экземпляр класса PluginSchedulingFilterPolicy  
---|---  
##  __Свойства
[Instance](P_Tessa_Platform_Plugins_PluginSchedulingFilterPolicy_Instance.htm)|
Экземпляр класса.  
---|---  
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[FilterAsync](M_Tessa_Platform_Plugins_PluginSchedulingFilterPolicy_FilterAsync.htm)|
Возвращает признак того, что выполнение метода с заданным параметром разрешено
для экземпляра расширения.  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetFilterContextAsync](M_Tessa_Platform_Plugins_PluginSchedulingFilterPolicy_GetFilterContextAsync.htm)|
Возвращает контекст фильтрации, используемый для определение разрешений на
выполнение метода для экземпляров расширений.  
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
[Tessa.Platform.Plugins - пространство имён](N_Tessa_Platform_Plugins.htm)
