# SearchFilter.ContainsSubstring - класс
Represents a search filter that checks for the presence of a substring inside
a text property. Applications can use ContainsSubstring to define conditions
such as "Field CONTAINS Value" or "Field IS PREFIXED WITH Value".
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ContainsSubstring : SearchFilter.PropertyBasedFilter
VB __Копировать
     Public NotInheritable Class ContainsSubstring
    	Inherits SearchFilter.PropertyBasedFilter
C++ __Копировать
     public ref class ContainsSubstring sealed : public SearchFilter.PropertyBasedFilter
F# __Копировать
     [<SealedAttribute>]
    type ContainsSubstring = 
        class
            inherit SearchFilter.PropertyBasedFilter
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ComplexProperty](T_Tessa_Exchange_WebServices_Data_ComplexProperty.htm) __[SearchFilter](T_Tessa_Exchange_WebServices_Data_SearchFilter.htm) __[SearchFilter.PropertyBasedFilter](T_Tessa_Exchange_WebServices_Data_SearchFilter_PropertyBasedFilter.htm) __ SearchFilter.ContainsSubstring
##  __Конструкторы
[SearchFilter.ContainsSubstring()](M_Tessa_Exchange_WebServices_Data_SearchFilter_ContainsSubstring__ctor.htm)|
Initializes a new instance of the SearchFilter.ContainsSubstring class.  
---|---  
[SearchFilter.ContainsSubstring(PropertyDefinitionBase,
String)](M_Tessa_Exchange_WebServices_Data_SearchFilter_ContainsSubstring__ctor_1.htm)|
Initializes a new instance of the SearchFilter.ContainsSubstring class. The
ContainmentMode property is initialized to ContainmentMode.Substring, and the
ComparisonMode property is initialized to ComparisonMode.IgnoreCase.  
[SearchFilter.ContainsSubstring(PropertyDefinitionBase, String,
ContainmentMode,
ComparisonMode)](M_Tessa_Exchange_WebServices_Data_SearchFilter_ContainsSubstring__ctor_2.htm)|
Initializes a new instance of the SearchFilter.ContainsSubstring class.  
## __Свойства
[ComparisonMode](P_Tessa_Exchange_WebServices_Data_SearchFilter_ContainsSubstring_ComparisonMode.htm)|
Gets or sets the comparison mode.  
---|---  
[ContainmentMode](P_Tessa_Exchange_WebServices_Data_SearchFilter_ContainsSubstring_ContainmentMode.htm)|
Gets or sets the containment mode.  
[PropertyDefinition](P_Tessa_Exchange_WebServices_Data_SearchFilter_PropertyBasedFilter_PropertyDefinition.htm)|
Gets or sets the definition of the property that is involved in the search
filter. Property definitions are available as static members from schema
classes (for example, EmailMessageSchema.Subject, AppointmentSchema.Start,
ContactSchema.GivenName, etc.)  
(Унаследован от
[SearchFilter.PropertyBasedFilter](T_Tessa_Exchange_WebServices_Data_SearchFilter_PropertyBasedFilter.htm))  
[Value](P_Tessa_Exchange_WebServices_Data_SearchFilter_ContainsSubstring_Value.htm)|
Gets or sets the value to compare the specified property with.  
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
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
