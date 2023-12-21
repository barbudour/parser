# BaseGuidCombProvider - класс
##  __Definition
 **Пространство имён:**
[Tessa.Platform.GuidComb](N_Tessa_Platform_GuidComb.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class BaseGuidCombProvider : IGuidCombProvider
VB __Копировать
     Public MustInherit Class BaseGuidCombProvider
    	Implements IGuidCombProvider
C++ __Копировать
     public ref class BaseGuidCombProvider abstract : IGuidCombProvider
F# __Копировать
     [<AbstractClassAttribute>]
    type BaseGuidCombProvider = 
        class
            interface IGuidCombProvider
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ BaseGuidCombProvider
Derived
[Tessa.Platform.GuidComb.PostgreSqlGuidCombProvider](T_Tessa_Platform_GuidComb_PostgreSqlGuidCombProvider.htm)
[Tessa.Platform.GuidComb.SqlGuidCombProvider](T_Tessa_Platform_GuidComb_SqlGuidCombProvider.htm)
Implements
    [IGuidCombProvider](T_Tessa_Platform_GuidComb_IGuidCombProvider.htm)
##  __Конструкторы
[BaseGuidCombProvider](M_Tessa_Platform_GuidComb_BaseGuidCombProvider__ctor.htm)|
Инициализирует новый экземпляр класса BaseGuidCombProvider  
---|---  
##  __Свойства
[GuidProvider](P_Tessa_Platform_GuidComb_BaseGuidCombProvider_GuidProvider.htm)|  
---|---  
[TimestampProvider](P_Tessa_Platform_GuidComb_BaseGuidCombProvider_TimestampProvider.htm)|  
## __Методы
[Create()](M_Tessa_Platform_GuidComb_BaseGuidCombProvider_Create.htm)|  
---|---  
[Create(DateTime)](M_Tessa_Platform_GuidComb_BaseGuidCombProvider_Create_1.htm)|  
[Create(Guid)](M_Tessa_Platform_GuidComb_BaseGuidCombProvider_Create_2.htm)|  
[Create(Guid,
DateTime)](M_Tessa_Platform_GuidComb_BaseGuidCombProvider_Create_3.htm)|  
[DefaultTimestampProvider](M_Tessa_Platform_GuidComb_BaseGuidCombProvider_DefaultTimestampProvider.htm)|  
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
[GetTimestamp](M_Tessa_Platform_GuidComb_BaseGuidCombProvider_GetTimestamp.htm)|  
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
##  __Поля
[DateTimeStrategy](F_Tessa_Platform_GuidComb_BaseGuidCombProvider_DateTimeStrategy.htm)|  
---|---  
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
[Tessa.Platform.GuidComb - пространство имён](N_Tessa_Platform_GuidComb.htm)
