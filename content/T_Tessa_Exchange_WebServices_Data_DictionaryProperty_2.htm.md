# DictionaryProperty<TKey, TEntry> \- класс
Represents a generic dictionary that can be sent to or retrieved from EWS.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
    [EditorBrowsableAttribute(EditorBrowsableState.Never)]
    public abstract class DictionaryProperty<TKey, TEntry> : ComplexProperty
    where TEntry : DictionaryEntryProperty<TKey>
VB __Копировать
    <EditorBrowsableAttribute(EditorBrowsableState.Never)>
    Public MustInherit Class DictionaryProperty(Of TKey, TEntry As DictionaryEntryProperty(Of TKey))
    	Inherits ComplexProperty
C++ __Копировать
    [EditorBrowsableAttribute(EditorBrowsableState::Never)]
    generic<typename TKey, typename TEntry>
    where TEntry : DictionaryEntryProperty<TKey>
    public ref class DictionaryProperty abstract : public ComplexProperty
F# __Копировать
     [<AbstractClassAttribute>]
    [<EditorBrowsableAttribute(EditorBrowsableState.Never)>]
    type DictionaryProperty<'TKey, 'TEntry when 'TEntry : DictionaryEntryProperty<'TKey>> = 
        class
            inherit ComplexProperty
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ComplexProperty](T_Tessa_Exchange_WebServices_Data_ComplexProperty.htm) __ DictionaryProperty<TKey, TEntry>
Derived
[Tessa.Exchange.WebServices.Data.EmailAddressDictionary](T_Tessa_Exchange_WebServices_Data_EmailAddressDictionary.htm)
[Tessa.Exchange.WebServices.Data.ImAddressDictionary](T_Tessa_Exchange_WebServices_Data_ImAddressDictionary.htm)
[Tessa.Exchange.WebServices.Data.PhoneNumberDictionary](T_Tessa_Exchange_WebServices_Data_PhoneNumberDictionary.htm)
[Tessa.Exchange.WebServices.Data.PhysicalAddressDictionary](T_Tessa_Exchange_WebServices_Data_PhysicalAddressDictionary.htm)
#### Параметры типа
TKey
    The type of key.
TEntry
    The type of entry.
##  __Конструкторы
[DictionaryProperty<TKey,
TEntry>](M_Tessa_Exchange_WebServices_Data_DictionaryProperty_2__ctor.htm)|
Инициализирует новый экземпляр класса DictionaryProperty<TKey, TEntry>  
---|---  
##  __Методы
[Contains](M_Tessa_Exchange_WebServices_Data_DictionaryProperty_2_Contains.htm)|
Determines whether this instance contains the specified key.  
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
