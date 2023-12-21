# SchemeObject - класс
##  __Definition
 **Пространство имён:** [Tessa.Scheme](N_Tessa_Scheme.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class SchemeObject : ISerializable, 
    	IDeserializationCallback, IXmlSerializable, INotifyPropertyChanged
VB __Копировать
     Public MustInherit Class SchemeObject
    	Implements ISerializable, IDeserializationCallback, IXmlSerializable, INotifyPropertyChanged
C++ __Копировать
     public ref class SchemeObject abstract : ISerializable, 
    	IDeserializationCallback, IXmlSerializable, INotifyPropertyChanged
F# __Копировать
     [<AbstractClassAttribute>]
    type SchemeObject = 
        class
            interface ISerializable
            interface IDeserializationCallback
            interface IXmlSerializable
            interface INotifyPropertyChanged
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ SchemeObject
Derived
[Tessa.Scheme.SchemeForeignKeyColumn](T_Tessa_Scheme_SchemeForeignKeyColumn.htm)
[Tessa.Scheme.SchemeIncludedColumn](T_Tessa_Scheme_SchemeIncludedColumn.htm)
[Tessa.Scheme.SchemeIndexedColumn](T_Tessa_Scheme_SchemeIndexedColumn.htm)
[Tessa.Scheme.SchemePartionableObject](T_Tessa_Scheme_SchemePartionableObject.htm)
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged), [IDeserializationCallback](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.ideserializationcallback), [ISerializable](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.iserializable), [IXmlSerializable](https://learn.microsoft.com/dotnet/api/system.xml.serialization.ixmlserializable)
##  __Конструкторы
[SchemeObject(Boolean)](M_Tessa_Scheme_SchemeObject__ctor.htm)| Инициализирует
новый экземпляр класса SchemeObject  
---|---  
[SchemeObject(SerializationInfo)](M_Tessa_Scheme_SchemeObject__ctor_1.htm)|
Инициализирует новый экземпляр класса SchemeObject  
##  __Свойства
[IsPermanent](P_Tessa_Scheme_SchemeObject_IsPermanent.htm)|  
---|---  
[IsSealed](P_Tessa_Scheme_SchemeObject_IsSealed.htm)|  
[IsSystem](P_Tessa_Scheme_SchemeObject_IsSystem.htm)|  
[LinkedWith](P_Tessa_Scheme_SchemeObject_LinkedWith.htm)|  
[Parent](P_Tessa_Scheme_SchemeObject_Parent.htm)|  
## __Методы
[BeginDeserializationOverride](M_Tessa_Scheme_SchemeObject_BeginDeserializationOverride.htm)|  
---|---  
[Copy](M_Tessa_Scheme_SchemeObject_Copy.htm)|  
[Deserialize](M_Tessa_Scheme_SchemeObject_Deserialize.htm)|  
[EndDeserializationOverride](M_Tessa_Scheme_SchemeObject_EndDeserializationOverride.htm)|  
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
[GetDisplayName](M_Tessa_Scheme_SchemeObject_GetDisplayName.htm)|  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetObjectData](M_Tessa_Scheme_SchemeObject_GetObjectData.htm)|  
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
[OnSealed](M_Tessa_Scheme_SchemeObject_OnSealed.htm)|  
[RaisePropertyChanged](M_Tessa_Scheme_SchemeObject_RaisePropertyChanged.htm)|  
[ReadXml(String)](M_Tessa_Scheme_SchemeObject_ReadXml.htm)|  
[ReadXml(XmlReader)](M_Tessa_Scheme_SchemeObject_ReadXml_1.htm)|  
[Seal](M_Tessa_Scheme_SchemeObject_Seal.htm)|  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[WriteXml](M_Tessa_Scheme_SchemeObject_WriteXml.htm)|  
## __События
[PropertyChanged](E_Tessa_Scheme_SchemeObject_PropertyChanged.htm)|  
---|---  
## __Поля
[ConstructorForXmlSerializationOnly](F_Tessa_Scheme_SchemeObject_ConstructorForXmlSerializationOnly.htm)|  
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
[Tessa.Scheme - пространство имён](N_Tessa_Scheme.htm)
