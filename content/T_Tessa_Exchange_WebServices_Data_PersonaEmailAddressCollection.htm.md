# PersonaEmailAddressCollection - класс
Represents a collection of persona e-mail addresses.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class PersonaEmailAddressCollection : ComplexPropertyCollection<PersonaEmailAddress>
VB __Копировать
     Public NotInheritable Class PersonaEmailAddressCollection
    	Inherits ComplexPropertyCollection(Of PersonaEmailAddress)
C++ __Копировать
     public ref class PersonaEmailAddressCollection sealed : public ComplexPropertyCollection<PersonaEmailAddress^>
F# __Копировать
     [<SealedAttribute>]
    type PersonaEmailAddressCollection = 
        class
            inherit ComplexPropertyCollection<PersonaEmailAddress>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ComplexProperty](T_Tessa_Exchange_WebServices_Data_ComplexProperty.htm) __[ComplexPropertyCollection](T_Tessa_Exchange_WebServices_Data_ComplexPropertyCollection_1.htm)<[PersonaEmailAddress](T_Tessa_Exchange_WebServices_Data_PersonaEmailAddress.htm)> __ PersonaEmailAddressCollection
##  __Свойства
[Count](P_Tessa_Exchange_WebServices_Data_ComplexPropertyCollection_1_Count.htm)|
Gets the total number of properties in the collection.  
(Унаследован от
[ComplexPropertyCollection<TComplexProperty>](T_Tessa_Exchange_WebServices_Data_ComplexPropertyCollection_1.htm))  
---|---  
[Item](P_Tessa_Exchange_WebServices_Data_ComplexPropertyCollection_1_Item.htm)|
Gets the property at the specified index.  
(Унаследован от
[ComplexPropertyCollection<TComplexProperty>](T_Tessa_Exchange_WebServices_Data_ComplexPropertyCollection_1.htm))  
##  __Методы
[Add(PersonaEmailAddress)](M_Tessa_Exchange_WebServices_Data_PersonaEmailAddressCollection_Add_2.htm)|
Adds a persona e-mail address to the collection.  
---|---  
[Add(String)](M_Tessa_Exchange_WebServices_Data_PersonaEmailAddressCollection_Add.htm)|
Adds a persona e-mail address to the collection.  
[Add(String,
String)](M_Tessa_Exchange_WebServices_Data_PersonaEmailAddressCollection_Add_1.htm)|
Adds an e-mail address to the collection.  
[AddRange(IEnumerable<String>)](M_Tessa_Exchange_WebServices_Data_PersonaEmailAddressCollection_AddRange.htm)|
Adds multiple e-mail addresses to the collection.  
[AddRange(IEnumerable<PersonaEmailAddress>)](M_Tessa_Exchange_WebServices_Data_PersonaEmailAddressCollection_AddRange_1.htm)|
Adds multiple persona e-mail addresses to the collection.  
[Clear](M_Tessa_Exchange_WebServices_Data_PersonaEmailAddressCollection_Clear.htm)|
Clears the collection.  
[Contains](M_Tessa_Exchange_WebServices_Data_ComplexPropertyCollection_1_Contains.htm)|
Determines whether a specific property is in the collection.  
(Унаследован от
[ComplexPropertyCollection<TComplexProperty>](T_Tessa_Exchange_WebServices_Data_ComplexPropertyCollection_1.htm))  
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
[GetEnumerator](M_Tessa_Exchange_WebServices_Data_ComplexPropertyCollection_1_GetEnumerator.htm)|
Gets an enumerator that iterates through the elements of the collection.  
(Унаследован от
[ComplexPropertyCollection<TComplexProperty>](T_Tessa_Exchange_WebServices_Data_ComplexPropertyCollection_1.htm))  
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
[IndexOf](M_Tessa_Exchange_WebServices_Data_ComplexPropertyCollection_1_IndexOf.htm)|
Searches for a specific property and return its zero-based index within the
collection.  
(Унаследован от
[ComplexPropertyCollection<TComplexProperty>](T_Tessa_Exchange_WebServices_Data_ComplexPropertyCollection_1.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Remove](M_Tessa_Exchange_WebServices_Data_PersonaEmailAddressCollection_Remove.htm)|
Removes a persona e-mail address from the collection.  
[RemoveAt](M_Tessa_Exchange_WebServices_Data_PersonaEmailAddressCollection_RemoveAt.htm)|
Removes a persona e-mail address from the collection.  
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
