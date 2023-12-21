# SchemePrimaryKey - класс
##  __Definition
 **Пространство имён:** [Tessa.Scheme](N_Tessa_Scheme.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public sealed class SchemePrimaryKey : SchemeUniqueKey
VB __Копировать
    <SerializableAttribute>
    Public NotInheritable Class SchemePrimaryKey
    	Inherits SchemeUniqueKey
C++ __Копировать
    [SerializableAttribute]
    public ref class SchemePrimaryKey sealed : public SchemeUniqueKey
F# __Копировать
     [<SealedAttribute>]
    [<SerializableAttribute>]
    type SchemePrimaryKey = 
        class
            inherit SchemeUniqueKey
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[SchemeObject](T_Tessa_Scheme_SchemeObject.htm) __[SchemePartionableObject](T_Tessa_Scheme_SchemePartionableObject.htm) __[SchemeNamedObject](T_Tessa_Scheme_SchemeNamedObject.htm) __[SchemeConstraint](T_Tessa_Scheme_SchemeConstraint.htm) __[SchemeUniqueKey](T_Tessa_Scheme_SchemeUniqueKey.htm) __ SchemePrimaryKey
##  __Конструкторы
[SchemePrimaryKey()](M_Tessa_Scheme_SchemePrimaryKey__ctor.htm)|
Инициализирует новый экземпляр класса SchemePrimaryKey  
Устарело.  
---|---  
[SchemePrimaryKey(SchemeIndexedColumn[])](M_Tessa_Scheme_SchemePrimaryKey__ctor_2.htm)|
Инициализирует новый экземпляр класса SchemePrimaryKey  
[SchemePrimaryKey(Guid,
SchemeIndexedColumn[])](M_Tessa_Scheme_SchemePrimaryKey__ctor_1.htm)|
Инициализирует новый экземпляр класса SchemePrimaryKey  
##  __Свойства
[AllowPageLocks](P_Tessa_Scheme_SchemeUniqueKey_AllowPageLocks.htm)|  
(Унаследован от [SchemeUniqueKey](T_Tessa_Scheme_SchemeUniqueKey.htm))  
---|---  
[AllowRowLocks](P_Tessa_Scheme_SchemeUniqueKey_AllowRowLocks.htm)|  
(Унаследован от [SchemeUniqueKey](T_Tessa_Scheme_SchemeUniqueKey.htm))  
[Columns](P_Tessa_Scheme_SchemeUniqueKey_Columns.htm)|  
(Унаследован от [SchemeUniqueKey](T_Tessa_Scheme_SchemeUniqueKey.htm))  
[DataCompression](P_Tessa_Scheme_SchemeUniqueKey_DataCompression.htm)|  
(Унаследован от [SchemeUniqueKey](T_Tessa_Scheme_SchemeUniqueKey.htm))  
[Description](P_Tessa_Scheme_SchemeNamedObject_Description.htm)|  
(Унаследован от [SchemeNamedObject](T_Tessa_Scheme_SchemeNamedObject.htm))  
[FillFactor](P_Tessa_Scheme_SchemeUniqueKey_FillFactor.htm)|  
(Унаследован от [SchemeUniqueKey](T_Tessa_Scheme_SchemeUniqueKey.htm))  
[HasSystemControlledName](P_Tessa_Scheme_SchemeConstraint_HasSystemControlledName.htm)|  
(Унаследован от [SchemeConstraint](T_Tessa_Scheme_SchemeConstraint.htm))  
[ID](P_Tessa_Scheme_SchemeNamedObject_ID.htm)|  
(Унаследован от [SchemeNamedObject](T_Tessa_Scheme_SchemeNamedObject.htm))  
[IgnoreDuplicateKey](P_Tessa_Scheme_SchemeUniqueKey_IgnoreDuplicateKey.htm)|  
(Унаследован от [SchemeUniqueKey](T_Tessa_Scheme_SchemeUniqueKey.htm))  
[Index](P_Tessa_Scheme_SchemeUniqueKey_Index.htm)|  
(Унаследован от [SchemeUniqueKey](T_Tessa_Scheme_SchemeUniqueKey.htm))  
[IsClustered](P_Tessa_Scheme_SchemeUniqueKey_IsClustered.htm)|  
(Унаследован от [SchemeUniqueKey](T_Tessa_Scheme_SchemeUniqueKey.htm))  
[IsPadded](P_Tessa_Scheme_SchemeUniqueKey_IsPadded.htm)|  
(Унаследован от [SchemeUniqueKey](T_Tessa_Scheme_SchemeUniqueKey.htm))  
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
(Унаследован от [SchemeNamedObject](T_Tessa_Scheme_SchemeNamedObject.htm))  
[NoRecomputeStatistics](P_Tessa_Scheme_SchemeUniqueKey_NoRecomputeStatistics.htm)|  
(Унаследован от [SchemeUniqueKey](T_Tessa_Scheme_SchemeUniqueKey.htm))  
[Parent](P_Tessa_Scheme_SchemeObject_Parent.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[Partition](P_Tessa_Scheme_SchemePartionableObject_Partition.htm)|  
(Унаследован от
[SchemePartionableObject](T_Tessa_Scheme_SchemePartionableObject.htm))  
[Table](P_Tessa_Scheme_SchemeConstraint_Table.htm)|  
(Унаследован от [SchemeConstraint](T_Tessa_Scheme_SchemeConstraint.htm))  
##  __Методы
[BeginDeserializationOverride](M_Tessa_Scheme_SchemeUniqueKey_BeginDeserializationOverride.htm)|  
(Унаследован от [SchemeUniqueKey](T_Tessa_Scheme_SchemeUniqueKey.htm))  
---|---  
[Copy](M_Tessa_Scheme_SchemeUniqueKey_Copy.htm)|  
(Унаследован от [SchemeUniqueKey](T_Tessa_Scheme_SchemeUniqueKey.htm))  
[Deserialize](M_Tessa_Scheme_SchemeObject_Deserialize.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[EndDeserializationOverride](M_Tessa_Scheme_SchemeUniqueKey_EndDeserializationOverride.htm)|  
(Унаследован от [SchemeUniqueKey](T_Tessa_Scheme_SchemeUniqueKey.htm))  
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
(Унаследован от [SchemeNamedObject](T_Tessa_Scheme_SchemeNamedObject.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetInheritedPartition](M_Tessa_Scheme_SchemePartionableObject_GetInheritedPartition.htm)|  
(Унаследован от
[SchemePartionableObject](T_Tessa_Scheme_SchemePartionableObject.htm))  
[GetObjectData](M_Tessa_Scheme_SchemeUniqueKey_GetObjectData.htm)|  
(Унаследован от [SchemeUniqueKey](T_Tessa_Scheme_SchemeUniqueKey.htm))  
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
