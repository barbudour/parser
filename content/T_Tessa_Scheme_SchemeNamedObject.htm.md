# SchemeNamedObject - класс
##  __Definition
 **Пространство имён:** [Tessa.Scheme](N_Tessa_Scheme.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class SchemeNamedObject : SchemePartionableObject
VB __Копировать
     Public MustInherit Class SchemeNamedObject
    	Inherits SchemePartionableObject
C++ __Копировать
     public ref class SchemeNamedObject abstract : public SchemePartionableObject
F# __Копировать
     [<AbstractClassAttribute>]
    type SchemeNamedObject = 
        class
            inherit SchemePartionableObject
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[SchemeObject](T_Tessa_Scheme_SchemeObject.htm) __[SchemePartionableObject](T_Tessa_Scheme_SchemePartionableObject.htm) __ SchemeNamedObject
Derived
[Tessa.Scheme.SchemeColumn](T_Tessa_Scheme_SchemeColumn.htm)
[Tessa.Scheme.SchemeConstraint](T_Tessa_Scheme_SchemeConstraint.htm)
[Tessa.Scheme.SchemeDatabase](T_Tessa_Scheme_SchemeDatabase.htm)
[Tessa.Scheme.SchemeDatabaseProperties](T_Tessa_Scheme_SchemeDatabaseProperties.htm)
[Tessa.Scheme.SchemeGroupableObject](T_Tessa_Scheme_SchemeGroupableObject.htm)
[Tessa.Scheme.SchemeIndex](T_Tessa_Scheme_SchemeIndex.htm)
[Tessa.Scheme.SchemePartition](T_Tessa_Scheme_SchemePartition.htm)
Подробнее __Less __
##  __Свойства
[Description](P_Tessa_Scheme_SchemeNamedObject_Description.htm)|  
---|---  
[HasSystemControlledName](P_Tessa_Scheme_SchemeNamedObject_HasSystemControlledName.htm)|  
[ID](P_Tessa_Scheme_SchemeNamedObject_ID.htm)|  
[IsPartitionInherited](P_Tessa_Scheme_SchemePartionableObject_IsPartitionInherited.htm)|  
(Унаследован от
[SchemePartionableObject](T_Tessa_Scheme_SchemePartionableObject.htm))  
[IsPermanent](P_Tessa_Scheme_SchemeObject_IsPermanent.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[IsSealed](P_Tessa_Scheme_SchemeObject_IsSealed.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[IsSystem](P_Tessa_Scheme_SchemeObject_IsSystem.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[LinkedWith](P_Tessa_Scheme_SchemeObject_LinkedWith.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[Name](P_Tessa_Scheme_SchemeNamedObject_Name.htm)|  
[Parent](P_Tessa_Scheme_SchemeObject_Parent.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[Partition](P_Tessa_Scheme_SchemePartionableObject_Partition.htm)|  
(Унаследован от
[SchemePartionableObject](T_Tessa_Scheme_SchemePartionableObject.htm))  
##  __Методы
[BeginDeserializationOverride](M_Tessa_Scheme_SchemeNamedObject_BeginDeserializationOverride.htm)|  
(Переопределяет
[SchemeObject.BeginDeserializationOverride(SerializationInfo)](M_Tessa_Scheme_SchemeObject_BeginDeserializationOverride.htm))  
---|---  
[Copy](M_Tessa_Scheme_SchemeNamedObject_Copy.htm)|  
(Переопределяет
[SchemePartionableObject.Copy(SchemeObject)](M_Tessa_Scheme_SchemePartionableObject_Copy.htm))  
[Deserialize](M_Tessa_Scheme_SchemeObject_Deserialize.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[EndDeserializationOverride](M_Tessa_Scheme_SchemePartionableObject_EndDeserializationOverride.htm)|  
(Унаследован от
[SchemePartionableObject](T_Tessa_Scheme_SchemePartionableObject.htm))  
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
[GetDisplayName](M_Tessa_Scheme_SchemeNamedObject_GetDisplayName.htm)|  
(Переопределяет
[SchemeObject.GetDisplayName()](M_Tessa_Scheme_SchemeObject_GetDisplayName.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetInheritedPartition](M_Tessa_Scheme_SchemePartionableObject_GetInheritedPartition.htm)|  
(Унаследован от
[SchemePartionableObject](T_Tessa_Scheme_SchemePartionableObject.htm))  
[GetObjectData](M_Tessa_Scheme_SchemeNamedObject_GetObjectData.htm)|  
(Переопределяет
[SchemePartionableObject.GetObjectData(SerializationInfo)](M_Tessa_Scheme_SchemePartionableObject_GetObjectData.htm))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[IsInvalidPartition](M_Tessa_Scheme_SchemePartionableObject_IsInvalidPartition.htm)|  
(Унаследован от
[SchemePartionableObject](T_Tessa_Scheme_SchemePartionableObject.htm))  
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
