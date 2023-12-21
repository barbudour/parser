# HookableServiceProxy<TService> \- класс
Абстрактный прокси-объект для hook-сервиса, обеспечивающий расширяемость для
объекта [HookableService<TService>](T_Tessa_Platform_HookableService_1.htm) и
декорирующий другой объект
[HookableServiceHook<TService>](T_Tessa_Platform_HookableServiceHook_1.htm).
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class HookableServiceProxy<TService> : HookableServiceHook<TService>
    where TService : class
VB __Копировать
     Public MustInherit Class HookableServiceProxy(Of TService As Class)
    	Inherits HookableServiceHook(Of TService)
C++ __Копировать
    generic<typename TService>
    where TService : ref class
    public ref class HookableServiceProxy abstract : public HookableServiceHook<TService>
F# __Копировать
     [<AbstractClassAttribute>]
    type HookableServiceProxy<'TService when 'TService : not struct> = 
        class
            inherit HookableServiceHook<'TService>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[HookableServiceHook](T_Tessa_Platform_HookableServiceHook_1.htm)<TService> __ HookableServiceProxy<TService>
Derived
[Tessa.Scheme.HookableSchemeServiceProxy](T_Tessa_Scheme_HookableSchemeServiceProxy.htm)
#### Параметры типа
TService
    Тип сервиса, расширяемость которого обеспечивается.
##  __Конструкторы
[HookableServiceProxy<TService>](M_Tessa_Platform_HookableServiceProxy_1__ctor.htm)|
Инициализирует новый экземпляр класса HookableServiceProxy<TService>  
---|---  
##  __Свойства
[NextHook](P_Tessa_Platform_HookableServiceHook_1_NextHook.htm)|  
(Унаследован от
[HookableServiceHook<TService>](T_Tessa_Platform_HookableServiceHook_1.htm))  
---|---  
[ProxiedService](P_Tessa_Platform_HookableServiceProxy_1_ProxiedService.htm)|  
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
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
