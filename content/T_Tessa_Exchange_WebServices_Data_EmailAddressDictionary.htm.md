# EmailAddressDictionary - класс
Represents a dictionary of e-mail addresses.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
    [EditorBrowsableAttribute(EditorBrowsableState.Never)]
    public sealed class EmailAddressDictionary : DictionaryProperty<EmailAddressKey, EmailAddressEntry>
VB __Копировать
    <EditorBrowsableAttribute(EditorBrowsableState.Never)>
    Public NotInheritable Class EmailAddressDictionary
    	Inherits DictionaryProperty(Of EmailAddressKey, EmailAddressEntry)
C++ __Копировать
    [EditorBrowsableAttribute(EditorBrowsableState::Never)]
    public ref class EmailAddressDictionary sealed : public DictionaryProperty<EmailAddressKey, EmailAddressEntry^>
F# __Копировать
     [<SealedAttribute>]
    [<EditorBrowsableAttribute(EditorBrowsableState.Never)>]
    type EmailAddressDictionary = 
        class
            inherit DictionaryProperty<EmailAddressKey, EmailAddressEntry>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ComplexProperty](T_Tessa_Exchange_WebServices_Data_ComplexProperty.htm) __[DictionaryProperty](T_Tessa_Exchange_WebServices_Data_DictionaryProperty_2.htm)<[EmailAddressKey](T_Tessa_Exchange_WebServices_Data_EmailAddressKey.htm), [EmailAddressEntry](T_Tessa_Exchange_WebServices_Data_EmailAddressEntry.htm)> __ EmailAddressDictionary
##  __Конструкторы
[EmailAddressDictionary](M_Tessa_Exchange_WebServices_Data_EmailAddressDictionary__ctor.htm)|
Инициализирует новый экземпляр класса EmailAddressDictionary  
---|---  
##  __Свойства
[Item](P_Tessa_Exchange_WebServices_Data_EmailAddressDictionary_Item.htm)|
Gets or sets the e-mail address at the specified key.  
---|---  
## __Методы
[Contains](M_Tessa_Exchange_WebServices_Data_DictionaryProperty_2_Contains.htm)|
Determines whether this instance contains the specified key.  
(Унаследован от [DictionaryProperty<TKey,
TEntry>](T_Tessa_Exchange_WebServices_Data_DictionaryProperty_2.htm))  
---|---  
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
[TryGetValue](M_Tessa_Exchange_WebServices_Data_EmailAddressDictionary_TryGetValue.htm)|
Tries to get the e-mail address associated with the specified key.  
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
