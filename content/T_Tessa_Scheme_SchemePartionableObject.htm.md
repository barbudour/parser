# SchemePartionableObject - класс
##  __Definition
 **Пространство имён:** [Tessa.Scheme](N_Tessa_Scheme.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class SchemePartionableObject : SchemeObject
VB __Копировать
     Public MustInherit Class SchemePartionableObject
    	Inherits SchemeObject
C++ __Копировать
     public ref class SchemePartionableObject abstract : public SchemeObject
F# __Копировать
     [<AbstractClassAttribute>]
    type SchemePartionableObject = 
        class
            inherit SchemeObject
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[SchemeObject](T_Tessa_Scheme_SchemeObject.htm) __ SchemePartionableObject
Derived
[Tessa.Scheme.SchemeNamedObject](T_Tessa_Scheme_SchemeNamedObject.htm)
[Tessa.Scheme.SchemeRecord](T_Tessa_Scheme_SchemeRecord.htm)
##  __Свойства
[IsPartitionInherited](P_Tessa_Scheme_SchemePartionableObject_IsPartitionInherited.htm)|  
---|---  
[IsPermanent](P_Tessa_Scheme_SchemeObject_IsPermanent.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[IsSealed](P_Tessa_Scheme_SchemeObject_IsSealed.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[IsSystem](P_Tessa_Scheme_SchemeObject_IsSystem.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[LinkedWith](P_Tessa_Scheme_SchemeObject_LinkedWith.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[Parent](P_Tessa_Scheme_SchemeObject_Parent.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[Partition](P_Tessa_Scheme_SchemePartionableObject_Partition.htm)|  
## __Методы
[BeginDeserializationOverride](M_Tessa_Scheme_SchemeObject_BeginDeserializationOverride.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
---|---  
[Copy](M_Tessa_Scheme_SchemePartionableObject_Copy.htm)|  
(Переопределяет
[SchemeObject.Copy(SchemeObject)](M_Tessa_Scheme_SchemeObject_Copy.htm))  
[Deserialize](M_Tessa_Scheme_SchemeObject_Deserialize.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[EndDeserializationOverride](M_Tessa_Scheme_SchemePartionableObject_EndDeserializationOverride.htm)|  
(Переопределяет
[SchemeObject.EndDeserializationOverride(SerializationInfo)](M_Tessa_Scheme_SchemeObject_EndDeserializationOverride.htm))  
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
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetInheritedPartition](M_Tessa_Scheme_SchemePartionableObject_GetInheritedPartition.htm)|  
[GetObjectData](M_Tessa_Scheme_SchemePartionableObject_GetObjectData.htm)|  
(Переопределяет
[SchemeObject.GetObjectData(SerializationInfo)](M_Tessa_Scheme_SchemeObject_GetObjectData.htm))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[IsInvalidPartition](M_Tessa_Scheme_SchemePartionableObject_IsInvalidPartition.htm)|  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[OnSealed](M_Tessa_Scheme_SchemeObject_OnSealed.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[RaisePropertyChanged](M_Tessa_Scheme_SchemeObject_RaisePropertyChanged.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[ReadXml(String)](M_Tessa_Scheme_SchemeObject_ReadXml.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[ReadXml(XmlReader)](M_Tessa_Scheme_SchemeObject_ReadXml_1.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[Seal](M_Tessa_Scheme_SchemeObject_Seal.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[WriteXml](M_Tessa_Scheme_SchemeObject_WriteXml.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
##  __События
[PropertyChanged](E_Tessa_Scheme_SchemeObject_PropertyChanged.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
---|---  
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
[Tessa.Scheme - пространство имён](N_Tessa_Scheme.htm)
