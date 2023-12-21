# SearchFilter.ExcludesBitmask - класс
Represents a bitmask exclusion search filter. Applications can use
ExcludesBitExcludesBitmaskFilter to define conditions such as "(OrdinalField
and 0x0010) != 0x0010"
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ExcludesBitmask : SearchFilter.PropertyBasedFilter
VB __Копировать
     Public NotInheritable Class ExcludesBitmask
    	Inherits SearchFilter.PropertyBasedFilter
C++ __Копировать
     public ref class ExcludesBitmask sealed : public SearchFilter.PropertyBasedFilter
F# __Копировать
     [<SealedAttribute>]
    type ExcludesBitmask = 
        class
            inherit SearchFilter.PropertyBasedFilter
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ComplexProperty](T_Tessa_Exchange_WebServices_Data_ComplexProperty.htm) __[SearchFilter](T_Tessa_Exchange_WebServices_Data_SearchFilter.htm) __[SearchFilter.PropertyBasedFilter](T_Tessa_Exchange_WebServices_Data_SearchFilter_PropertyBasedFilter.htm) __ SearchFilter.ExcludesBitmask
##  __Конструкторы
[SearchFilter.ExcludesBitmask()](M_Tessa_Exchange_WebServices_Data_SearchFilter_ExcludesBitmask__ctor.htm)|
Initializes a new instance of the SearchFilter.ExcludesBitmask class.  
---|---  
[SearchFilter.ExcludesBitmask(PropertyDefinitionBase,
Int32)](M_Tessa_Exchange_WebServices_Data_SearchFilter_ExcludesBitmask__ctor_1.htm)|
Initializes a new instance of the SearchFilter.ExcludesBitmask class.  
## __Свойства
[Bitmask](P_Tessa_Exchange_WebServices_Data_SearchFilter_ExcludesBitmask_Bitmask.htm)|
Gets or sets the bitmask to compare the property with.  
---|---  
[PropertyDefinition](P_Tessa_Exchange_WebServices_Data_SearchFilter_PropertyBasedFilter_PropertyDefinition.htm)|
Gets or sets the definition of the property that is involved in the search
filter. Property definitions are available as static members from schema
classes (for example, EmailMessageSchema.Subject, AppointmentSchema.Start,
ContactSchema.GivenName, etc.)  
(Унаследован от
[SearchFilter.PropertyBasedFilter](T_Tessa_Exchange_WebServices_Data_SearchFilter_PropertyBasedFilter.htm))  
##  __Методы
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
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
