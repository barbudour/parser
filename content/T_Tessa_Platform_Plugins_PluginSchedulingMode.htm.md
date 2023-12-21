# PluginSchedulingMode - класс
Способ диспетчеризации плагина.
## __Definition
 **Пространство имён:** [Tessa.Platform.Plugins](N_Tessa_Platform_Plugins.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class PluginSchedulingMode : IEquatable<PluginSchedulingMode>
VB __Копировать
     Public NotInheritable Class PluginSchedulingMode
    	Implements IEquatable(Of PluginSchedulingMode)
C++ __Копировать
     public ref class PluginSchedulingMode sealed : IEquatable<PluginSchedulingMode^>
F# __Копировать
     [<SealedAttribute>]
    type PluginSchedulingMode = 
        class
            interface IEquatable<PluginSchedulingMode>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PluginSchedulingMode
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<PluginSchedulingMode>
##  __Конструкторы
[PluginSchedulingMode](M_Tessa_Platform_Plugins_PluginSchedulingMode__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[DisplayName](P_Tessa_Platform_Plugins_PluginSchedulingMode_DisplayName.htm)|
Отображаемое имя для способа диспетчеризации.  
---|---  
[ID](P_Tessa_Platform_Plugins_PluginSchedulingMode_ID.htm)|  Уникальный
идентификатор способа диспетчеризации, по которому сравниваются объекты.  
## __Методы
[Equals(Object)](M_Tessa_Platform_Plugins_PluginSchedulingMode_Equals.htm)|
Сравнивает текущий объект с заданным.  
(Переопределяет
[Object.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)))  
---|---  
[Equals(PluginSchedulingMode)](M_Tessa_Platform_Plugins_PluginSchedulingMode_Equals_1.htm)|
Сравнивает текущий объект с заданным.  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Platform_Plugins_PluginSchedulingMode_GetHashCode.htm)|
Возвращает хеш-код объекта.  
(Переопределяет
[Object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode))  
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
[ToString](M_Tessa_Platform_Plugins_PluginSchedulingMode_ToString.htm)|
Возвращает строковое представление объекта.  
(Переопределяет
[Object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring))  
##  __Операторы
[Equality(PluginSchedulingMode,
PluginSchedulingMode)](M_Tessa_Platform_Plugins_PluginSchedulingMode_op_Equality.htm)|
Сравнивает заданные значения на равенство.  
---|---  
[Explicit(PluginSchedulingMode to
Guid)](M_Tessa_Platform_Plugins_PluginSchedulingMode_op_Explicit.htm)|  
[Explicit(PluginSchedulingMode to
String)](M_Tessa_Platform_Plugins_PluginSchedulingMode_op_Explicit_1.htm)|  
[Inequality(PluginSchedulingMode,
PluginSchedulingMode)](M_Tessa_Platform_Plugins_PluginSchedulingMode_op_Inequality.htm)|
Сравнивает заданные значения на неравенство.  
##  __Поля
[Daily](F_Tessa_Platform_Plugins_PluginSchedulingMode_Daily.htm)|  Каждый день
в нерабочее время.  
---|---  
[Normal](F_Tessa_Platform_Plugins_PluginSchedulingMode_Normal.htm)|  Несколько
раз в час.  
[Often](F_Tessa_Platform_Plugins_PluginSchedulingMode_Often.htm)|  Несколько
раз в минуту.  
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
[Tessa.Platform.Plugins - пространство имён](N_Tessa_Platform_Plugins.htm)
