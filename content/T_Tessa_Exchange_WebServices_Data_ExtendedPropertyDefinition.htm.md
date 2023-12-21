# ExtendedPropertyDefinition - класс
Represents the definition of an extended property.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ExtendedPropertyDefinition : PropertyDefinitionBase
VB __Копировать
     Public NotInheritable Class ExtendedPropertyDefinition
    	Inherits PropertyDefinitionBase
C++ __Копировать
     public ref class ExtendedPropertyDefinition sealed : public PropertyDefinitionBase
F# __Копировать
     [<SealedAttribute>]
    type ExtendedPropertyDefinition = 
        class
            inherit PropertyDefinitionBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[PropertyDefinitionBase](T_Tessa_Exchange_WebServices_Data_PropertyDefinitionBase.htm) __ ExtendedPropertyDefinition
##  __Конструкторы
[ExtendedPropertyDefinition(Int32,
MapiPropertyType)](M_Tessa_Exchange_WebServices_Data_ExtendedPropertyDefinition__ctor_2.htm)|
Initializes a new instance of the ExtendedPropertyDefinition class.  
---|---  
[ExtendedPropertyDefinition(DefaultExtendedPropertySet, Int32,
MapiPropertyType)](M_Tessa_Exchange_WebServices_Data_ExtendedPropertyDefinition__ctor_3.htm)|
Initializes a new instance of ExtendedPropertyDefinition.  
[ExtendedPropertyDefinition(DefaultExtendedPropertySet, String,
MapiPropertyType)](M_Tessa_Exchange_WebServices_Data_ExtendedPropertyDefinition__ctor_4.htm)|
Initializes a new instance of the ExtendedPropertyDefinition class.  
[ExtendedPropertyDefinition(Guid, Int32,
MapiPropertyType)](M_Tessa_Exchange_WebServices_Data_ExtendedPropertyDefinition__ctor.htm)|
Initializes a new instance of the ExtendedPropertyDefinition class.  
[ExtendedPropertyDefinition(Guid, String,
MapiPropertyType)](M_Tessa_Exchange_WebServices_Data_ExtendedPropertyDefinition__ctor_1.htm)|
Initializes a new instance of the ExtendedPropertyDefinition class.  
## __Свойства
[Id](P_Tessa_Exchange_WebServices_Data_ExtendedPropertyDefinition_Id.htm)|
Gets the Id of the extended property.  
---|---  
[MapiType](P_Tessa_Exchange_WebServices_Data_ExtendedPropertyDefinition_MapiType.htm)|
Gets the MAPI type of the extended property.  
[Name](P_Tessa_Exchange_WebServices_Data_ExtendedPropertyDefinition_Name.htm)|
Gets the name of the extended property.  
[PropertySet](P_Tessa_Exchange_WebServices_Data_ExtendedPropertyDefinition_PropertySet.htm)|
Gets the property set of the extended property.  
[PropertySetId](P_Tessa_Exchange_WebServices_Data_ExtendedPropertyDefinition_PropertySetId.htm)|
Gets the property set Id or the extended property.  
[Tag](P_Tessa_Exchange_WebServices_Data_ExtendedPropertyDefinition_Tag.htm)|
Gets the extended property's tag.  
[Type](P_Tessa_Exchange_WebServices_Data_ExtendedPropertyDefinition_Type.htm)|
Gets the property type.  
(Переопределяет
[PropertyDefinitionBase.Type](P_Tessa_Exchange_WebServices_Data_PropertyDefinitionBase_Type.htm))  
[Version](P_Tessa_Exchange_WebServices_Data_ExtendedPropertyDefinition_Version.htm)|
Gets the minimum Exchange version that supports this extended property.  
(Переопределяет
[PropertyDefinitionBase.Version](P_Tessa_Exchange_WebServices_Data_PropertyDefinitionBase_Version.htm))  
##  __Методы
[Equals](M_Tessa_Exchange_WebServices_Data_ExtendedPropertyDefinition_Equals.htm)|
Determines whether a given extended property definition is equal to this
extended property definition.  
(Переопределяет
[Object.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Exchange_WebServices_Data_ExtendedPropertyDefinition_GetHashCode.htm)|
Serves as a hash function for a particular type.  
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
[ToString](M_Tessa_Exchange_WebServices_Data_PropertyDefinitionBase_ToString.htm)|
Returns a [String](https://learn.microsoft.com/dotnet/api/system.string) that
represents the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[PropertyDefinitionBase](T_Tessa_Exchange_WebServices_Data_PropertyDefinitionBase.htm))  
##  __Операторы
[Equality(ExtendedPropertyDefinition,
ExtendedPropertyDefinition)](M_Tessa_Exchange_WebServices_Data_ExtendedPropertyDefinition_op_Equality.htm)|
Determines whether two specified instances of ExtendedPropertyDefinition are
equal.  
---|---  
[Inequality(ExtendedPropertyDefinition,
ExtendedPropertyDefinition)](M_Tessa_Exchange_WebServices_Data_ExtendedPropertyDefinition_op_Inequality.htm)|
Determines whether two specified instances of ExtendedPropertyDefinition are
not equal.  
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
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
