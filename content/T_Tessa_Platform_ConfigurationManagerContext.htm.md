# ConfigurationManagerContext - класс
Контекст, переопределяющий текущий
[ConfigurationManager](T_Tessa_Platform_ConfigurationManager.htm).
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ConfigurationManagerContext : IConfigurationManagerContext
VB __Копировать
     Public NotInheritable Class ConfigurationManagerContext
    	Implements IConfigurationManagerContext
C++ __Копировать
     public ref class ConfigurationManagerContext sealed : IConfigurationManagerContext
F# __Копировать
     [<SealedAttribute>]
    type ConfigurationManagerContext = 
        class
            interface IConfigurationManagerContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ConfigurationManagerContext
Implements
    [IConfigurationManagerContext](T_Tessa_Platform_IConfigurationManagerContext.htm)
##  __Конструкторы
[ConfigurationManagerContext](M_Tessa_Platform_ConfigurationManagerContext__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[Current](P_Tessa_Platform_ConfigurationManagerContext_Current.htm)|
Возвращает текущий контекст
[IConfigurationManagerContext](T_Tessa_Platform_IConfigurationManagerContext.htm).  
---|---  
[HasCurrent](P_Tessa_Platform_ConfigurationManagerContext_HasCurrent.htm)|
Возвращает значение, показывающще, что текущий код выполняется внутри операции
с контекстом
[IConfigurationManagerContext](T_Tessa_Platform_IConfigurationManagerContext.htm),
а свойство [Current](P_Tessa_Platform_ConfigurationManagerContext_Current.htm)
ссылается на действительный контекст.  
[Manager](P_Tessa_Platform_ConfigurationManagerContext_Manager.htm)|  Объект,
управляющий конфигурацией приложений.  
[Unknown](P_Tessa_Platform_ConfigurationManagerContext_Unknown.htm)|
Неизвестный контекст
[IConfigurationManagerContext](T_Tessa_Platform_IConfigurationManagerContext.htm).  
## __Методы
[Create(ConfigurationManager)](M_Tessa_Platform_ConfigurationManagerContext_Create.htm)|
Создаёт область операции, в которой заданный
[ConfigurationManager](T_Tessa_Platform_ConfigurationManager.htm) будет
являться текущим в контексте.  
---|---  
[Create(IConfigurationManagerContext)](M_Tessa_Platform_ConfigurationManagerContext_Create_1.htm)|
Создаёт область операции, в которой заданный контекст будет являться текущим.  
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
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
